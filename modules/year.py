def show_year(columns_file):
    years = []
    for year in columns_file["years"]["column_data"]:
        years.append(year)
        print(year)

    return years


def get_year():
    print("Enter the year by which the calculation will be made:")
    selected_year = str(input())
    return selected_year

def validation(selected_year, years):
    valid_number = False
    for year in years:
        if selected_year == year:
            valid_number = True

    return valid_number

def show_result(result_validation, selected_year):
    if result_validation == True:
        print("You choosed " + selected_year)
    else:
        print("There is no such year in the table")
        exit()
