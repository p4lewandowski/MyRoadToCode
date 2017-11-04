def reverse(text):
    text = erease_all(text)
    print(text)
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


def erease_all(text):
    text = text.replace(" ","")
    text = text.replace(",", "")
    return text

something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")


