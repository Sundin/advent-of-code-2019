
def split_into_digits(number):
    digits = []
    while number:
        digit = number % 10
        digits.append(digit)
        # remove last digit from number (as integer):
        number //= 10
    digits.reverse()
    return digits


def is_matching(digits):
    found_twins = False
    for d in range(1, 6):
        if digits[d] < digits[d-1]:
            return False

        if digits[d] == digits[d-1]:
            found_twins = True

    return found_twins


def is_matching_number(number):
    digits = split_into_digits(number)
    return is_matching(digits)


# not used
def get_number_of_passwords(start, stop):
    digits = split_into_digits(start)
    for d in reversed(range(1, 6)):
        if (d == 0):
            print("0")
        elif(digits[d] < digits[d-1]):
            digits[d] = digits[d-1]
        else:
            print("?")
    return 0


def main():
    start = 172851
    stop = 675869
    matching_passwords = 0
    for number in range(start, stop+1):
        if (is_matching_number(number)):
            matching_passwords += 1

    print("Number of potential passwords:", matching_passwords)


main()
