"""Main

Module Description
==================
This module is the main file of the project. This file executes the complete
analysis on countries and companies based on the input from the user.

Note that this module compiles the conversion and graphing module to present
the complete analysis and presents an appropriate conclusion.

Copyright and Usage Information
===============================

This file is provided solely for the use of TAs and professors
assessing the CSC110 Project at the University of Toronto St. George campus.
All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2020 Divit Singh, Marton Kovacs, Nimit Bhanshali
and Praket Kanaujia.
"""

import conversion
import graphing
import sys


def country_analysis(country: str, start_year: int, end_year: int):
    """
    Create lists of annual highest temperatures and annual fossil fuel consumption for use in graphing.

    Preconditions:
        - 2010 <= start_year <= 2017
        - 2011 <= end_year <= 2018
        - start_year < end_year

    >>> country_analysis('India', 2010, 2018)
    Not Enough Data To Make Conclusion
    """
    temps_dict = conversion.max_temperature_country('Temperatures.csv', country)
    fossil_fuels_dict = conversion.fossil_fuel('Fossil Fuel Consumption.csv', country)
    temps = [temps_dict[x] for x in range(start_year, end_year)]
    fossil_fuel_consumptions = [fossil_fuels_dict[x] for x in range(start_year, end_year)]

    graphing.plot_country_graph(country, temps, fossil_fuel_consumptions, start_year, end_year)
    print(graphing.estimate_country(fossil_fuel_consumptions, temps_dict))


def company_analysis(company: str, country: str, start_year: int, end_year: int):
    """
    Create lists of annual highest temperatures and annual mean stock value for use in graphing.

    Preconditions:
        - 2010 <= start_year <= 2017
        - 2011 <= end_year <= 2018
        - start_year < end_year

    >>> company_analysis('Tokyo Gas', 'Japan', 2010, 2018)
    Green Company
    """
    temps_dict = conversion.max_temperature_country('Temperatures.csv', country)
    indices_dict = conversion.stock_close(company + '.csv')
    fossil_fuels_dict = conversion.fossil_fuel('Fossil Fuel Consumption.csv', country)
    temps = [temps_dict[x] for x in range(start_year, end_year + 1)]
    indices = [indices_dict[x] for x in range(start_year, end_year + 1)]
    fossil_fuel_consumptions = [fossil_fuels_dict[x] for x in range(start_year, end_year + 1)]

    print(graphing.estimate_company(indices, fossil_fuel_consumptions))
    graphing.plot_company_graph(company, temps, indices, start_year, end_year)


###############################################################################
# User Interface
###############################################################################

print("Welcome to the Climate Change Graph Analyser!")
print("In order to undertake an analysis, you can make use of two functions:")
print("1) 'country_analysis' in order to analyse a given country.")
print("2) 'company_analysis' in order to analyse a given company.")

country = input('Please select a country from the following countries: Japan, India')

if country != 'Japan' and country != 'India':
    print('Invalid Input, restart program')
    sys.exit()

elif country == 'India':
    company = input('Please select a company: Tata Chemicals, Hindustan Unilever, Indian Oil')

    if company != 'Tata Chemicals' and company != 'Hindustan Unilever' and company != 'Indian Oil':
        print('Invalid Input, restart program')
        sys.exit()

else:
    company = input('Please select a company: Mitsubishi, Tokyo Gas, TEPCO')

    if company != 'RICOH' and company != 'Tokyo Gas' and company != 'TEPCO':
        print('Invalid Input, restart program')
        sys.exit()

start_year = int(input("Please select a start year between 2010 and 2017"))

end_year = int(input("Please select an end year between 2011 and 2018 that is greater than your start year"))

if end_year <= start_year:
    print('Invalid Input, restart program')
    sys.exit()

analysis_type = input('What type of analysis do you wish to conduct? Country Analysis or Company Analysis?')

if analysis_type == 'Country Analysis':
    country_analysis(country, start_year, end_year)

elif analysis_type == 'Company Analysis':
    company_analysis(company, country, start_year, end_year)

else:
    print('Invalid Input, restart program')
    sys.exit()
