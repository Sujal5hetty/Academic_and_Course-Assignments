def check_vowel_or_consonant(char):
    vowels='aeiouAEIOU'
    if char.isalpha() and len(char)==1:  
        if char in vowels:
            return f"{char} is a vowel"
        else:
            return f"{char} is a consonant"
    else:
        return "Please enter a single character"

char=input("Enter  a  character: ")

print(check_vowel_or_consonant(char))


#The method char.isalpha() in Python is used to check if a character (or string) consists entirely of alphabetic letters (a-z and A-Z).
#If all the characters in the string are alphabetic, it returns True; otherwise, it returns False.
