"""Conversion and Extraction of Data

Module Description
==================
This module contains functions that read .csv files as well as filter
and extract specific columns of data from these data sets.
Note that this module makes use of the Python library, Pandas, to
carry out these functions.

Copyright and Usage Information
===============================

This file is provided solely for the use of TAs and professors
assessing the CSC110 Project at the University of Toronto St. George campus.
All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2020 Divit Singh, Marton Kovacs, Nimit Bhanshali
and Praket Kanaujia.
"""


from typing import Dict
import pandas as pd


def max_temperature_country(filename: str, country: str) -> Dict[int, float]:
    """
    Return a dictionary that states the maximum temperature for each year,
    filtered for the inputted country.

    Preconditions:
        - filename != ''
        - filename refers to a valid csv file with headers
        - country != ''

    >>> temp = max_temperature_country('Temperatures.csv', 'Japan')
    >>> temp[2000] == 89.0
    True
    """
    data = pd.read_csv(filename)
    filter_data = data[(data["Country"] == country)]
    max_temp = filter_data.groupby("Year")["AvgTemperature"].max()

    return max_temp.to_dict()


def stock_close(filename: str) -> Dict[int, float]:
    """
    Return a dictionary that states the stock's mean closing value for each year.

    Preconditions:
        - filename != ''
        - filename refers to a valid csv file with headers

    >>> value = stock_close('Indian Oil.csv')
    >>> value[2000] == 13.596525166666666
    True
    """
    data = pd.read_csv(filename)
    data['Date'] = pd.to_datetime(data['Date'])
    data["Year"] = data["Date"].dt.year
    close = data.groupby("Year")["Close"].mean()

    return close.to_dict()


def fossil_fuel(filename: str, country: str) -> Dict[int, float]:
    """
    Return a dictionary that states the fossil fuel consumption for each year,
    filtered for the inputted country.

    Preconditions:
        - filename != ''
        - filename refers to a valid csv file with headers
        - country != ''

    >>> consumption = fossil_fuel('Fossil Fuel Consumption.csv', 'Japan')
    >>> consumption[2000] == 4961.77
    True
    """
    data = pd.read_csv(filename)
    filter_data = data[(data["Entity"] == country)]
    fuel = filter_data.groupby("Year")["Fossil Fuels (TWh)"].max()
    fuel_round = fuel.round(3)

    return fuel_round.to_dict()


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'typing', 'pandas'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
