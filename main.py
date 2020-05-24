#./data/emigration_statistics_from_sweden.csv
from modules import greet
from modules import source
from modules import country
from modules import sex
from modules import year
from modules import people
from modules import calculation_of_percentage
from modules import validation_file
from modules import check_call_module

greet.show()
data_file = source.load()
validation_file.check_format(data_file)
data = source.open_file(data_file)
check_call_module.check_type(data)
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
check_call_module.check_type(count_people)
result_validation = people.validation(count_people)
people.show_result(result_validation)

#get calculation result
result = calculation_of_percentage.calculation(count_people)
calculation_of_percentage.show_calculation_result(result)
