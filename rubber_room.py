#ninety nine bottles but its rubber room
import msvcrt
import time

lines = [
    'Crazy?',
    'I was crazy once',
    'They put me in a room',
    'A rubber room',
    'A rubber room with rats',
    'And rats made me crazy'
]

while True:
    for line in lines:
        print(line)
        for _ in range(10):
            time.sleep(0.1)
            if msvcrt.kbhit():
                print("\nAight we dip")
                raise SystemExit


