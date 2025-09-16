from cs50 import get_string

number = get_string("Number: ") # prompt the user for the card number

valid_lengths = {13, 15, 16} # the valid length of card numbers

length = len(number) # to check the length of the string provided

if length not in valid_lengths: # Quick breakout for invalid numbers
    print("INVALID")

digits = [int(d) for d in number] # cast the individual numbers out of
                                    # the number provided for Luhn's algorithm
total = 0 # to keep track of the total for the algo

for i in range(length - 2, -1, -2): # start at the second last number, iterate over every 2 until 0
    double = digits[i] * 2 # multiply those numbers by two
    if double > 9:
        double = (double % 10) + 1 # to keep track of the runaways
    total = total + double # keep track of the total while adding

for i in range(length - 1, -1, -2): # start at the last number, iterate over every two until 0
    total = total + digits[i] # add the totals

check = total % 10 # check against the algo

if check == 0:
    if length == 15 and number.startswith(("34", "37")):
        print("AMEX")

    elif length == 16 and number.startswith(("51", "52", "53", "54", "55")):
        print("MASTERCARD")

    elif (length == 13 or length == 16) and number.startswith(("4")):
          print("VISA")

    else:
        print("INVALID") # Just incase anything missed passed the Luhn's algo but failed the 3 checks

else:
    print("INVALID") # For everything else





