import time
import sys

def countdown(seconds):
    for i in range(seconds, -1, -1):
        sys.stdout.write(f"\r{i:3d}")
        sys.stdout.flush()
        time.sleep(1)
    print("\nDone!")

print('Count to ')
num = input('> ')
countdown(int(num))
