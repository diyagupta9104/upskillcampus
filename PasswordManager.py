import sqlite3
import os
import random
import string
from cryptography.fernet import Fernet

# --- Encryption Setup ---
key_file = "secret.key"

def load_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    else:
        with open(key_file, "rb") as f:
            key = f.read()
    return Fernet(key)

fernet = load_key()

# --- Database Setup ---
conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY,
    site TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()

# --- Password Generation ---
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# --- Add Password ---
def add_password(site, username, password):
    encrypted = fernet.encrypt(password.encode())
    cursor.execute("INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)",
                   (site, username, encrypted))
    conn.commit()
    print("✅ Password saved successfully.")

# --- Retrieve Passwords ---
def get_password(site):
    cursor.execute("SELECT username, password FROM passwords WHERE site=?", (site,))
    rows = cursor.fetchall()
    if rows:
        for username, enc_password in rows:
            decrypted = fernet.decrypt(enc_password).decode()
            print(f"🔐 Site: {site} | Username: {username} | Password: {decrypted}")
    else:
        print("❌ No entry found.")

# --- Main Menu ---
def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Add new password")
        print("2. Retrieve password")
        print("3. Generate strong password")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            site = input("Enter site name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(site, username, password)

        elif choice == '2':
            site = input("Enter site name to retrieve: ")
            get_password(site)

        elif choice == '3':
            length = int(input("Enter desired password length: "))
            print("Generated password:", generate_password(length))

        elif choice == '4':
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
    conn.close()
