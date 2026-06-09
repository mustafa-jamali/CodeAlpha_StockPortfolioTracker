# Stock Portfolio Tracker

## Overview

Stock Portfolio Tracker is a simple Python console application that
allows users to: - Add stocks to a portfolio - Enter the number of
shares owned - Calculate the total portfolio value - View a portfolio
summary - Save the portfolio report to a text file

## Features

-   Predefined stock prices for:
    -   AAPL (Apple)
    -   TSLA (Tesla)
    -   MSFT (Microsoft)
    -   AMZN (Amazon)
    -   GOOG (Google)
-   Input validation for stock names and quantities
-   Automatic portfolio value calculation
-   Generates a portfolio summary
-   Saves results in `portfolio_summary.txt`

## Requirements

-   Python 3.x

## How to Run

1.  Open a terminal.
2.  Navigate to the project folder.
3.  Run the program:

``` bash
python portfolio_tracker.py
```

## Example Usage

``` text
Available Stocks: ['AAPL', 'TSLA', 'MSFT', 'AMZN', 'GOOG']
Write your stock name: AAPL
How many AAPL you have? 5

Available Stocks: ['AAPL', 'TSLA', 'MSFT', 'AMZN', 'GOOG']
Write your stock name: EXIT
```

### Sample Output

``` text
YOUR STOCK PORTFOLIO

- AAPL: 5 Shares x $180 = $900

Total Investment Value: $900
```

## Project Structure

``` text
portfolio_tracker.py      # Main Python program
portfolio_summary.txt     # Generated portfolio report
README.md                 # Project documentation
```

## Future Improvements

-   Real-time stock prices using APIs
-   Portfolio profit/loss tracking
-   Graphical user interface (GUI)
-   Data storage using a database

## Author

Mustafa Jamali
