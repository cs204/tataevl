'''Если в шапке вставляю, то повторяет ввод нужной суммы'''
def main():
    amount_due = 50
    pay(amount_due)

def pay(amount_due):
    coins = [50,20,10,5]
    while amount_due > 0:
        print(f"Нужная сумма: {amount_due}")
        coin = int(input("Вставьте монету: ").strip())
        if coin not in coins:
            continue
        else:
            amount_due -= coin
    change_owed = -amount_due
    print(f"Ваша сдача: {change_owed}")



main()