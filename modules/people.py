import re

def get_count(columns_file, country, year, sex):
    count = {
        "count_all_countries": 0,
        "count_selected_country": 0
    }

    if year == "2018":
        count["count_all_countries"] = columns_file["all_countries_2018"]["column_data"]

        if sex == "0":
            for value in columns_file["total_2018"]["column_data"]:
                if int(country) == columns_file["total_2018"]["column_data"].index(value) + 1:
                    count["count_selected_country"] = value

        if sex == "1":
            for value in columns_file["women_2018"]["column_data"]:
                if int(country) == columns_file["women_2018"]["column_data"].index(value) + 1:
                    count["count_selected_country"] = value

        if sex == "2":
            for value in columns_file["men_2018"]["column_data"]:
                if int(country) == columns_file["men_2018"]["column_data"].index(value) + 1:
                    count["count_selected_country"] = value

    if year == "2017":
        count["count_all_countries"] = columns_file["all_countries_2017"]["column_data"]

        if sex == "0":
            for value in columns_file["total_2017"]["column_data"]:
                if int(country) == columns_file["total_2017"]["column_data"].index(value) + 1:
                    count["count_selected_country"] = value

        if sex == "1":
            for value in columns_file["women_2017"]["column_data"]:
                if int(country) == columns_file["women_2017"]["column_data"].index(value) + 1:
                    count["count_selected_country"] = value

        if sex == "2":
            for value in columns_file["men_2017"]["column_data"]:
                if int(country) == columns_file["men_2017"]["column_data"].index(value) + 1:
                    count["count_selected_country"] = value

    return count

def validation(count):
    valid_count = False
    for _, value in count.items():
        if re.fullmatch(r"\d+", value):
            valid_count = True

    return valid_count

def show_result(result_validation):
    print(result_validation)
    if result_validation == False:
        print("Incorrect data")
        exit()
