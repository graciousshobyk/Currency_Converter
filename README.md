Overview of the project
This project is a lightweight, command-line-based Python application that provides real-time currency conversion. It fetches live exchange rates from the open ExchangeRate-API to deliver accurate and instantaneous conversions between supported global currencies.
Features
• Real-time currency conversion using live API data.
• Support for numerous global currencies.
• Simple and intuitive interactive command-line interface.
• Robust error handling for network connectivity issues, negative amounts, and unsupported currency codes.
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
