from cs50 import get_string

text = get_string("Text: ")

def main():
    L = letters(text)

    W = words(text)

    S = sentences(text)

    C = float(CLI(L, W, S))

    C = int(C + 0.5)

    if C >= 16:
        print("Grade 16+")

    elif C < 1:
        print("Before Grade 1")

    else:
        print(f"Grade {C}")


def letters(text):
    total = 0

    for i in text:
        if (("a" <= i <= "z") or ("A" <= i <= "Z")):
            total += 1

    return total


def words(text):
    total = 1 # There must be some text to evaluate (get_string)

    for i in text:
        if (i == (" ")):
            total += 1

    return total


def sentences(text):
    total = 0

    for i in text:
        if (i == ".") or (i == "?") or (i == "!"):
            total += 1

    return total


def CLI(letters, words, sentences):
    L = float(letters/words) * 100
    S = float(sentences/words) * 100

    C = (0.0588 * L) - (0.296 * S) - 15.8

    return C

main()
