fruit={
    "Apple":130,
    "Banana":110,
    "Lemon":15,
    "Pear":100,
    "Lime":20,
    "Grapefruit":60,
    "Honeydew Melon":50,
    "Kiwifruit":90,
    "Grapes":90,
    "Strawberry":50,
    "Watermelon":80
}
item=input("item:").title().strip()
for test in fruit:
    if item in test:
        print(f"calories: {fruit[item]}")