result = None
operand = None
operator = None
wait_for_number = True


while True:
    while wait_for_number:
        try:
            operand = int(input("введіть число: "))
            break
        except ValueError:
            print("це не ціле число, спробуйте ще раз.")
            operand = int(input("введіть число: "))
    while wait_for_number:
        try:
            operator = input("введіть оператор: ")
        except ValueError:
            print("це не оператор")
        if operator == "+":
            operand += operand 
            break
        elif operator == "-":
            operand -= operand
            break
        elif operator == "*":
            operand *= operand
            break
        elif operator == "/":
            operand /= operand
            break
        elif operator == "=":
            result = operand
            break
        else:
            print("це не оператор")
    if operator == "=":
        print(result)
        break

