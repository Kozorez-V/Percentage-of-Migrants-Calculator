# ./data/emigration_statistics_from_sweden.csv
from modules import greet, source, country, sex, year, people, calculation_of_percentage, validation_file

greet.show()
data_file = source.load()
validation_file.check_format(data_file)
data = source.open_file(data_file)
validation_file.check_columns_file(data)

# get number of country and validation
country.show_countries(data)
selected_number_country = country.get_number_country()
result_validation = country.validation(selected_number_country, data)
country.show_result(result_validation, selected_number_country, data)

# get number of sex and validation
selected_number_sex = sex.get_sex()
result_validation = sex.validation(selected_number_sex)
sex.show_result(result_validation, selected_number_sex)

# get number of year and validation
years = year.show_year(data)
selected_year = year.get_year()
result_validation = year.validation(selected_year, years)
year.show_result(result_validation, selected_year)

# get count all countries and selected country
count_people = people.get_count(data, selected_number_country, selected_year, selected_number_sex)

# get calculation result
result = calculation_of_percentage.calculation(count_people)
calculation_of_percentage.show_calculation_result(result)
