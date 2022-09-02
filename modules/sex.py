def get_sex():
    print("Choose the sex by which the calculation will be made:\n"
          "0 — Both sexes\n"
          "1 — Woman\n"
          "2 — Male")
    selected_sex = str(input())
    return selected_sex


def validation(selected_sex):
    valid_number = False
    if selected_sex == "0" or selected_sex == "1" or selected_sex == "2":
        valid_number = True

    return valid_number


def show_result(result_validation, selected_sex):
    if result_validation == True:
        print(f'You choosed {selected_sex}')
    else:
        print("This choise doesn't exist")
        exit()
