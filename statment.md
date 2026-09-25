Problem statement
In a globalized environment, individuals often need quick and accurate currency conversion tools. Many existing solutions are web-based, cluttered with ads, or overly complex. There is a need for a straightforward, lightweight command-line utility that provides instant currency conversion using live market rates without unnecessary overhead.
Overview of the project
This project is a lightweight, command-line-based Python application that provides real-time currency conversion. It fetches live exchange rates from the open ExchangeRate-API to deliver accurate and instantaneous conversions between supported global currencies.
Scope of the project
The project covers the development of a Python CLI application that interacts with a public exchange rate API. It includes fetching real-time rates, performing calculations based on user input, and displaying the results. The scope is focused strictly on real-time conversions and excludes offline modes, historical data analysis, and graphical user interfaces (GUIs).
Target users
• Students and Developers: Needing a simple, accessible script for API integration and CLI tool usage.
• Travelers and Freelancers: Requiring a fast terminal-based tool to check up-to-date conversion rates.
• General Users: Anyone needing quick, ad-free currency calculations directly from their command prompt.
High-level features
• Live Data Fetching: Integrates with an external REST API (ExchangeRate-API) to retrieve up-to-date currency values.
• Interactive CLI: Prompts the user for source currency, target currency, and amount in a clear, easy-to-use terminal interface.
• Dynamic Calculation: Instantly computes conversion values using the latest fetched rates.
• Error Handling: Gracefully manages network disconnections, invalid currency code inputs, and negative numerical values.
Technologies/tools used
• Language: Python 3.x
• Libraries: Built-in Python modules (urllib.request, urllib.error, json)
• External API: ExchangeRate-API (https://open.er-api.com)
Steps to install & run the project
1. Ensure Python 3.x is installed on your computer.
2. Save the Python script to a local file (e.g., currency_converter.py).
3. Open your terminal or command prompt.
4. Navigate to the directory where you saved the script.
5. Execute the script by running the command: python currency_converter.py
Instructions for testing
1. Successful Conversion Test: Run the script, input 'USD' as the source currency, 'INR' as the target currency, and '100' for the amount. Verify that the correct converted amount is displayed.
2. Invalid Currency Test: Input a non-existent currency code (e.g., 'XYZ') and verify that the program catches the error and informs you that the currency is not supported.
3. Negative Amount Test: Enter '-50' when prompted for an amount. Ensure the system displays an 'Amount cannot be negative' validation error.
4. Network Error Test: Disconnect your device from the internet and run the script. Verify that the program gracefully displays a 'Network Error' rather than crashing.
