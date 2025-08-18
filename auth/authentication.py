import json
import os
import hashlib

USERS_FILE = "auth/users.json"

def get_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    users = get_users()
    if username in users:
        return False, "❌ Username already exists"
    users[username] = hash_password(password)
    save_users(users)
    return True, "✅ Registration successful!"

def login_user(username, password):
    users = get_users()
    if username in users and users[username] == hash_password(password):
        return True
    return False
