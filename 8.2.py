import string


def is_palindrome(text):
    clear_str = ''
    for char in text:
        if char not in string.punctuation + " ":
            clear_str += char.lower()

    if clear_str == clear_str[::-1]:
        print(f"'{text}' is palindrome")
        return True
    else:
        print(f"'{text}' is not palindrome")
        return False


is_palindrome('A man, a plan, a canal: Panama')
is_palindrome('0P')
is_palindrome('a.')
is_palindrome('aurora')
