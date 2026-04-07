#!/usr/bin/env python3
"""
Scan all markdown files in a repository for image references like:
    ![alt text](/path/to/image.png)
    ![alt text](/path/to/image.png =50%x50%)

Move each referenced image to sit next to the markdown file that references it,
and update the markdown reference accordingly.

Images under /branding or /static are left untouched.
"""

import argparse
from datetime import datetime, timezone
import re
import os
import shutil
import subprocess
import sys
from collections import Counter

IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.bmp', '.ico', '.tiff', '.tif'}

# Regex breakdown:
#   ![alt](  /path/to/image.ext  optional_size_descriptor  )
# The path may contain parentheses (e.g. "image_(1).png") so we anchor on a known
# image extension rather than stopping at ')'. The path has no spaces.
_EXT = r'\.(?:png|jpe?g|gif|webp|svg|bmp|ico|tiff?)'
IMAGE_ABS_RE = re.compile(r'!\[([^\]]*)\]\((/[^\s]+?' + _EXT + r')(\s+[^)]*)?\)', re.IGNORECASE)
IMAGE_ANY_RE = re.compile(r'!\[([^\]]*)\]\(([^\s]+?' + _EXT + r')(\s+[^)]*)?\)', re.IGNORECASE)


def find_image_refs(repo_root, absolute_only=True):
    """Walk all .md files and collect image references.

    If absolute_only=True, only match paths starting with /.
    If absolute_only=False, match all image references (including relative).

    Returns a list of dicts:
        md_file: absolute path to the markdown file
        alt: alt text
        img_path: the path from the reference
        suffix: everything after the image path inside the parens (size descriptor etc.)
        match_text: full original match string
    """
    pattern = IMAGE_ABS_RE if absolute_only else IMAGE_ANY_RE
    refs = []
    for dirpath, _, filenames in os.walk(repo_root):
        # Skip .git
        if '/.git' in dirpath or dirpath.endswith('/.git'):
            continue
        for fname in filenames:
            if not fname.endswith('.md'):
                continue
            md_file = os.path.join(dirpath, fname)
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            for m in pattern.finditer(content):
                refs.append({
                    'md_file': md_file,
                    'alt': m.group(1),
                    'img_path': m.group(2),
                    'suffix': m.group(3) or '',  # e.g. " =50%x50%" or ""
                    'match_text': m.group(0),
                })
    return refs


def find_all_images(repo_root):
    """Find all image files in the repo (excluding .git)."""
    images = []
    for dirpath, _, filenames in os.walk(repo_root):
        if '/.git' in dirpath or dirpath.endswith('/.git'):
            continue
        for fname in filenames:
            ext = os.path.splitext(fname)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                images.append(os.path.join(dirpath, fname))
    return images


