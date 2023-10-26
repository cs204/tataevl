text = input("Приветствие: ")
if text.startswith("Здравствуйте"):
    print("$0")
if text.startswith("з"):
    print("$20")
else:
    print("$100")