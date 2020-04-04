def show_countries(columns_file):
    for number, country in zip(columns_file["number_country"]["column_data"],
                               columns_file["countries"]["column_data"]):
        print(number, "—", country)

def get_number_country():
    print("Here is a numbered list of countries. You need to choose the percentage"
          " of natives which one you want to calculate. To do this, enter the number of the selected country.")
    selected_number = str(input())
    return selected_number

def validation(selected_number, columns_file):
    numbers_country = columns_file["number_country"]["column_data"]
    valid_number = False
    for element in numbers_country:
        if selected_number == element:
            valid_number = True

    return valid_number

def show_result(result_validation, selected_number, columns_file):
    if result_validation == True:
        for value in columns_file["countries"]["column_data"]:
            if int(selected_number) == columns_file["countries"]["column_data"].index(value) + 1:
                print("You choosed " + value)
    else:
        print("This number isn't on the list")
        exit()
