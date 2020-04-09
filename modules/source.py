import os.path
import csv

def load():
    print("At first, enter the path to the file:")
    filename = str(input())
    if os.path.exists(filename) != True:
            print("There is no such file or directory")
            return exit()
    return filename
    # return "./data/emigration_statistics_from_sweden.csv"

def open_file(data_file):
    columns_file = {
        "years": {
            "column_data": [],
            "first_year_position": 2,
            "second_year_position": 5,
            "check": r"\d+"
        },

        "all_countries_2018": {
            "column_data": 0,
            "position": 2,
            "check": r"\d+"
        },

        "all_countries_2017": {
            "column_data": 0,
            "position": 5,
            "check": r"\d+"
        },

        "number_country": {
            "column_data": [],
            "position": 0,
            "check": r"\d+"
        },

        "countries": {
            "column_data": [],
            "position": 1,
            "check": r"[a-z, \s]+"
        },

        "total_2018": {
            "column_data": [],
            "position": 2,
            "check": r"\d+"
            },

        "women_2018": {
            "column_data": [],
            "position": 3,
            "check": r"\d+"
        },

        "men_2018": {
            "column_data": [],
            "position": 4,
            "check": r"\d+"
        },

        "total_2017": {
            "column_data": [],
            "position": 5,
            "check": r"\d+"
        },

        "women_2017": {
            "column_data": [],
            "position": 6,
            "check": r"\d+"
        },

        "men_2017": {
            "column_data": [],
            "position": 7,
            "check": r"\d+"
        }
    }

    with open(data_file, newline ="") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if row[1] == "All countries":
                columns_file["all_countries_2017"]["column_data"] = row[columns_file["all_countries_2017"]["position"]]
                columns_file["all_countries_2018"]["column_data"] = row[columns_file["all_countries_2018"]["position"]]

            if row[3] == "":
                columns_file["years"]["column_data"].append(row[columns_file["years"]["first_year_position"]])
                columns_file["years"]["column_data"].append(row[columns_file["years"]["second_year_position"]])

            if row[0] != "":
                columns_file["number_country"]["column_data"].append(row[columns_file["number_country"]["position"]])
                columns_file["countries"]["column_data"].append(row[columns_file["countries"]["position"]])
                columns_file["total_2018"]["column_data"].append(row[columns_file["total_2018"]["position"]])
                columns_file["women_2018"]["column_data"].append(row[columns_file["women_2018"]["position"]])
                columns_file["men_2018"]["column_data"].append(row[columns_file["men_2018"]["position"]])
                columns_file["total_2017"]["column_data"].append(row[columns_file["total_2017"]["position"]])
                columns_file["women_2017"]["column_data"].append(row[columns_file["women_2017"]["position"]])
                columns_file["men_2017"]["column_data"].append(row[columns_file["men_2017"]["position"]])

    return columns_file
