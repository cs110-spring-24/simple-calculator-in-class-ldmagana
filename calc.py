num1 = int(input("enter your first number: "))
op = input("enter your operator: ")
num2 = int(input("enter your second number: "))

if op == "+":
	total = num1 + num2
	print(f"{num1} + {num2} = {total}")
if op == "-":
	total = num1 - num2
	print(f"{num1} - {num2} = {total}")
if op == "*":
	total = num1 * num2
	print(f"{num1} * {num2} = {total}")
if op == "/":
	total = num1 / num2
	print(f"{num1} / {num2} = {total}")
if op == "**":
	total = num1 ** num2
	print(f"{num1} ** {num2} = {total}")
if op == "//":
	total = num1 // num2
	print(f"{num1} // {num2} = {total}")
if op == "%":
	total = num1 % num2
	print(f"{num1} % {num2} = {total}")
if op !="'+','-','*','/','**','//','%'":
	print("you have entered an invalid operator. please choose one of the following: +, -, *, /, **, //, %")
