vowel=["a","u","i","o","e"]
user=input("Input:")
print("Output:",end="")
for i in user:
    if i.casefold() not in vowel:
        print(i,end="")