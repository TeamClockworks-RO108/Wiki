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
import re
import os
import shutil
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


def sync(repo_root):
    """Sync operation (not yet implemented)."""
    print("Sync is not yet implemented.")


def main():
    parser = argparse.ArgumentParser(description="WikiSync utility")
    parser.add_argument('repo_root', nargs='?', default=os.getcwd(),
                        help="Path to the repository root (default: current directory)")
    parser.add_argument('--relocate-images', action='store_true',
                        help="Relocate images next to the markdown files that reference them")
    parser.add_argument('--sync', action='store_true',
                        help="Sync operation (not yet implemented)")
    args = parser.parse_args()

    repo_root = os.path.abspath(args.repo_root)

    if not args.relocate_images and not args.sync:
        parser.print_help()
        sys.exit(1)

    if args.relocate_images:
        relocate_images(repo_root)

    if args.sync:
        sync(repo_root)


if __name__ == '__main__':
    main()
