#!/usr/bin/env bash
set -euo pipefail


die() { printf 'Error: %s\n' "$*" >&2; exit 1; }

if (( $# != 2 )); then
  die "Expected 2 args: oldfile newfile_base"
fi

oldfile="$1"
newbase="$2"


# Filenames have no subpaths per requirement; enforce to avoid surprises.
[[ "$oldfile" == */* ]] && die "oldfile must not contain '/'"
[[ "$newbase" == */* ]] && die "newfile_base must not contain '/'"

[[ -e "$oldfile" ]] || die "oldfile '$oldfile' does not exist"

# Extract extension (text after last dot). If no dot, extension is empty.
ext="${oldfile##*.}"
newfile="${newbase}.${ext}"
[[ ! -e "$newfile" ]] || die "target '$newfile' already exists"

mv -- "$oldfile" "$newfile"
lower_ext="${ext,,}"
if [[ "$lower_ext" != "png" ]]; then
    pngfile="${newbase}.png"
    [[ ! -e "$pngfile" ]] || die "cannot re-encode: '$pngfile' already exists"
    ffmpeg -hide_banner -loglevel error -y -i "$newfile" "$pngfile"
    rm -f -- "$newfile"
    newfile="$pngfile"
fi

escape_sed_repl() {
  # Escape backslashes, ampersands, and delimiter '|'
  # (for sed replacement part)
  printf '%s' "$1" | sed -e 's/[\/&|\\]/\\&/g'
}
escape_sed_pat() {
  # Escape for sed pattern (basic regex) so oldfile is treated literally
  printf '%s' "$1" | sed -e 's/[][(){}.^$*+?|\\\/]/\\&/g'
}

old_pat="$(escape_sed_pat "$oldfile")"
new_rep="$(escape_sed_repl "$newfile")"

while IFS= read -r -d '' f; do
    sed -i "s|$old_pat|$new_rep|g" "$f"
done < <(find . -type f -name '*.md' -print0)

git add $(git diff --name-only | grep .md)
git add -A -- "$oldfile" "$newfile"
git commit -m "Rename image $oldfile to $newfile"







