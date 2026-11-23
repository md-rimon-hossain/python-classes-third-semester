# ফাংশন ব্যবহার করে একটি স্ট্রিং Palindrome কিনা যাচাই করার প্রোগ্রাম লেখ।

def is_palindrome(word):
    reverse_word = ""
    
    for char in word:    
        reverse_word = char + reverse_word
   
    if word == reverse_word:
        print(word, "is a palindrome.")
    else:
        print(word, "is not a palindrome.")
        
is_palindrome("madam")