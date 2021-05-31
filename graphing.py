"""Graphing Data

Module Description
==================
This module contains functions that takes in the dictionaries that were
extracted and converted in the conversion module and plots graphs
using that data.

This module also contains function that analyze and estimate the trends
of the plotted graphs and return an appropriate conclusion.

Copyright and Usage Information
===============================

This file is provided solely for the use of TAs and professors
assessing the CSC110 Project at the University of Toronto St. George campus.
All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2020 Divit Singh, Marton Kovacs, Nimit Bhanshali
and Praket Kanaujia.
"""

from typing import Dict, List
import plotly.graph_objects as go
from plotly.subplots import make_subplots


###############################################################################
# Plotting Graphs
###############################################################################
def plot_country_graph(country: str, temps: List[float], fossil_fuel_consumptions: List[float],
                       start_year: int, end_year: int) -> None:
    """
    Plot a graph of Annual Highest Temperature (temps) on the x-axis against Fossil Fuel
    Expenditure (expenditures) on the y-axis for the given country.

    Preconditions:
        - country != ''
        - temps != []
        - fossil_fuel_consumptions != []
        - 2010 <= start_year <= 2017
        - 2011 <= end_year <= 2018
        - start_year < end_year
    """
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=list(range(start_year, end_year)), y=fossil_fuel_consumptions,
                   name="Fossil Fuel Consumption (TWh)"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=list(range(start_year, end_year)), y=temps,
                   name="Annual Highest Temperature (°F)"),
        secondary_y=True,
    )

    fig.update_layout(
        title_text=country + " (" + str(start_year) + " - " + str(end_year) + ")"
    )
    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="Fossil Fuel Consumption (TWh)", secondary_y=False)
    fig.update_yaxes(title_text="Annual Highest Temperature (°F)", secondary_y=True)

    fig.show()


def plot_company_graph(company: str, temps: List[float], indices: List[float],
                       start_year: int, end_year: int) -> None:
    """
    Plot a graph of Annual Highest Temperature (temps) on the x-axis against Stock
    Index Value (indices) on the y-axis for the given company.

    Preconditions:
        - company != ''
        - temps != []
        - indices != []
        - 2010 <= start_year <= 2017
        - 2011 <= end_year <= 2018
        - start_year < end_year
    """
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=list(range(start_year, end_year)), y=indices,
                   name="Stock Index Value ($)"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=list(range(start_year, end_year)), y=temps,
                   name="Annual Highest Temperature (°F)"),
        secondary_y=True,
    )

    fig.update_layout(
        title_text=company + " (" + str(start_year) + " - " + str(end_year) + ")"
    )
    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="Stock Index Value ($)", secondary_y=False)
    fig.update_yaxes(title_text="Annual Highest Temperature (°F)", secondary_y=True)

    fig.show()


###############################################################################
# Estimate Graph Trends
###############################################################################
def estimate_country(fossil_fuel_consumptions: List[float], temps_dict: Dict[int, float]) -> str:
    """
    Return a string describing the nature of the graph of fuel consumption vs the graph of
    annual highest temperature.

    The function returns:
        -'High Stake' if more than 70% of the graph is increasing
        -'Not Enough Data To Make Conclusion' if the function is neither mainly increasing
        nor mainly decreasing
        -'Low Stake' otherwise

    Preconditions:
        - fossil_fuel_consumption != []
        - temps_dict != {}

    >>> consumption = [6000, 7000, 8000, 10000, 6000, 6000, 5000]
    >>> temperature = {2000: 91, 2001: 92, 2002: 94, 2003: 95, 2004: 100, 2005: 104, 2006: 109}
    >>> estimate_country(consumption, temperature)
    'Not Enough Data To Make Conclusion'

    >>> consumption = [6000, 7000, 8000, 10000, 11000, 11000, 5000, 7000]
    >>> estimate_country(consumption, temperature)
    'High Stake'

    >>> consumption = [16000, 17000, 15000, 10000, 9000, 8000, 7000, 6000]
    >>> estimate_country(consumption, temperature)
    'Low Stake'
    """
    highest_temp = [temps_dict[year] for year in temps_dict]

    if check_gradient(highest_temp) == 'Increasing':
        if check_gradient(fossil_fuel_consumptions) == 'Increasing':
            return 'High Stake'
        elif check_gradient(fossil_fuel_consumptions) == 'Decreasing':
            return 'Low Stake'
        else:
            return 'Not Enough Data To Make Conclusion'
    elif check_gradient(highest_temp) == 'Decreasing':
        if check_gradient(fossil_fuel_consumptions) == 'Increasing':
            return 'Low Stake'
        elif check_gradient(fossil_fuel_consumptions) == 'Decreasing':
            return 'High Stake'
        else:
            return 'Not Enough Data To Make Conclusion'
    else:
        return 'Not Enough Data To Make Conclusion'