def relocate_images(repo_root):
    """Relocate images to sit next to the markdown files that reference them."""
    print(f"Scanning repository: {repo_root}")

    refs = find_image_refs(repo_root)

    if not refs:
        print("No absolute image references to relocate.\n")
    else:
        print(f"Found {len(refs)} image reference(s) to relocate.\n")

    img_ref_counts = Counter(ref['img_path'] for ref in refs
                             if not ref['img_path'].startswith('/branding/')
                             and not ref['img_path'].startswith('/static/'))

    for ref in refs:
        img_path = ref['img_path']       # e.g. /screenshots/screenshot.png
        md_file = ref['md_file']

        # Skip images under /branding or /static
        if img_path.startswith('/branding/') or img_path.startswith('/static/'):
            print(f"SKIP (branding/static): {img_path}  (in {os.path.relpath(md_file, repo_root)})")
            continue

        # Skip images referenced more than once
        if img_ref_counts[img_path] > 1:
            print(f"SKIP (referenced {img_ref_counts[img_path]} times): {img_path}  (in {os.path.relpath(md_file, repo_root)})")
            continue

        img_abs = os.path.join(repo_root, img_path.lstrip('/'))
        md_dir = os.path.dirname(md_file)
        img_basename = os.path.basename(img_path)
        new_img_abs = os.path.join(md_dir, img_basename)

        # Check if image file exists
        if not os.path.isfile(img_abs):
            print(f"WARNING: image not found: {img_abs}  (referenced in {os.path.relpath(md_file, repo_root)})")
            continue

        # Check if already in the right place
        if os.path.normpath(img_abs) == os.path.normpath(new_img_abs):
            print(f"OK (already in place): {img_path}  (in {os.path.relpath(md_file, repo_root)})")
            continue

        # Handle name collision at destination
        if os.path.exists(new_img_abs):
            print(f"WARNING: destination already exists: {new_img_abs}  — skipping")
            continue

        # Move the image
        print(f"MOVE: {os.path.relpath(img_abs, repo_root)}  ->  {os.path.relpath(new_img_abs, repo_root)}")
        shutil.move(img_abs, new_img_abs)

        # Update the markdown reference: absolute path from repo root
        old_ref = ref['match_text']
        new_abs_path = '/' + os.path.relpath(new_img_abs, repo_root)
        new_ref = f"![{ref['alt']}]({new_abs_path}{ref['suffix']})"

        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace(old_ref, new_ref, 1)

        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Updated reference in {os.path.relpath(md_file, repo_root)}: {old_ref}  ->  {new_ref}")

    # --- Stage 1b: Fix relative image references to absolute ---
    print("\n--- Fixing relative image references ---\n")

    rel_refs = find_image_refs(repo_root, absolute_only=False)
    for ref in rel_refs:
        img_path = ref['img_path']
        if img_path.startswith('/'):
            continue  # already absolute

        md_file = ref['md_file']
        md_dir = os.path.dirname(md_file)
        img_abs = os.path.normpath(os.path.join(md_dir, img_path))

        if not os.path.isfile(img_abs):
            continue

        abs_path = '/' + os.path.relpath(img_abs, repo_root)
        old_ref = ref['match_text']
        new_ref = f"![{ref['alt']}]({abs_path}{ref['suffix']})"

        if old_ref == new_ref:
            continue

        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace(old_ref, new_ref, 1)

        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  FIX: {old_ref}  ->  {new_ref}  (in {os.path.relpath(md_file, repo_root)})")

    # --- Stage 1c: Convert non-PNG images to PNG ---
    print("\n--- Converting non-PNG images to PNG ---\n")

    CONVERT_EXTENSIONS = {'.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.ico', '.tiff', '.tif'}
    all_refs_for_convert = find_image_refs(repo_root, absolute_only=False)
    converted = 0

    for ref in all_refs_for_convert:
        img_path = ref['img_path']
        md_file = ref['md_file']

        # Resolve to absolute path
        if img_path.startswith('/'):
            img_abs = os.path.join(repo_root, img_path.lstrip('/'))
        else:
            img_abs = os.path.normpath(os.path.join(os.path.dirname(md_file), img_path))

        ext = os.path.splitext(img_abs)[1].lower()
        if ext not in CONVERT_EXTENSIONS:
            continue

        if not os.path.isfile(img_abs):
            continue

        # Skip branding/static
        img_rel = os.path.relpath(img_abs, repo_root)
        parts = img_rel.split(os.sep)
        if parts[0] in ('branding', 'static'):
            continue

        # Convert to PNG
        png_abs = os.path.splitext(img_abs)[0] + '.png'
        if os.path.exists(png_abs):
            print(f"WARNING: conversion target already exists: {os.path.relpath(png_abs, repo_root)} — skipping")
            continue

        print(f"CONVERT: {img_rel}  ->  {os.path.relpath(png_abs, repo_root)}")
        result = subprocess.run(
            ['magick', img_abs, png_abs],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  ERROR: magick failed: {result.stderr.strip()}")
            continue

        os.remove(img_abs)

        # Update the markdown reference — replace extension in both alt and path
        old_ref = ref['match_text']
        new_img_path = os.path.splitext(img_path)[0] + '.png'
        new_alt = os.path.splitext(ref['alt'])[0] + '.png' if os.path.splitext(ref['alt'])[1].lower() in CONVERT_EXTENSIONS else ref['alt']
        new_ref = f"![{new_alt}]({new_img_path}{ref['suffix']})"

        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace(old_ref, new_ref, 1)

        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Updated reference in {os.path.relpath(md_file, repo_root)}")
        converted += 1

    if converted == 0:
        print("No images to convert.")
    else:
        print(f"\nConverted {converted} image(s) to PNG.")

    # --- Stage 2: Delete unreferenced images outside /branding and /static ---
    print("\n--- Checking for unreferenced images ---\n")

    # Re-scan all refs (including relative paths now) to build the full set of referenced images
    all_refs = find_image_refs(repo_root, absolute_only=False)
    referenced_abs_paths = set()
    for ref in all_refs:
        img_path = ref['img_path']
        if img_path.startswith('/'):
            # Absolute repo path
            referenced_abs_paths.add(os.path.normpath(os.path.join(repo_root, img_path.lstrip('/'))))
        else:
            # Relative path — resolve from the markdown file's directory
            md_dir = os.path.dirname(ref['md_file'])
            referenced_abs_paths.add(os.path.normpath(os.path.join(md_dir, img_path)))

    all_images = find_all_images(repo_root)
    branding_static = []
    referenced = []
    unreferenced = []

    for img_abs in all_images:
        img_rel = os.path.relpath(img_abs, repo_root)
        parts = img_rel.split(os.sep)
        if parts[0] in ('branding', 'static'):
            branding_static.append(img_rel)
        elif os.path.normpath(img_abs) in referenced_abs_paths:
            referenced.append(img_rel)
        else:
            unreferenced.append(img_rel)

    total = len(all_images)
    print(f"Total images found:      {total}")
    print(f"  Branding/static:       {len(branding_static)}")
    print(f"  Referenced:            {len(referenced)}")
    print(f"  Unreferenced:          {len(unreferenced)}")

    for img_rel in unreferenced:
        img_abs = os.path.join(repo_root, img_rel)
        print(f"DELETE (unreferenced): {img_rel}")
        os.remove(img_abs)

    if unreferenced:
        print(f"\nDeleted {len(unreferenced)} unreferenced image(s).")

    print("\nDone.")


# ---------------------------------------------------------------------------
# Sync: bidirectional page synchronization between two wiki repos
# ---------------------------------------------------------------------------

# Words to search for across two consecutive '>' lines to identify a sync marker.
_SYNC_WORDS = [
    'available', 'wiki', 'clockworks', 'alacrity',
    'page', 'id', 'synchronization', 'automatically', 'automagically',
]
_SYNC_THRESHOLD = 0.6  # at least 60 % of the words must be present

# Extracts the PAGEID from inside backticks on the second line.
_PAGEID_RE = re.compile(r'`([-_a-zA-Z0-9]+)`')


def find_sync_markers(repo_root):
    """Scan all .md files for sync markers.

    Returns a list of dicts:
        md_file:  absolute path to the markdown file
        rel_path: path relative to repo_root
        page_id:  the extracted PAGEID string
    """
    results = []
    for dirpath, _, filenames in os.walk(repo_root):
        if '/.git' in dirpath or dirpath.endswith('/.git'):
            continue
        for fname in filenames:
            if not fname.endswith('.md'):
                continue
            md_file = os.path.join(dirpath, fname)
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            for i in range(len(lines) - 1):
                line1 = lines[i]
                line2 = lines[i + 1]

                if not line1.lstrip().startswith('>'):
                    continue
                if not line2.lstrip().startswith('>'):
                    continue

                combined = (line1 + ' ' + line2).lower()
                found = sum(1 for w in _SYNC_WORDS if w in combined)
                if found < len(_SYNC_WORDS) * _SYNC_THRESHOLD:
                    continue

                m = _PAGEID_RE.search(line2)
                if not m:
                    continue

                results.append({
                    'md_file': md_file,
                    'rel_path': os.path.relpath(md_file, repo_root),
                    'page_id': m.group(1),
                })
    return results


def _git(*args, repo=None, check=True):
    """Run a git command and return stdout."""
    cmd = ['git']
    if repo:
        cmd += ['-C', repo]
    cmd += list(args)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode != 0:
        return None
    return r.stdout.strip()


def _find_last_sync_commit(repo_root, page_id):
    """Return the SHA of the newest commit whose message contains PAGEID=<id>."""
    return _git('log', '--all', '-1', '--format=%H',
                f'--grep=PAGEID={page_id}', repo=repo_root)


def _get_file_at_commit(repo_root, commit, rel_path):
    """Return the contents of a file at a given commit, or None."""
    return _git('show', f'{commit}:{rel_path}', repo=repo_root)


def _three_way_merge(base_content, content_a, content_b, newer_side):
    """Three-way merge of content_a and content_b with base_content as ancestor.

    Uses git merge-file with diff3 style. On conflict, the side indicated by
    newer_side ('a' or 'b') wins.

    Returns (merged_content, had_conflicts).
    """
    import tempfile

    tmp_base = tempfile.NamedTemporaryFile(mode='w', suffix='.base', delete=False)
    tmp_a = tempfile.NamedTemporaryFile(mode='w', suffix='.a', delete=False)
    tmp_b = tempfile.NamedTemporaryFile(mode='w', suffix='.b', delete=False)

    try:
        tmp_base.write(base_content); tmp_base.close()
        tmp_a.write(content_a); tmp_a.close()
        tmp_b.write(content_b); tmp_b.close()

        # git merge-file modifies the first file in-place with the merge result.
        # Return code: 0 = clean, >0 = number of conflicts, <0 = error.
        # --diff3 gives the base in conflict markers for clarity.
        r = subprocess.run(
            ['git', 'merge-file', '--diff3',
             '-L', 'A', '-L', 'BASE', '-L', 'B',
             tmp_a.name, tmp_base.name, tmp_b.name],
            capture_output=True, text=True,
        )

        had_conflicts = r.returncode > 0

        with open(tmp_a.name, 'r', encoding='utf-8') as f:
            merged = f.read()

        if had_conflicts:
            # Resolve conflicts by picking the newer side
            merged = _resolve_conflicts(merged, newer_side)

        return merged, had_conflicts

    finally:
        os.remove(tmp_base.name)
        os.remove(tmp_a.name)
        os.remove(tmp_b.name)


def _resolve_conflicts(text, pick):
    """Resolve diff3-style conflict markers by keeping the chosen side.

    pick: 'a' keeps the A side, 'b' keeps the B side.
    Handles both diff3 markers (with ||||||| BASE) and standard markers.
    """
    lines = text.splitlines(keepends=True)
    result = []
    in_conflict = False
    section = None  # 'a', 'base', or 'b'

    for line in lines:
        if line.startswith('<<<<<<<'):
            in_conflict = True
            section = 'a'
            continue
        elif line.startswith('|||||||'):
            section = 'base'
            continue
        elif line.startswith('=======\n') or line.rstrip() == '=======':
            section = 'b'
            continue
        elif line.startswith('>>>>>>>'):
            in_conflict = False
            section = None
            continue

        if not in_conflict:
            result.append(line)
        elif section == pick:
            result.append(line)

    return ''.join(result)


_DATE_RE = re.compile(r'^date:\s*(.+)$', re.MULTILINE)


def _get_page_date(md_file):
    """Extract the 'date' field from the YAML frontmatter of a markdown file.

    Returns a datetime object or None if not found / unparseable.
    """
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Frontmatter must start at the very beginning with ---
    if not content.startswith('---'):
        return None
    end = content.find('---', 3)
    if end == -1:
        return None
    frontmatter = content[3:end]

    m = _DATE_RE.search(frontmatter)
    if not m:
        return None

    date_str = m.group(1).strip()
    # Try ISO 8601 formats
    for fmt in ('%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%SZ',
                '%Y-%m-%dT%H:%M:%S.%f%z', '%Y-%m-%dT%H:%M:%S%z',
                '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d'):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def _commit_page(repo_root, page_id, rel_path, allow_empty=False):
    """Stage and commit changes for a single synced page (no push).

    If allow_empty is True, create a dummy commit even when there are no changes
    (used to establish a PAGEID baseline on the source side).
    """
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    msg = f"Sync for PAGEID={page_id} at {now}"

    _git('add', rel_path, repo=repo_root)

    # Check if there is anything staged
    r = subprocess.run(
        ['git', '-C', repo_root, 'diff', '--cached', '--quiet'],
        capture_output=True,
    )
    if r.returncode == 0:
        if not allow_empty:
            return  # nothing to commit
        _git('commit', '--allow-empty', '-m', msg, repo=repo_root, check=False)
    else:
        _git('commit', '-m', msg, repo=repo_root, check=False)

    print(f"    Committed: {msg}")


def _get_page_image_refs(md_file):
    """Extract all image paths referenced in a single markdown file.

    Returns a set of repo-relative paths (starting with /).
    """
    pattern = IMAGE_ANY_RE
    refs = set()
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    for m in pattern.finditer(content):
        refs.add(m.group(2))
    return refs


def _file_hash(path):
    """Return the SHA-256 hex digest of a file."""
    import hashlib
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def _last_real_change_date(repo_root, rel_path):
    """Return the author date of the last commit that touched rel_path,
    ignoring commits created by Sync (messages starting with 'Sync for PAGEID=').

    Returns a datetime or None.
    """
    # Get all commits that touched this file, newest first
    out = _git('log', '--format=%H %aI %s', '--follow', '--', rel_path,
               repo=repo_root)
    if not out:
        return None

    for line in out.splitlines():
        parts = line.split(' ', 2)
        if len(parts) < 3:
            continue
        _, date_str, subject = parts
        if subject.startswith('Sync for PAGEID='):
            continue
        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            continue
    return None


def _resolve_img_path(img_path, md_file, repo_root):
    """Resolve an image path (absolute or relative) to an absolute filesystem path."""
    if img_path.startswith('/'):
        return os.path.join(repo_root, img_path.lstrip('/'))
    else:
        return os.path.normpath(os.path.join(os.path.dirname(md_file), img_path))


def _sync_media(repo_a, repo_b, info_a, info_b, page_id):
    """Synchronize media (images) referenced by a synced page pair.

    After text sync, both pages should be identical, so their image refs match.
    We read from one side (A) since refs are the same.

    Steps:
      1. Delete unreferenced images in both repos (repo-wide, like --relocate)
      2. Copy missing images from the other side
      3. For images present on both sides with different hashes, keep the one
         with the most recent non-sync commit
    """
    print(f"\n  --- Media sync for PAGEID={page_id} ---")

    # Pages should be identical after text sync — read refs from A
    refs = _get_page_image_refs(info_a['md_file'])
    if not refs:
        print(f"    No image references in page")
        return

    print(f"    {len(refs)} image reference(s) found")

    # Step 1: Delete unreferenced images in both repos
    for label, repo, info in [('A', repo_a, info_a), ('B', repo_b, info_b)]:
        all_repo_refs = find_image_refs(repo, absolute_only=False)
        referenced_abs = set()
        for ref in all_repo_refs:
            referenced_abs.add(os.path.normpath(
                _resolve_img_path(ref['img_path'], ref['md_file'], repo)))

        all_imgs = find_all_images(repo)
        for img_abs in all_imgs:
            img_rel = os.path.relpath(img_abs, repo)
            parts = img_rel.split(os.sep)
            if parts[0] in ('branding', 'static'):
                continue
            if os.path.normpath(img_abs) not in referenced_abs:
                print(f"    DELETE (unreferenced in {label}): {img_rel}")
                os.remove(img_abs)

    # Step 2: Copy missing images from the other side
    staged_files_a = []
    staged_files_b = []

    for img_path in sorted(refs):
        abs_a = _resolve_img_path(img_path, info_a['md_file'], repo_a)
        abs_b = _resolve_img_path(img_path, info_b['md_file'], repo_b)

        exists_a = os.path.isfile(abs_a)
        exists_b = os.path.isfile(abs_b)

        rel_a = os.path.relpath(abs_a, repo_a)
        rel_b = os.path.relpath(abs_b, repo_b)

        if not exists_a and not exists_b:
            print(f"    WARNING: {img_path} missing on both sides")
            continue

        if not exists_a and exists_b:
            os.makedirs(os.path.dirname(abs_a), exist_ok=True)
            shutil.copy2(abs_b, abs_a)
            staged_files_a.append(rel_a)
            print(f"    COPY B -> A: {img_path}")
            continue

        if exists_a and not exists_b:
            os.makedirs(os.path.dirname(abs_b), exist_ok=True)
            shutil.copy2(abs_a, abs_b)
            staged_files_b.append(rel_b)
            print(f"    COPY A -> B: {img_path}")
            continue

        # Step 3: Both exist — compare hashes
        hash_a = _file_hash(abs_a)
        hash_b = _file_hash(abs_b)

        if hash_a == hash_b:
            continue  # identical

        # Different content — newest non-sync commit wins
        date_a = _last_real_change_date(repo_a, rel_a)
        date_b = _last_real_change_date(repo_b, rel_b)

        date_a_str = date_a.isoformat() if date_a else 'unknown'
        date_b_str = date_b.isoformat() if date_b else 'unknown'

        if date_a and date_b:
            winner = 'a' if date_a >= date_b else 'b'
        elif date_a:
            winner = 'a'
        elif date_b:
            winner = 'b'
        else:
            winner = 'a'  # arbitrary fallback

        if winner == 'a':
            shutil.copy2(abs_a, abs_b)
            staged_files_b.append(rel_b)
            print(f"    OVERWRITE A -> B: {img_path}  (A: {date_a_str}, B: {date_b_str})")
        else:
            shutil.copy2(abs_b, abs_a)
            staged_files_a.append(rel_a)
            print(f"    OVERWRITE B -> A: {img_path}  (A: {date_a_str}, B: {date_b_str})")

    # Commit media changes (one commit per page, not per file)
    if staged_files_a:
        for f in staged_files_a:
            _git('add', f, repo=repo_a)
        now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        _git('commit', '-m', f"Sync media for PAGEID={page_id} at {now}",
             repo=repo_a, check=False)
        print(f"    Committed media changes in A")

    if staged_files_b:
        for f in staged_files_b:
            _git('add', f, repo=repo_b)
        now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        _git('commit', '-m', f"Sync media for PAGEID={page_id} at {now}",
             repo=repo_b, check=False)
        print(f"    Committed media changes in B")

    if not staged_files_a and not staged_files_b:
        print(f"    Media already in sync")


def sync(repo_a, repo_b):
    """Synchronize pages between two repositories based on sync markers."""
    print(f"=== WikiSync — bidirectional page sync ===\n")
    print(f"  Repo A: {repo_a}")
    print(f"  Repo B: {repo_b}\n")

    # Reset and pull both repos to ensure a clean, up-to-date state
    for label, repo in [('A', repo_a), ('B', repo_b)]:
        print(f"  Preparing repo {label}...")
        _git('reset', '--hard', repo=repo)
        subprocess.run(['git', '-C', repo, 'clean', '-f'],
                        capture_output=True)
        _git('pull', repo=repo, check=False)

    print()

    markers_a = find_sync_markers(repo_a)
    markers_b = find_sync_markers(repo_b)

    by_id_a = {m['page_id']: m for m in markers_a}
    by_id_b = {m['page_id']: m for m in markers_b}

    common_ids = sorted(set(by_id_a) & set(by_id_b))
    only_a = sorted(set(by_id_a) - set(by_id_b))
    only_b = sorted(set(by_id_b) - set(by_id_a))

    print(f"Sync markers found:")
    print(f"  Repo A:          {len(markers_a)}")
    print(f"  Repo B:          {len(markers_b)}")
    print(f"  Matched pairs:   {len(common_ids)}")
    if only_a:
        print(f"  Only in A:       {', '.join(only_a)}")
    if only_b:
        print(f"  Only in B:       {', '.join(only_b)}")

    if not common_ids:
        print("\nNo pages to sync.")
        return

    for page_id in common_ids:
        info_a = by_id_a[page_id]
        info_b = by_id_b[page_id]

        print(f"\n--- PAGEID={page_id} ---")
        print(f"  A: {info_a['rel_path']}")
        print(f"  B: {info_b['rel_path']}")

        # Find the last sync commit in each repo
        commit_a = _find_last_sync_commit(repo_a, page_id)
        commit_b = _find_last_sync_commit(repo_b, page_id)

        if not commit_a or not commit_b:
            # No baseline — copy the newer page over the older one
            date_a = _get_page_date(info_a['md_file'])
            date_b = _get_page_date(info_b['md_file'])

            date_a_str = date_a.isoformat() if date_a else 'unknown'
            date_b_str = date_b.isoformat() if date_b else 'unknown'
            print(f"  No baseline sync commit — initial copy by date")
            print(f"    A date: {date_a_str}")
            print(f"    B date: {date_b_str}")

            if date_a is None and date_b is None:
                print(f"  SKIP — no date found on either side")
                continue

            # Determine source (newer) and destination (older / no date)
            if date_a is None:
                src, dst = info_b, info_a
                direction = 'B -> A'
            elif date_b is None:
                src, dst = info_a, info_b
                direction = 'A -> B'
            elif date_a >= date_b:
                src, dst = info_a, info_b
                direction = 'A -> B'
            else:
                src, dst = info_b, info_a
                direction = 'B -> A'

            # Check if files are already identical
            import filecmp
            if filecmp.cmp(src['md_file'], dst['md_file'], shallow=False):
                print(f"  Already identical — nothing to do")
            else:
                print(f"  COPY ({direction}): {src['rel_path']}  ->  {dst['rel_path']}")
                shutil.copy2(src['md_file'], dst['md_file'])
                dst_repo = repo_a if dst == info_a else repo_b
                src_repo = repo_a if src == info_a else repo_b
                _commit_page(dst_repo, page_id, dst['rel_path'])
                # Dummy baseline on source so future diffs have an anchor
                _commit_page(src_repo, page_id, src['rel_path'], allow_empty=True)

        else:
            short_a = commit_a[:12]
            short_b = commit_b[:12]
            print(f"  Last sync commit A: {short_a}")
            print(f"  Last sync commit B: {short_b}")

            # Get the file content at the sync point (the common baseline)
            base_a = _get_file_at_commit(repo_a, commit_a, info_a['rel_path'])
            base_b = _get_file_at_commit(repo_b, commit_b, info_b['rel_path'])

            if base_a is None:
                print(f"  SKIP — cannot read {info_a['rel_path']} at {short_a} in repo A")
                continue
            if base_b is None:
                print(f"  SKIP — cannot read {info_b['rel_path']} at {short_b} in repo B")
                continue

            # Read current working-tree content
            with open(info_a['md_file'], 'r', encoding='utf-8') as f:
                current_a = f.read()
            with open(info_b['md_file'], 'r', encoding='utf-8') as f:
                current_b = f.read()

            changed_a = current_a != base_a
            changed_b = current_b != base_b

            if not changed_a and not changed_b:
                print(f"  No changes in either repo since last sync")
            else:
                # Determine which side is newer (for conflict resolution)
                date_a = _get_page_date(info_a['md_file'])
                date_b = _get_page_date(info_b['md_file'])
                if date_a and date_b:
                    newer_side = 'a' if date_a >= date_b else 'b'
                elif date_a:
                    newer_side = 'a'
                elif date_b:
                    newer_side = 'b'
                else:
                    newer_side = 'a'  # arbitrary fallback

                # Use the baseline that both sides diverged from.
                # Since content was identical at sync time, base_a == base_b; pick either.
                base = base_a

                if changed_a and not changed_b:
                    print(f"  Only A changed — copying A -> B")
                    merged = current_a
                elif changed_b and not changed_a:
                    print(f"  Only B changed — copying B -> A")
                    merged = current_b
                else:
                    print(f"  Both sides changed — three-way merge (conflicts -> {newer_side.upper()})")
                    merged, had_conflicts = _three_way_merge(base, current_a, current_b, newer_side)
                    if had_conflicts:
                        print(f"    Conflicts resolved in favour of side {newer_side.upper()}")
                    else:
                        print(f"    Merged cleanly")

                # Write merged content to both sides
                with open(info_a['md_file'], 'w', encoding='utf-8') as f:
                    f.write(merged)
                with open(info_b['md_file'], 'w', encoding='utf-8') as f:
                    f.write(merged)

                _commit_page(repo_a, page_id, info_a['rel_path'])
                _commit_page(repo_b, page_id, info_b['rel_path'])

        # --- Media sync for this page ---
        _sync_media(repo_a, repo_b, info_a, info_b, page_id)

    # Push all commits at once
    print("\n--- Pushing ---")
    for label, repo in [('A', repo_a), ('B', repo_b)]:
        result = _git('push', repo=repo, check=False)
        if result is None:
            print(f"  WARNING: push failed for repo {label} ({repo})")
        else:
            print(f"  Repo {label}: pushed")

    print("\nSync done.")


def main():
    parser = argparse.ArgumentParser(description="WikiSync utility")
    parser.add_argument('repos', nargs='*',
                        help="Repository path(s): one for --relocate, two for --sync")
    parser.add_argument('-r', '--relocate', action='store_true',
                        help="Relocate images next to the markdown files that reference them")
    parser.add_argument('-s', '--sync', action='store_true',
                        help="Bidirectional page sync between two repos using PAGEID markers")
    args = parser.parse_args()

    if not args.relocate and not args.sync:
        parser.print_help()
        sys.exit(1)

    if args.relocate:
        repo = os.path.abspath(args.repos[0]) if args.repos else os.getcwd()
        relocate_images(repo)

    if args.sync:
        if len(args.repos) < 2:
            print("ERROR: --sync requires two repository paths", file=sys.stderr)
            sys.exit(1)
        repo_a = os.path.abspath(args.repos[0])
        repo_b = os.path.abspath(args.repos[1])
        sync(repo_a, repo_b)


if __name__ == '__main__':
    main()
