class calculator:
	whileChecker = True
	def multiplication(x,y):
		result = x*y
		print(result)


	while whileChecker == True:
		choice = int(input("1 - addition, 2 - subtraction, 3 - multiplication, 4 - division, 5 - exit "))
		if choice == 1:
			x = int(input("first value: "))
			y = int(input("second value: "))
			addition(x,y)
		elif choice == 2:
			x = int(input("first value: "))
			y = int(input("second value: "))
			subtraction(x,y)
		elif choice == 3:
			x = int(input("first value: "))
			y = int(input("second value: "))
			multiplication(x,y)
		elif choice == 4:
			x = int(input("first value: "))
			y = int(input("second value: "))
			division(x,y)
		elif choice == 5:
			whileChecker = False
		else:
                	print("wrong input")
	