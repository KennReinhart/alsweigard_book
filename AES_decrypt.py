# decrypt.py
import os, base64, sys, hashlib, hmac
from getpass import getpass
try:
    import pyperclip
except Exception:
    pyperclip = None

from AES_core import aes_decrypt_cbc

SALT_LEN = 16
IV_LEN = 16
HMAC_LEN = 32
PBKDF2_ITERS = 150_000

def derive_keys(password: str, salt: bytes):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, PBKDF2_ITERS, dklen=32)
    return dk[:16], dk[16:]

def package_decrypt(b64_payload: str, password: str, out_file: str=None):
    try:
        raw = base64.b64decode(b64_payload)
    except Exception:
        raise ValueError("Input is not valid base64.")

    if len(raw) < (SALT_LEN + IV_LEN + HMAC_LEN + 1):
        raise ValueError("Payload too short or corrupted.")

    salt = raw[:SALT_LEN]
    iv = raw[SALT_LEN:SALT_LEN+IV_LEN]
    mac = raw[-HMAC_LEN:]
    ciphertext = raw[SALT_LEN+IV_LEN:-HMAC_LEN]

    aes_key, hmac_key = derive_keys(password, salt)
    # Verify HMAC
    expected_mac = hmac.new(hmac_key, salt + iv + ciphertext, hashlib.sha256).digest()
    if not hmac.compare_digest(mac, expected_mac):
        raise ValueError("HMAC verification failed. Wrong password or tampered ciphertext.")

    plaintext = aes_decrypt_cbc(aes_key, ciphertext, iv)
    if out_file:
        with open(out_file, 'wb') as f:
            f.write(plaintext)
        print(f"Decrypted data written to {out_file}")
    else:
        text = plaintext.decode(errors='replace')
        print("\nDecrypted text:\n")
        print(text)
        if pyperclip:
            try:
                pyperclip.copy(text)
                print("\nCopied to clipboard.")
            except:
                pass

def decrypt_interactive():
    print("=== AES-128-CBC + HMAC Decrypt ===")
    mode = input("Decrypt from (F)ile or (P)aste base64? ").strip().lower()
    if mode.startswith('f'):
        path = input("Path to base64-encrypted file: ").strip()
        if not os.path.isfile(path):
            print("File not found.")
            return
        with open(path, 'r', encoding='utf-8') as f:
            b64 = f.read().strip()
        out = input("Output path for decrypted file (leave blank to print text): ").strip() or None
    else:
        b64 = input("Paste base64 ciphertext:\n> ").strip()
        out = None

    password = getpass("Enter password used to encrypt: ")
    try:
        package_decrypt(b64, password, out_file=out)
    except Exception as e:
        print("Decryption failed:", e)

if __name__ == '__main__':
    decrypt_interactive()
