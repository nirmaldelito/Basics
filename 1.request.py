def calculator(first_number,second_number,function):
    answer = None
    if function == "addition":
        answer = first_number + second_number
    elif function == "subtraction":
        answer = first_number - second_number
    elif function == "multiplication":
        answer = first_number * second_number
    elif function == "division":
        answer = first_number / second_number

    return answer


print(calculator(1, 2, 'division'))
