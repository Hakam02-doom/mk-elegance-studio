#!/bin/zsh
set -e
S=${0:A:h}
SITE="/Users/hakam/Library/Application Support/Claude/scratch-workspaces/78f59744-3440-4f83-8fe6-33cefd4ed061/dddfd7f4-6df2-4d7f-bc03-5dca84a9f6fd/scratch-2026-11-27-15d728/site"
python3 -I $S/tools/rebrand.py $S/pristine "$SITE" $S/orig_assets > /dev/null
$S/venv/bin/python -I $S/tools/siteify.py "$SITE"
