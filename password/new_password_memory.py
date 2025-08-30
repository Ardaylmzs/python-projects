# password_manager_secure.py
import os
import json
from cryptography.fernet import Fernet

KEY_FILE = "key.key"
DATA_FILE = "passwords.json"

def ensure_key():
    """Anahtarı yükle ya da oluştur ve dosya izinlerini kısıtla."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        # güvenli olarak yaz (varsa overwrite)
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        try:
            os.chmod(KEY_FILE, 0o600)  # sadece dosya sahibi için okuma/yazma
        except Exception:
            # Windows gibi bazı sistemlerde chmod farklı davranabilir; yinede devam et
            pass
        return key
    else:
        with open(KEY_FILE, "rb") as f:
            return f.read()

def load_data():
    """JSON dosyasından (varsa) veri yükle."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []  # boş liste

def save_data(data):
    """Veriyi JSON dosyasına yaz."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Anahtar ve Fernet objesi
key = ensure_key()
fernet = Fernet(key)

# Başlangıç: var olan veriyi yükle
password_memory = load_data()

def encrypt_text(plain_text: str) -> str:
    token = fernet.encrypt(plain_text.encode())
    return token.decode()  # bytes -> str (utf-8)

def decrypt_text(token_str: str) -> str:
    try:
        plain = fernet.decrypt(token_str.encode())
        return plain.decode()
    except Exception:
        return "[decryption error]"

def save_password():
    user_name = input("Please enter your name: ").strip()
    password_name = input("Please enter your password name: ").strip()
    password_user = input("Please enter the password you want to save: ").strip()

    encrypted = encrypt_text(password_user)

    entry = {
        "username": user_name,
        "password_name": password_name,
        "password_user_encrypted": encrypted
    }
    password_memory.append(entry)
    save_data(password_memory)
    print("Password saved securely!")

def recall_password():
    input_password_name = input("Please enter the password name you want to recall (or press Enter to list all): ").strip()
    if input_password_name == "":
        # tüm kayıtları listele (şifreler çözümlenmiş)
        if not password_memory:
            print("No passwords saved yet.")
            return
        for i, item in enumerate(password_memory, 1):
            try:
                decrypted = decrypt_text(item["password_user_encrypted"])
            except KeyError:
                decrypted = "[invalid entry]"
            print(f"{i}) name: {item['password_name']}  user: {item['username']}  password: {decrypted}")
        return

    # tek bir kayıt arama
    found = False
    for item in password_memory:
        if item["password_name"] == input_password_name:
            decrypted = decrypt_text(item["password_user_encrypted"])
            print(f"Password for '{input_password_name}': {decrypted}")
            found = True
            break

    if not found:
        print("Password not found.")

def delete_password():
    username = input("Enter the username for the password to delete: ").strip()
    password_name = input("Enter the password name to delete: ").strip()

    global password_memory
    initial_len = len(password_memory)

    password_memory = [
        item for item in password_memory
        if not (item["username"] == username and item["password_name"] == password_name)
    ]

    if len(password_memory) == initial_len:
        print("No matching password found.")
    else:
        save_data(password_memory)
        print("Password deleted successfully!")


def main():
    print("Welcome to the secure password memory!")
    while True:
        try:
            choice_user = input("Which function? Recall (1) , Save (2) , Quit (q) or delete (3) for password: ").strip().lower()
            if choice_user in ("1", "recall"):
                recall_password()
            elif choice_user in ("2", "save"):
                save_password()
            elif choice_user in ("q", "quit", "exit"):
                print("Goodbye.")
                break
            elif choice_user in ("3", "delete"):
                delete_password()

            else:
                print("Invalid choice. Type 1, 2 or q.")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            break

if __name__ == "__main__":
    main()
