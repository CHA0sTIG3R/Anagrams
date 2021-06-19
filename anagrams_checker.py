# Anagram Checker

# inputs
text1 = input("Enter First Text: ")
text2 = input("Enter Second Text: ")

# remove spaces and make the characters into lowercase
text1 = text1.lower().replace(" ", "") 
text2 = text2.lower().replace(" ", "")

# initialise the checking variable
check = False

for i in text1: 
    # check if it exists in both inputs
    if i in text2 and i in text1:
        check = True
        # remove the checked characters to make it more precise
        text2 = text2.replace(i,'',1)
        text1 = text1.replace(i,'',1)
    else:
        check = False
        break

if check:
    print("Anagrams")
else:
    print("Not Anagrams")