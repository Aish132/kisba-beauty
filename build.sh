#!/usr/bin/env bash
# build.sh — Render build script for Kisba Beauty

set -o errexit  # exit on any error

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
