# CodXo_2
# Currency Converter Application

## Overview

The Currency Converter is a Python-based GUI application that allows users to convert amounts between different currencies. Utilizing the `tkinter` library for the graphical interface and `requests` for fetching live exchange rates, the application provides an intuitive way to handle currency conversions. The dropdown menus include all global currencies with their full names, and a dynamic search feature helps users quickly find their desired currency.

## Features

- **Real-time Currency Conversion**: Fetches live exchange rates from a reliable API and performs conversions based on the current rates.
- **Searchable Dropdown Menus**: Allows users to search and select currencies from a dropdown list with real-time filtering.
- **User-Friendly Interface**: Built with `tkinter`, the interface is clean and easy to use.
- **Error Handling**: Provides error messages for invalid inputs or API issues.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- `requests` library
- `tkinter` (usually comes pre-installed with Python)

To install the `requests` library, use pip:

```bash
pip install requests
```

## API Key

The application uses the ExchangeRate-API for fetching currency data. You need to replace the `API_KEY` with your own key, which you can obtain by signing up at [ExchangeRate-API](https://www.exchangerate-api.com/).

```python
API_KEY = 'YOUR_API_KEY_HERE'
```

## Usage

1. **Run the Application**: Execute the script to open the currency converter GUI.

   ```bash
   python Codxo2.py
   ```

2. **Input Amount**: Enter the amount you wish to convert.

3. **Select Currencies**: Use the search boxes to select the source and target currencies from the dropdown menus.

4. **Convert**: Click the "Convert" button to see the conversion result.

5. **View Results**: The result will be displayed below the button showing the converted amount.

## Code Explanation

- **Data Fetching**: The `get_exchange_rates` function fetches currency conversion rates from the API.
- **Conversion Logic**: The `convert_currency` function performs the conversion based on the fetched rates.
- **UI Components**: The `tkinter` GUI includes input fields, comboboxes with search functionality, and a result label.

## Code

Here is the main part of the script:

```python
import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_KEY = 'YOUR_API_KEY_HERE'
BASE_URL = 'https://v6.exchangerate-api.com/v6/'

currency_names = {
    # (Currency data as provided)
}

def get_exchange_rates(base_currency):
    """Fetch exchange rates and currency list from the API."""
    url = f"{BASE_URL}{API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or data.get('result') != 'success':
        raise Exception(f"Error fetching data: {data.get('error-type')}")
    return data['conversion_rates'], data['conversion_rates'].keys()

def convert_currency(amount, from_currency, to_currency):
    """Convert amount from one currency to another using the API."""
    rates, _ = get_exchange_rates(from_currency)
    if to_currency not in rates:
        raise ValueError(f"Conversion rate from {from_currency} to {to_currency} is not available.")
    
    rate = rates[to_currency]
    return amount * rate

# (Rest of the script for UI creation and event handling)
```
