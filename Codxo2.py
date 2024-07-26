import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_KEY = '2722677886e3a4c684b35a8e'
BASE_URL = 'https://v6.exchangerate-api.com/v6/'

currency_names = {
    'AED': 'United Arab Emirates Dirham',
    'AFN': 'Afghan Afghani',
    'ALL': 'Albanian Lek',
    'AMD': 'Armenian Dram',
    'ANG': 'Netherlands Antillean Guilder',
    'AOA': 'Angolan Kwanza',
    'ARS': 'Argentine Peso',
    'AUD': 'Australian Dollar',
    'AWG': 'Aruban Florin',
    'AZN': 'Azerbaijani Manat',
    'BAM': 'Bosnia and Herzegovina Convertible Mark',
    'BBD': 'Barbadian Dollar',
    'BDT': 'Bangladeshi Taka',
    'BGN': 'Bulgarian Lev',
    'BHD': 'Bahraini Dinar',
    'BIF': 'Burundian Franc',
    'BMD': 'Bermudian Dollar',
    'BND': 'Brunei Dollar',
    'BOB': 'Bolivian Boliviano',
    'BRL': 'Brazilian Real',
    'BSD': 'Bahamian Dollar',
    'BTN': 'Bhutanese Ngultrum',
    'BWP': 'Botswana Pula',
    'BYN': 'Belarusian Ruble',
    'BZD': 'Belize Dollar',
    'CAD': 'Canadian Dollar',
    'CDF': 'Congolese Franc',
    'CHF': 'Swiss Franc',
    'CLP': 'Chilean Peso',
    'CNY': 'Chinese Yuan',
    'COP': 'Colombian Peso',
    'CRC': 'Costa Rican Colón',
    'CUP': 'Cuban Peso',
    'CVE': 'Cape Verdean Escudo',
    'CZK': 'Czech Koruna',
    'DJF': 'Djiboutian Franc',
    'DKK': 'Danish Krone',
    'DOP': 'Dominican Peso',
    'DZD': 'Algerian Dinar',
    'EGP': 'Egyptian Pound',
    'ERN': 'Eritrean Nakfa',
    'ETB': 'Ethiopian Birr',
    'EUR': 'Euro',
    'FJD': 'Fijian Dollar',
    'FKP': 'Falkland Islands Pound',
    'FOK': 'Faroese Króna',
    'GBP': 'British Pound Sterling',
    'GEL': 'Georgian Lari',
    'GHS': 'Ghanaian Cedi',
    'GIP': 'Gibraltar Pound',
    'GMD': 'Gambian Dalasi',
    'GNF': 'Guinean Franc',
    'GTQ': 'Guatemalan Quetzal',
    'GYD': 'Guyanese Dollar',
    'HKD': 'Hong Kong Dollar',
    'HNL': 'Honduran Lempira',
    'HRK': 'Croatian Kuna',
    'HTG': 'Haitian Gourde',
    'HUF': 'Hungarian Forint',
    'IDR': 'Indonesian Rupiah',
    'ILS': 'Israeli New Shekel',
    'INR': 'Indian Rupee',
    'IQD': 'Iraqi Dinar',
    'IRR': 'Iranian Rial',
    'ISK': 'Icelandic Króna',
    'JMD': 'Jamaican Dollar',
    'JOD': 'Jordanian Dinar',
    'JPY': 'Japanese Yen',
    'KES': 'Kenyan Shilling',
    'KGS': 'Kyrgystani Som',
    'KHR': 'Cambodian Riel',
    'KID': 'Kiribati Dollar',
    'KMF': 'Comorian Franc',
    'KRW': 'South Korean Won',
    'KWD': 'Kuwaiti Dinar',
    'KYD': 'Cayman Islands Dollar',
    'KZT': 'Kazakhstani Tenge',
    'LAK': 'Laotian Kip',
    'LBP': 'Lebanese Pound',
    'LKR': 'Sri Lankan Rupee',
    'LRD': 'Liberian Dollar',
    'LSL': 'Lesotho Loti',
    'LYD': 'Libyan Dinar',
    'MAD': 'Moroccan Dirham',
    'MDL': 'Moldovan Leu',
    'MGA': 'Malagasy Ariary',
    'MKD': 'Macedonian Denar',
    'MMK': 'Myanma Kyat',
    'MNT': 'Mongolian Tugrik',
    'MOP': 'Macanese Pataca',
    'MRU': 'Mauritanian Ouguiya',
    'MUR': 'Mauritian Rupee',
    'MVR': 'Maldivian Rufiyaa',
    'MWK': 'Malawian Kwacha',
    'MXN': 'Mexican Peso',
    'MYR': 'Malaysian Ringgit',
    'MZN': 'Mozambican Metical',
    'NAD': 'Namibian Dollar',
    'NGN': 'Nigerian Naira',
    'NIO': 'Nicaraguan Córdoba',
    'NOK': 'Norwegian Krone',
    'NPR': 'Nepalese Rupee',
    'NZD': 'New Zealand Dollar',
    'OMR': 'Omani Rial',
    'PAB': 'Panamanian Balboa',
    'PEN': 'Peruvian Nuevo Sol',
    'PGK': 'Papua New Guinean Kina',
    'PHP': 'Philippine Peso',
    'PKR': 'Pakistani Rupee',
    'PLN': 'Polish Zloty',
    'PYG': 'Paraguayan Guarani',
    'QAR': 'Qatari Rial',
    'RON': 'Romanian Leu',
    'RSD': 'Serbian Dinar',
    'RUB': 'Russian Ruble',
    'RWF': 'Rwandan Franc',
    'SAR': 'Saudi Riyal',
    'SBD': 'Solomon Islands Dollar',
    'SCR': 'Seychellois Rupee',
    'SDG': 'Sudanese Pound',
    'SEK': 'Swedish Krona',
    'SGD': 'Singapore Dollar',
    'SHP': 'Saint Helena Pound',
    'SLL': 'Sierra Leonean Leone',
    'SOS': 'Somali Shilling',
    'SRD': 'Surinamese Dollar',
    'SSP': 'South Sudanese Pound',
    'STN': 'São Tomé and Príncipe Dobra',
    'SYP': 'Syrian Pound',
    'SZL': 'Swazi Lilangeni',
    'THB': 'Thai Baht',
    'TJS': 'Tajikistani Somoni',
    'TMT': 'Turkmenistani Manat',
    'TND': 'Tunisian Dinar',
    'TOP': 'Tongan Paʻanga',
    'TRY': 'Turkish Lira',
    'TTD': 'Trinidad and Tobago Dollar',
    'TWD': 'New Taiwan Dollar',
    'TZS': 'Tanzanian Shilling',
    'UAH': 'Ukrainian Hryvnia',
    'UGX': 'Ugandan Shilling',
    'USD': 'United States Dollar',
    'UYU': 'Uruguayan Peso',
    'UZS': 'Uzbekistani Som',
    'VES': 'Venezuelan Bolívar',
    'VND': 'Vietnamese Dong',
    'VUV': 'Vanuatu Vatu',
    'WST': 'Samoan Tala',
    'XAF': 'Central African CFA Franc',
    'XAG': 'Silver Ounce',
    'XAU': 'Gold Ounce',
    'XCD': 'East Caribbean Dollar',
    'XDR': 'Special Drawing Rights',
    'XOF': 'West African CFA Franc',
    'XPF': 'CFP Franc',
    'YER': 'Yemeni Rial',
    'ZAR': 'South African Rand',
    'ZMW': 'Zambian Kwacha',
    'ZWL': 'Zimbabwean Dollar'
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

def on_convert():
    """Handle conversion when the Convert button is clicked."""
    try:
        amount = float(amount_entry.get())
        from_currency_name = from_currency_combobox.get()
        to_currency_name = to_currency_combobox.get()

        from_currency = [code for code, name in currency_names.items() if name == from_currency_name][0]
        to_currency = [code for code, name in currency_names.items() if name == to_currency_name][0]

        converted_amount = convert_currency(amount, from_currency, to_currency)
        result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_currency_options():
    """Update currency options in the dropdowns."""
    try:
        _, currencies = get_exchange_rates("USD")
        full_currency_names = [currency_names.get(code, code) for code in currencies]
        global all_currency_names
        all_currency_names = sorted(full_currency_names)
        filter_combobox_options(from_currency_combobox, all_currency_names)
        filter_combobox_options(to_currency_combobox, all_currency_names)
        
        from_currency_combobox.set("United States Dollar")
        to_currency_combobox.set("Euro")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while fetching currencies: {e}")

def filter_combobox_options(combobox, options):
    """Filter and update the options in a combobox."""
    combobox['values'] = options
    if combobox.get() not in options:
        combobox.set("")

def on_search_from_currency(*args):
    """Filter options in the 'From Currency' combobox based on search."""
    search_term = from_currency_search.get().lower()
    filtered_options = [name for name in all_currency_names if search_term in name.lower()]
    filter_combobox_options(from_currency_combobox, filtered_options)

def on_search_to_currency(*args):
    """Filter options in the 'To Currency' combobox based on search."""
    search_term = to_currency_search.get().lower()
    filtered_options = [name for name in all_currency_names if search_term in name.lower()]
    filter_combobox_options(to_currency_combobox, filtered_options)

root = tk.Tk()
root.title("Currency Converter")

root.geometry("600x500")
root.minsize(400, 300)

background_color = "#f4f4f9"
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
result_font = ("Arial", 12, "italic")
bg_color = "#ffffff"

root.configure(bg=background_color)

frame = tk.Frame(root, bg=background_color)
frame.pack(padx=20, pady=20, expand=True, fill='both')

# Set grid configuration for resizable behavior
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)

