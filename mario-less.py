from cs50 import get_int
import sys

n = 0

while (n < 1 or n > 8):
    n = get_int("Height: ")

if (n == 1):
    print("#")
    sys.exit()


for i in range(1, n + 1):
    print((" " * (n - i)), end="")
    print("#" * i)
