result = None
operand = 0
operator = None
wait_for_number = True


while True:
    while wait_for_number:
        try:
            num = int(input("введіть число: "))
            break
        except ValueError:
            print("це не ціле число, спробуйте ще раз.")
            num = int(input("введіть число: "))
    while wait_for_number:
        try:
            operator = input("введіть оператор: ")
        except ValueError:
            print("це не оператор")
        if operator == "+":
            operand += num 
            break
        elif operator == "-":
            operand -= num
            break
        elif operator == "*":
            operand *= num
            break
        elif operator == "/":
            operand /= num
            break
        elif operator == "=":
            result = operand
            break
        else:
            print("це не оператор")
    if operator == "=":
        print(result)
        break


