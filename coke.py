coin=50
cent=[25,10,5]
total_paid=0
while coin > 0:
    print(f"amount Due: {coin}")
    user=int(input("insert coin:"))
    if user in cent:
        coin = coin - user
        total_paid = total_paid + user
if total_paid >= coin:
    print(f"change owed: {total_paid - 50}")