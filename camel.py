camel=input("camelCase:")
print("snake_case:",end="")
for i in camel:
    if i.islower():
        print(i,end="")
    if i.isupper():
        print("_",i.lower(),end="",sep="")