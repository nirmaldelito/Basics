def calculator(first_number, second_number, fun):
    answer = None
    if fun == "addition":
        answer = first_number + second_number
    elif fun == "subtraction":
        answer = first_number - second_number
    elif fun == "multiplication":
        answer = first_number * second_number
    elif fun == "division":
        answer = first_number / second_number

    return answer


print(calculator(1, 2, 'division'))
