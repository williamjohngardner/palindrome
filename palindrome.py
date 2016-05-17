# Bill Gardner
# 5/16/16
# Palindrome Finder

word = input("Enter your word to see if it's a palindrome: ").lower()

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", " "]
for i in punctuation:
    word = word.replace(i, "")

a = word[0]
b = word[-1]
count1 = 0
count2 = -1
s = len(word)

for letter in word:
    if a == b:
        count1 += 1
        count2 -= 1
        if count1 == s:
            print("This is a Panlidrome")
            break
        a = word[count1]
        b = word[count2]
    else:
        print("This is not a palindrome.")
        break
