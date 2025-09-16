from cs50 import get_float


while True:
    n = get_float("Change: ")
    if (n > 0):
        break

counter = 0  # The return value (min number of coins)

n = round(n * 100)  # To change the input from dollars to cents

while (n > 0):
    if (n >= 25):
        quarters = (n // 25)  # truncation to get the number of quaters in the change
        counter += quarters  # increment counter by the quarters
        remainder = n % 25  # modulus to keep track of how many cents are left
        n = remainder  # coz the thing reads from top to bottom

    elif (25 > n >= 10):
        dimes = (n // 10)  # number of dimes
        counter += dimes  # increment counter by the dimes
        remainder = n % 10  # cents left in the change
        n = remainder

    elif (10 > n >= 5):
        nickels = (n // 5)  # number of nickels
        counter += nickels  # increment counter by the nickels
        remainder = n % 5  # cents left in the change
        n = remainder

    else:
        counter += n
        remainder = n % 1
        n = remainder

print(int(counter))
