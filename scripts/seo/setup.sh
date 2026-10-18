#!/usr/bin/env bash
# Oturum başına bir kez: claude-seo skill ve betiklerini klonla, Python bağımlılıklarını kur.
set -euo pipefail
D=/home/user/agricidaniel/claude-seo
[ -d "$D/.git" ] || { mkdir -p "$(dirname "$D")"; GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/AgriciDaniel/claude-seo "$D"; }
pip install -q beautifulsoup4 lxml scikit-learn requests 2>&1 | tail -1 || true
echo "claude-seo hazır: $D (skills: $(ls "$D/skills" | wc -l))"
