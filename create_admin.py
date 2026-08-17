"""
One-time script to create/reset the superuser on Render.
Run via: python create_admin.py
Remove this file after the admin account is confirmed working.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kasbi.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import connection

User = get_user_model()

# Print which database we are connected to
db = connection.settings_dict
print(f"==> Database engine : {db['ENGINE']}")
print(f"==> Database name   : {db.get('NAME', 'n/a')}")
print(f"==> Database host   : {db.get('HOST', 'localhost (sqlite)')}")

username = os.environ.get('ADMIN_USERNAME', 'admin')
email    = os.environ.get('ADMIN_EMAIL',    'admin@kisbabeauty.com')
password = os.environ.get('ADMIN_PASSWORD', 'Admin@1234')

print(f"==> Creating/updating superuser '{username}' ...")

user, created = User.objects.get_or_create(username=username)
user.email        = email
user.is_staff     = True
user.is_superuser = True
user.is_active    = True
user.set_password(password)
user.save()

# Verify it was saved correctly
user.refresh_from_db()
print(f"==> {'Created' if created else 'Updated'} superuser: {username}")
print(f"==> is_staff     : {user.is_staff}")
print(f"==> is_superuser : {user.is_superuser}")
print(f"==> is_active    : {user.is_active}")
print(f"==> password set : {user.has_usable_password()}")
print(f"==> Login with username='{username}' password='{password}'")
