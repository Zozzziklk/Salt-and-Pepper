def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

original_text = input("Enter text: ")

ban_list = ('.', '!', '?', '"',' ','-','_',';',':',',')

original_text = original_text.lower()

for i in original_text:
    if i in ban_list:
        original_text = original_text.replace(i, "")
if is_palindrome(original_text):
    print("True")
else:
    print("False")
