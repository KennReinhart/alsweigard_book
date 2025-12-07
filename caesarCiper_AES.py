# AES-128 Pure Python Implementation (ECB Mode)
# Works on Python 3.13 with NO external libraries
# Author: ChatGPT (2025)

import itertools
try:
    import pyperclip
except ImportError:
    pass
# ----------------------
# AES CONSTANTS
# ----------------------

S_BOX = [
    99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118,
    202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192,
    183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21,
    4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117,
    9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132,
    83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207,
    208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168,
    81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210,
    205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115,
    96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219,
    224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121,
    231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8,
    186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138,
    112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158,
    225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223,
    140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22
]

INV_S_BOX = [
    82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251,
    124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203,
    84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78,
    8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37,
    114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146,
    108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132,
    144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6,
    208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107,
    58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115,
    150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110,
    71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27,
    252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244,
    31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95,
    96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239,
    160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97,
    23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125
]

RCON = [
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36
]


# ----------------------
# AES HELPERS
# ----------------------

def sub_bytes(state):
    return [S_BOX[b] for b in state]


def inv_sub_bytes(state):
    return [INV_S_BOX[b] for b in state]


def shift_rows(state):
    return [
        state[0], state[5], state[10], state[15],
        state[4], state[9], state[14], state[3],
        state[8], state[13], state[2], state[7],
        state[12], state[1], state[6], state[11]
    ]


def inv_shift_rows(state):
    return [
        state[0], state[13], state[10], state[7],
        state[4], state[1], state[14], state[11],
        state[8], state[5], state[2], state[15],
        state[12], state[9], state[6], state[3]
    ]

def xtime(a):
    return ((a << 1) ^ 0x1B) & 0xFF if a & 0x80 else (a << 1)

def mix_columns(state):
    result = []
    for i in range(0, 16, 4):
        a = state[i:i + 4]
        result.extend([
            xtime(a[0]) ^ xtime(a[1]) ^ a[1] ^ a[2] ^ a[3],
            a[0] ^ xtime(a[1]) ^ xtime(a[2]) ^ a[2] ^ a[3],
            a[0] ^ a[1] ^ xtime(a[2]) ^ xtime(a[3]) ^ a[3],
            xtime(a[0]) ^ a[0] ^ a[1] ^ a[2] ^ xtime(a[3])
        ])
    return result

def inv_mix_columns(state):
    result = []
    for i in range(0, 16, 4):
        a = state[i:i + 4]
        result.extend([
            mul(0x0E, a[0]) ^ mul(0x0B, a[1]) ^ mul(0x0D, a[2]) ^ mul(0x09, a[3]),
            mul(0x09, a[0]) ^ mul(0x0E, a[1]) ^ mul(0x0B, a[2]) ^ mul(0x0D, a[3]),
            mul(0x0D, a[0]) ^ mul(0x09, a[1]) ^ mul(0x0E, a[2]) ^ mul(0x0B, a[3]),
            mul(0x0B, a[0]) ^ mul(0x0D, a[1]) ^ mul(0x09, a[2]) ^ mul(0x0E, a[3]),
        ])
    return result

def mul(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi:
            a ^= 0x1B
        b >>= 1
    return p

# ----------------------
# KEY EXPANSION
# ----------------------

def rotate(word):
    return word[1:] + word[:1]

def key_expansion(key):
    key_symbols = list(key)
    if len(key_symbols) != 16:
        raise ValueError("AES-128 key must be 16 bytes")

    expanded = key_symbols.copy()

    for i in range(4, 44):
        temp = expanded[(i - 1) * 4:i * 4]
        if i % 4 == 0:
            temp = sub_bytes(rotate(temp))
            temp[0] ^= RCON[i // 4]
        for j in range(4):
            temp[j] ^= expanded[(i - 4) * 4 + j]
        expanded.extend(temp)
    return expanded

# ----------------------
# BLOCK ENCRYPTION
# ----------------------

def encrypt_block(block, expanded_key):
    state = list(block)

    state = add_round_key(state, expanded_key[:16])

    for r in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, expanded_key[r * 16:(r + 1) * 16])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, expanded_key[160:176])

    return state

def decrypt_block(block, expanded_key):
    state = list(block)

    state = add_round_key(state, expanded_key[160:176])

    for r in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, expanded_key[r * 16:(r + 1) * 16])
        state = inv_mix_columns(state)

    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, expanded_key[:16])

    return state

def add_round_key(state, round_key):
    return [s ^ k for s, k in zip(state, round_key)]

# ----------------------
# PADDING
# ----------------------

def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# ----------------------
# USER-FRIENDLY API
# ----------------------

def aes_encrypt(key: bytes, plaintext: str) -> bytes:
    expanded = key_expansion(key)
    data = pad(plaintext.encode())
    blocks = [data[i:i + 16] for i in range(0, len(data), 16)]
    encrypted = []

    for b in blocks:
        encrypted.extend(encrypt_block(list(b), expanded))

    return bytes(encrypted)

def aes_decrypt(key: bytes, ciphertext: bytes) -> str:
    expanded = key_expansion(key)
    blocks = [ciphertext[i:i + 16] for i in range(0, len(ciphertext), 16)]
    decrypted = []

    for b in blocks:
        decrypted.extend(decrypt_block(list(b), expanded))

    return unpad(bytes(decrypted)).decode()

# Main
def main():
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    while True:
        mode = input("> ").lower()
        if mode in ("e", "d"):
            break
        print("Please enter 'e' or 'd' only.")

    mode_text = "encrypt" if mode == "e" else "decrypt"

    # Key input (must be 16 bytes)
    while True:
        print(f"Enter 16-character AES key to {mode_text}:")
        key = input("> ")
        if len(key) == 16:
            key_bytes = key.encode()
            break
        print("Key MUST be exactly 16 characters!")

    # Message input
    print(f"Enter message to {mode_text}:")
    user_input = input("> ")

    # Process based on mode
    if mode == "e":
        result_bytes = aes_encrypt(key_bytes, user_input)
        result = result_bytes.hex()
        print("\nEncrypted (HEX):")
        print(result)

    elif mode == "d":
        try:
            ciphertext = bytes.fromhex(user_input.strip())
            result = aes_decrypt(key_bytes, ciphertext)
            print("\nDecrypted:")
            print(result)

        except ValueError:
            print("ERROR: Ciphertext must be valid HEX.")
            exit()

    # Copy to clipboard if possible
    if pyperclip:
        try:
            pyperclip.copy(result)
            print("\nResult copied to clipboard!")
        except:
            pass

    print("\nDone.")

if __name__ == "__main__":
    main()