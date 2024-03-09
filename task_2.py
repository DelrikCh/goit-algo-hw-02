from collections import deque


def is_palindrome(s: str) -> bool:
    char_queue = deque()
    for char in s:
        if char != ' ':
            char_queue.append(char.lower())

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True


input_string = input("Input string: ")
if is_palindrome(input_string):
    print("The string is palindrome")
else:
    print("The string is not palindrome")
