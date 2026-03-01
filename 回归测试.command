#!/bin/zsh
set -e

cd "/Users/lc/Documents/记账本"

exec python3 -m unittest discover -s tests -v
