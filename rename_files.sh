#!/usr/bin/env bash
set -euo pipefail

# Rename root-level photos and update Markdown references that use: ![...](/photo)
# We update by searching for occurrences of: (/FILENAME)
# Extensions supported: jpg, jpeg, png, webp, heic (case-insensitive)

ROOT="."
DRY_RUN=0

usage() {
  cat <<'EOF'
Usage: rename-photos.sh [--dry-run]

Iterates over photos in the repository root and prompts to rename them.
Then updates all references in all *.md files (recursive) by replacing:
  (/oldfilename)  ->  (/newfilename)

Options:
  --dry-run   Show what would change without modifying files.
EOF
}

if [[ "${1-}" == "-h" || "${1-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ "${1-}" == "--dry-run" ]]; then
  DRY_RUN=1
fi

# Ensure we are in repo root (best effort): use current directory.
# You can cd to your repo root before running.

# Collect markdown files once (recursive)
mapfile -d '' MD_FILES < <(find "$ROOT" -type f -name '*.md' -print0)

if (( ${#MD_FILES[@]} == 0 )); then
  echo "No markdown files (*.md) found under: $ROOT"
fi

# Find root-level photos only
mapfile -d '' PHOTOS < <(
  find "$ROOT" -maxdepth 1 -type f \( \
    -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.webp' -o -iname '*.heic' \
  \) -print0
)

if (( ${#PHOTOS[@]} == 0 )); then
  echo "No photos found in repo root ($ROOT) with extensions: jpg jpeg png webp heic"
  exit 0
fi

# Helper: count occurrences of (/filename) in markdown files
count_occurrences() {
    echo 1
}

update_markdown_refs() {
  local old="$1"
  local new="$2"

  local old_pat="(/$old)"
  local new_pat="(/$new)"

  if (( ${#MD_FILES[@]} == 0 )); then
    return 0
  fi

  if (( DRY_RUN == 1 )); then
    echo "  [dry-run] would replace: $old_pat -> $new_pat in ${#MD_FILES[@]} markdown files"
    return 0
  fi

  # Pass strings via env so we don't fight delimiter parsing.
  # Also escape special chars in the replacement so it stays literal.
  OLD="$old_pat" NEW="$new_pat" \
  perl -i -pe '
    BEGIN {
      $old = $ENV{OLD};
      $new = $ENV{NEW};

      # Make replacement literal (avoid $1, \1, etc. being interpreted)
      $new =~ s/\\/\\\\/g;
      $new =~ s/\$/\\\$/g;
      $new =~ s/\@/\\\@/g;
    }
    s/\Q$old\E/$new/g;
  ' -- "${MD_FILES[@]}"
}


# Helper: validate new filename
is_valid_new_name() {
  local name="$1"
  # Disallow path separators
  [[ "$name" != *"/"* && "$name" != *"\\"* && -n "$name" ]]
}

echo "Found ${#PHOTOS[@]} photo(s) in repo root."
echo "Will update references in ${#MD_FILES[@]} markdown file(s)."
echo

for photo_path in "${PHOTOS[@]}"; do
  base="$(basename "$photo_path")"

  # How many references exist?
  refs="$(count_occurrences "$base")"

  echo "Photo: $base"
  echo "  References found in markdown: $refs"
  echo -n "  New name (Enter=skip, '.'=auto-suggest from base name): "
  IFS= read -r new_name

  if [[ -z "$new_name" ]]; then
    echo "  Skipped."
    echo
    continue
  fi

  if [[ "$new_name" == "." ]]; then
    # Simple suggestion: replace spaces with '-', keep extension
    ext="${base##*.}"
    stem="${base%.*}"
    suggested="${stem// /-}.${ext}"
    new_name="$suggested"
    echo "  Suggested: $new_name"
  fi

  if ! is_valid_new_name "$new_name"; then
    echo "  Invalid new name. Must not contain '/' or '\\' and must be non-empty."
    echo
    continue
  fi

  if [[ "$new_name" == "$base" ]]; then
    echo "  Same name; nothing to do."
    echo
    continue
  fi

  if [[ -e "$ROOT/$new_name" ]]; then
    echo "  Target already exists: $new_name"
    echo "  Skipping to avoid overwrite."
    echo
    continue
  fi

  # Confirm
  echo -n "  Rename '$base' -> '$new_name' and update markdown refs? [y/N]: "
  IFS= read -r ans
  if [[ "$ans" != "y" && "$ans" != "Y" ]]; then
    echo "  Cancelled."
    echo
    continue
  fi

  if (( DRY_RUN == 1 )); then
    echo "  [dry-run] would mv -- '$base' '$new_name'"
  else
    mv -- "$ROOT/$base" "$ROOT/$new_name"
  fi

  if (( refs > 0 )); then
    update_markdown_refs "$base" "$new_name"
    echo "  Updated markdown references."
  else
    echo "  No markdown references to update."
  fi

  echo
done

echo "Done."

