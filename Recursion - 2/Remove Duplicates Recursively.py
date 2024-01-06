# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    if len(string)<2:
        return string
    # split the string
    first_char=string[0]
    remaining_string=removeConsecutiveDuplicates(string[1:])
    if first_char==remaining_string[0]:
        return remaining_string
    else:
        return first_char+remaining_string


# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
