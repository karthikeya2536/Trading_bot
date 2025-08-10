Simplified Binance Futures Trading Bot
This is a command-line trading bot written in Python for interacting with the Binance Futures Testnet. It allows users to place Market, Limit, and Stop-Limit orders securely and provides detailed logging for all actions.

Features
Multiple Order Types: Place Market, Limit, and Stop-Limit orders.

Interactive CLI: A user-friendly command-line interface for easy operation.

Input Validation: Ensures that user inputs like symbol, side, and quantity are valid before sending them to the API.

Robust Error Handling: Catches and clearly displays API and order-related errors from Binance.

Comprehensive Logging: Logs all major events, including API requests, responses, and errors, to a trading_bot.log file for easy debugging and record-keeping.

Secure: Uses environment variables or direct input for API keys (for local use).

Requirements
Python 3.6+

python-binance library

Setup & Installation
Clone the repository or download the script:

git clone <your-repo-url>
cd <your-repo-directory>

Install the required Python library:

pip install python-binance

Get your Binance Testnet API Keys:

Register for an account on the Binance Futures Testnet.

Generate an API Key and Secret Key.

Important: Make sure to enable trading permissions for the key.

How to Run
Navigate to the script's directory in your terminal.

Run the script:

python trading_bot.py

Enter your credentials:

The script will prompt you to enter your Binance Testnet API Key and Secret Key.

(For better security, you can set these as environment variables named BINANCE_API_KEY and BINANCE_API_SECRET to avoid entering them each time.)

Usage
Once the bot is running, you will see the main menu:

--- Main Menu ---
1. Place Market Order
2. Place Limit Order
3. Place Stop-Limit Order (Bonus)
4. Exit

Select an option by typing the corresponding number and pressing Enter.

Follow the prompts to enter the order details (e.g., Symbol BTCUSDT, Side buy, Quantity 0.01).

The bot will confirm if the order was placed successfully or display an error message if it failed.

Getting Testnet Funds
If you receive a Margin is insufficient error, it means your testnet account has no funds.

Go to the Binance Futures Testnet site.

Find and click the "Faucet" to add free testnet assets (USDT, BTC, etc.) to your account.

Logging
All transactions, successful or not, are logged with a timestamp in the trading_bot.log file. This is useful for tracking activity and debugging issues.

Disclaimer
This bot is for educational and demonstration purposes only. It is configured to run on the Binance Testnet and does not use real money. Trading cryptocurrencies involves significant risk.
