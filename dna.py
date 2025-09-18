import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv culprit.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as file:
        data = list(csv.DictReader(file))  # make a list of the database and save it in memory

        keys = list(data[0].keys())  # grab all the headers in the database

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file1:
        sequence = file1.read()  # read the contents of the txt file into memory

    # TODO: Find longest match of each STR in DNA sequence
    repeat = {}  # repeat is a dictionary where key = subsequence and value = return of longest_match for that key

    for key in keys[1:]:  # skip the name field when iterating
        # this gives us a dictionary starting at keys[1:n]
        repeat[key] = longest_match(sequence, key)

    # TODO: Check database for matching profiles
    for row in data:  # Grab the individual dictionaries in the database
        # if (repeat) matches the sequence in the database
        if all(int(row[key]) == repeat[key] for key in keys[1:]):
            print(row['name'])  # print the name of the culprit
            return

    print("No match")  # if nothing matches

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
