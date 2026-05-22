import os
import json
import random
import time

SYSTEM_NAME = "oz"

users = {}
current_user = None
currnet_zone = "Lobby"

if os.path.exists("users.json"):
    with open("users.json", "r") as f:
        users = json.load(f)


def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)


def boot_screen():
    print("=" * 40)
    print(f"  {SYSTEM_NAME} SYSTEM INITIALIZED")
    print("=" * 40)
    time.sleep(1)


def register():
    global users

    username = input("NEW USERNAME: ")

    if username in users:
        print("USER ALREADY EXISTS")
        return

    password = input("NEW PASSWAORD: ")

    users[username] = {
        "password": password,
        "avatar": "Default",
        "level": 1,
        "zone": "Lobby",
    }

    save_users()
    print("ACCOUNT CREATED SUCCESSFULLY")


def login():
    global current_user

    username = input("USERNAME: ")
    password = input("PASSWORD: ")

    if username not in users:
        print("INVALID USERNAME")
        return

    if users[username]["password"] != password:
        print("INVALID PASSWORD")
        return

    current_user = username
    print(f"ACCESS GRANTED: {username}")


def logout():
    global current_user

    if current_user is None:
        print("NO ACTIVE USER")
        return

    print(f"{current_user} LOGGED OUT")
    current_user = None


def profile():
    global current_user

    if current_user is None:
        print("LOGIN REQUIRED")
        return

    data = users[current_user]

    print("=" * 30)
    print(f"USER: {current_user}")
    print(f"AVATAR: {data['avatar']}")
    print(f"LEVEL: {data['level']}")
    print(f"ZONE: {data['zone']}")
    print("=" * 30)


def create_avatar():
    global current_user

    if current_user is None:
        print("LOGIN REQUIRED")
        return

    avatar = input("AVATAR NAME: ")

    users[current_user]["avatar"] = avatar
    save_users()
    print(f"AVATAR [{avatar}] CREATED")


zones = {"Neo-Tokyo", "Central City", "Cyber Arena", "Sky Garden", "AI District"}


def world_jump():
    global current_user
    if current_user is None:
        print("LOGIN REQUIRED")
        return

    print("AVAILABLE ZONES:")
    for z in zones:
        print("-", z)

    zone = input("SELECT ZONE: ")

    if zone not in zones:
        print("INVALID ZONE")
        return

    users[current_user]["zone"] = zone
    save_users()

    print(f"MOVING TO [{zone}]...")
    time.sleep(1)


def security_scan():
    print("OZ SECURITY SCAN STARTED")
    time.sleep(1)

    result = random.choice(
        ["SYSTEM SAFE", "LOW RISK DETECTED", "UNKNOWN SIGNAL DETECTED"]
    )
    print(result)


def core_status():
    print("=" * 30)
    print("OZ CORE STATUS")
    print("CPU: STABLE")
    print("NETWORK: ONLINE")
    print("SECURITY: NORMAL")
    print("=" * 30)


def help_menu():
    print("""
AVAILABLE COMMANDS
oz.register
oz.login
oz.logout
oz.profile.status
oz.avatar.create
oz.world.jump
oz.security.scan
oz.core.status
help
exit
""")


boot_screen()
help_menu()

while True:
    command = input("OZ> ")

    if command == "oz.register":
        register()
    elif command == "oz.login":
        login()
    elif command == "oz.logout":
        logout()
    elif command == "oz.profile":
        profile()
    elif command == "oz.avatar.create":
        create_avatar()
    elif command == "oz.world.jump":
        world_jump()
    elif command == "oz.security.scan":
        security_scan()
    elif command == "oz.core.status":
        core_status()
    elif command == "help":
        help_menu()
    elif command == "exit":
        print("EXITING OZ...")
        break
    else:
        print("UNKNOWN COMMAND")
