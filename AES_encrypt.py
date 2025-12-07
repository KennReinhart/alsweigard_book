# encrypt.py
import os, base64, sys, hashlib, hmac
import secrets
from getpass import getpass
try:
    import pyperclip
except Exception:
    pyperclip = None

# Optional QR generation
try:
    import qrcode
    QR_AVAILABLE = True
except Exception:
    QR_AVAILABLE = False

from AES_core import aes_encrypt_cbc

# --- Config ---
PBKDF2_ITERS = 150_000  # reasonable default
SALT_LEN = 16
IV_LEN = 16
HMAC_LEN = 32  # SHA256 digest length

def derive_keys(password: str, salt: bytes) -> (bytes, bytes):
    """Derive 32 bytes from password+salt, split into AES key(16) + HMAC key(16)."""
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, PBKDF2_ITERS, dklen=32)
    return dk[:16], dk[16:]

def package_encrypt(plaintext_bytes: bytes, password: str, to_file: str=None, qr_path: str=None):
    salt = secrets.token_bytes(SALT_LEN)
    aes_key, hmac_key = derive_keys(password, salt)
    iv = secrets.token_bytes(IV_LEN)
    ciphertext = aes_encrypt_cbc(aes_key, plaintext_bytes, iv)
    # compute HMAC over (salt || iv || ciphertext)
    mac = hmac.new(hmac_key, salt + iv + ciphertext, hashlib.sha256).digest()
    payload = salt + iv + ciphertext + mac
    b64 = base64.b64encode(payload).decode()

    if to_file:
        with open(to_file, 'w', encoding='utf-8') as f:
            f.write(b64)
        print(f"Encrypted and saved to {to_file}")
    else:
        print("\nEncrypted (base64):\n")
        print(b64)

    if pyperclip and not to_file:
        try:
            pyperclip.copy(b64)
            print("\nCopied to clipboard.")
        except:
            pass

    if qr_path:
        if not QR_AVAILABLE:
            print("qrcode library not installed; cannot generate QR.")
        else:
            img = qrcode.make(b64)
            img.save(qr_path)
            print(f"Saved QR to {qr_path}")

def encrypt_interactive():
    print("=== AES-128-CBC + HMAC Encrypt ===")
    mode = input("Encrypt (T)ext or (F)ile? ").strip().lower()
    if mode.startswith('f'):
        path = input("Path of file to encrypt: ").strip()
        if not os.path.isfile(path):
            print("File not found.")
            return
        with open(path, 'rb') as f:
            data = f.read()
        out = input("Output encrypted file path (leave blank to print base64): ").strip() or None
    else:
        text = input("Message to encrypt:\n> ")
        data = text.encode()
        out = None

    password = getpass("Enter password (will derive key): ")
    confirm = getpass("Confirm password: ")
    if password != confirm:
        print("Passwords do not match.")
        return

    askqr = 'n'
    if QR_AVAILABLE and out is None:
        askqr = input("Generate QR image of ciphertext? (y/N) ").strip().lower()
    qrpath = None
    if askqr.startswith('y'):
        qrpath = input("QR output PNG path (e.g. cipher.png): ").strip()

    package_encrypt(data, password, to_file=out, qr_path=qrpath)

if __name__ == '__main__':
    encrypt_interactive()
