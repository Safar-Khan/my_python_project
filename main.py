current_calculations = 24
name_of_calculation = "hours"


def calculations(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * current_calculations} {name_of_calculation}"
    else:
        return "Enter a valid number"


def validate_execute():
    if user_input.isdigit():
        user_num = int(user_input)
        the_ans = calculations(user_num)
        print(the_ans)
    else:
        print("hehe, lol")


user_input = input("Enter some number\n")
validate_execute()


