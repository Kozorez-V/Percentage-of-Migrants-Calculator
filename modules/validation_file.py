import re

def check_format(data_file):
    if data_file.endswith(".csv"):
        return True
    else:
        print("Invalid file format")
        exit()

def check_columns_file(columns_file):

    error_messages = []

    for _, column in columns_file.items():
        for value in column["column_data"]:
            if not re.fullmatch(column["check_type"], value, re.IGNORECASE):
                message = "Incorrect data in " + str(column["position"]) + " column: " + value
                error_messages.append(message)

    if len(error_messages) > 0:
        print("The file contains incorrect data\n")
        for message in error_messages:
            print(message)
            exit()