tk.Label(frame, text="Amount:", font=label_font, bg=background_color).grid(row=0, column=0, sticky='e', padx=10, pady=5)
amount_entry = tk.Entry(frame, font=entry_font, bg=bg_color)
amount_entry.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

tk.Label(frame, text="From Currency:", font=label_font, bg=background_color).grid(row=1, column=0, sticky='e', padx=10, pady=5)
from_currency_search = tk.Entry(frame, font=entry_font, bg=bg_color)
from_currency_search.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
from_currency_search.bind("<KeyRelease>", on_search_from_currency)

from_currency_combobox = ttk.Combobox(frame, font=entry_font, state='readonly')
from_currency_combobox.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

tk.Label(frame, text="To Currency:", font=label_font, bg=background_color).grid(row=3, column=0, sticky='e', padx=10, pady=5)
to_currency_search = tk.Entry(frame, font=entry_font, bg=bg_color)
to_currency_search.grid(row=3, column=1, padx=10, pady=5, sticky='ew')
to_currency_search.bind("<KeyRelease>", on_search_to_currency)

to_currency_combobox = ttk.Combobox(frame, font=entry_font, state='readonly')
to_currency_combobox.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

convert_button = tk.Button(frame, text="Convert", font=button_font, command=on_convert, bg="#007bff", fg="#ffffff")
convert_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="", font=result_font, bg=background_color)
result_label.grid(row=6, column=0, columnspan=2, pady=10)

_, currencies = get_exchange_rates("USD")
all_currency_names = sorted([currency_names.get(code, code) for code in currencies])

update_currency_options()

root.mainloop()
