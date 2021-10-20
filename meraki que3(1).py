# print("welcome to ATM")
# print("insert your card")
# language=(input("enter a language"))
# if language=="english":
# 	print("thank you for english language")
# elif language=="hindi":
# 	print("thank you for hindi language")
# else:
# 	print("any language")
# account=(input("enter your account"))
# if account=="saving account":
# 	print("thank you")
# else:
# 	print("corrent account")
# banking=(input("chhose your option"))
# amount=int(input("enter your amount"))
# pin=int(input("enter your pin"))
# if banking=="withdraw":
# 	if amount>=10 and amount<=10000:
# 			if pin==9516:
# 				print("your withdraw is succesfully")
# elif banking=="deposit money":
# 	if amount==5000:
# 		if pin==9516:
# 			print("thank you for deposit money")


def students(*names):
    print(names)
students(["sunita","sapna","geetu","shalini"])