def estimate_company(indices: List[float], fossil_fuel_consumptions: List[float]) -> str:
    """
    Return a string describing the nature of a graph.

    The function returns:
        Assuming the corresponding country is a high stake country the function returns:
            -'Red Company' if more than 70% of the graph is increasing
            -'Green Company' if more than 70% of the graph is decreasing
            -'White company' otherwise

        Assuming the corresponding country is a low stake country the function returns:
            -'Red Company' if more than 70% of the graph is increasing
            -'Green Company' if more than 70% of the graph is decreasing
            -'White Company' otherwise

        Assuming the corresponding country does not have enoug data the function returns:
            -'Not Enough Cumulative Data To Compute Company Nature'

    Preconditions:
        - indices != []
        - fossil_fuel_consumption != []

    >>> consumption = [6000, 7000, 8000, 10000, 6000, 6000, 5000]
    >>> stock = [15.1, 15.8, 16.2, 17.5, 15.2, 18.5]
    >>> estimate_company(stock, consumption)
    'Not Enough Cumulative Data To Compute Company Nature'

    >>> consumption = [6000, 7000, 8000, 10000, 11000, 11000, 5000, 7000]
    >>> stock = [15.1, 15.8, 16.2, 17.5, 15.2, 18.5]
    >>> estimate_company(stock, consumption)
    'Red Company'

    >>> consumption = [16000, 17000, 15000, 10000, 9000, 8000, 7000, 6000]
    >>> stock = [15.1, 15.8, 16.2, 17.5, 15.2, 18.5]
    >>> estimate_company(stock, consumption)
    'Green Company'
    """
    if check_gradient(fossil_fuel_consumptions) == 'Increasing':
        if check_gradient(indices) == 'Increasing':
            return 'Red Company'
        elif check_gradient(indices) == 'Decreasing':
            return 'Green Company'
        else:
            return 'White company'
    elif check_gradient(fossil_fuel_consumptions) == 'Decreasing':
        if check_gradient(indices) == 'Increasing':
            return 'Green Company'
        elif check_gradient(indices) == 'Decreasing':
            return 'Red Company'
        else:
            return 'White company'
    else:
        return 'Not Enough Cumulative Data To Compute Company Nature'


def check_gradient(y_axis: List[float]) -> str:
    """
    Calculate the whether a graph is increasing, decreasing or fluctuating

    The function returns:
        -'Increasing' if the function is mainly increasing
        -'Decreasing' if the function is mainly decreasing
        -'Fluctuating' if the graph is neither increasing or decreasing

    Precondition:
        - y_axis != []
    """
    positive_grad = 0
    flat_grad = 0
    negative_grad = 0

    for index in range(1, len(y_axis)):
        if y_axis[index] > y_axis[index - 1]:
            positive_grad += 1
        elif y_axis[index] < y_axis[index - 1]:
            negative_grad += 1
        else:
            flat_grad += 1

    if positive_grad >= 0.7 * (positive_grad + flat_grad + negative_grad):
        return 'Increasing'
    elif positive_grad > 0.3 * (positive_grad + flat_grad + negative_grad):
        return 'Fluctuating'
    else:
        return 'Decreasing'


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'typing', 'plotly.graph_objects',
                          'plotly.subplots'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
