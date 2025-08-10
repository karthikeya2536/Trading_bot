
import logging
import os
from decimal import Decimal, InvalidOperation
from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("trading_bot.log"),
        logging.StreamHandler()
    ]
)

class BasicBot:
    """
    A simple trading bot for the Binance Futures Testnet.
    Handles API connection, order placement, and logging.
    """
    def __init__(self, api_key, api_secret, testnet=True):
        """
        Initializes the bot.

        :param api_key: Your Binance API key.
        :param api_secret: Your Binance API secret.
        :param testnet: Set to True to use the testnet (default).
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        self.client = self._create_client()
        self._check_connection()

    def _create_client(self):
        """Sets up the connection to the Binance API."""
        try:
            client = Client(self.api_key, self.api_secret, testnet=self.testnet)
            if self.testnet:
                 logging.info("Client initialized for Binance Futures Testnet.")
            else:
                 logging.info("Client initialized for Binance Futures Mainnet. BE CAREFUL!")
            return client
        except Exception as e:
            logging.error(f"Failed to create Binance client: {e}")
            raise

    def _check_connection(self):
        """Pings the API to verify the connection and credentials."""
        try:
            self.client.futures_account()
            logging.info("Successfully connected to Binance Futures API.")
        except BinanceAPIException as e:
            logging.error(f"API connection failed: {e}. Double-check your API keys and permissions.")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred during connection check: {e}")
            raise

    def _execute_order(self, order_params):
        """
        Sends an order to Binance and handles the response.

        :param order_params: A dictionary holding all the order details.
        """
        try:
            logging.info(f"Placing order with parameters: {order_params}")
            order = self.client.futures_create_order(**order_params)
            logging.info("Successfully placed order.")
            logging.info(f"Response: {order}")
            print("\n--- ✅ Order Placed Successfully ---")
            for key, value in order.items():
                print(f"{key}: {value}")
            print("-------------------------------------\n")
            return order
        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {e}")
            print(f"\n--- ❌ API Error --- \nMessage: {e}\n--------------------\n")
        except BinanceOrderException as e:
            logging.error(f"Binance Order Exception: {e}")
            print(f"\n--- ❌ Order Error --- \nMessage: {e}\n---------------------\n")
        except Exception as e:
            logging.error(f"An unexpected error occurred while placing order: {e}")
            print(f"\n--- ❌ Unexpected Error --- \nMessage: {e}\n--------------------------\n")
        return None

    def place_market_order(self, symbol, side, quantity):
        """Places a market order."""
        params = {
            'symbol': symbol,
            'side': side.upper(),
            'type': 'MARKET',
            'quantity': quantity
        }
        return self._execute_order(params)

    def place_limit_order(self, symbol, side, quantity, price):
        """Places a limit order."""
        params = {
            'symbol': symbol,
            'side': side.upper(),
            'type': 'LIMIT',
            'quantity': quantity,
            'price': price,
            'timeInForce': 'GTC'
        }
        return self._execute_order(params)

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """Places a stop-limit order (Bonus Feature)."""
        params = {
            'symbol': symbol,
            'side': side.upper(),
            'type': 'STOP_LIMIT',
            'quantity': quantity,
            'price': price,
            'stopPrice': stop_price,
            'timeInForce': 'GTC'
        }
        return self._execute_order(params)


def get_validated_input(prompt, validation_func, error_message):
    """Gets and validates user input."""
    while True:
        user_input = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        else:
            print(f"Invalid input. {error_message}")

def get_decimal_input(prompt):
    """Gets a positive decimal number from the user."""
    while True:
        try:
            value = Decimal(input(prompt).strip())
            if value > 0:
                # Return as a string to avoid floating point precision issues.
                return str(value)
            else:
                print("Invalid input. Please enter a number greater than zero.")
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")

def cli_interface():
    """The main command-line interface for the user."""
    print("--- Welcome to the Simplified Trading Bot ---")
    print("This bot will interact with the Binance Futures Testnet.")
    
    # For better security, use environment variables for API keys in a real application.
    api_key = os.environ.get('BINANCE_API_KEY') or input("Enter your Binance Testnet API Key: ").strip()
    api_secret = os.environ.get('BINANCE_API_SECRET') or input("Enter your Binance Testnet API Secret: ").strip()

    try:
        bot = BasicBot(api_key, api_secret, testnet=True)
    except Exception:
        print("\nCould not initialize the bot. Check the log file for details and restart.")
        return

    while True:
        print("\n--- Main Menu ---")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Place Stop-Limit Order (Bonus)")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == '4':
            print("Exiting bot. Goodbye!")
            break
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice, please select a valid option.")
            continue

        symbol = get_validated_input(
            "Enter symbol (e.g., BTCUSDT): ",
            lambda s: s.isalnum() and len(s) > 4,
            "Symbol should be something like BTCUSDT."
        ).upper()
        
        side = get_validated_input(
            "Enter side (buy/sell): ",
            lambda s: s.lower() in ['buy', 'sell'],
            "Side must be 'buy' or 'sell'."
        ).upper()

        quantity = get_decimal_input("Enter quantity: ")

        if choice == '1':
            bot.place_market_order(symbol, side, quantity)
        
        elif choice == '2':
            price = get_decimal_input("Enter limit price: ")
            bot.place_limit_order(symbol, side, quantity, price)

        elif choice == '3':
            stop_price = get_decimal_input("Enter stop price (the trigger price): ")
            price = get_decimal_input("Enter limit price (the execution price): ")
            
            # Warn user about potentially illogical stop-limit prices.
            if (side == 'BUY' and Decimal(price) < Decimal(stop_price)) or \
               (side == 'SELL' and Decimal(price) > Decimal(stop_price)):
                print("\nWarning: For a BUY order, the limit price is usually above the stop price.")
                print("For a SELL order, the limit price is usually below the stop price.")
                print("This order might not execute as expected.\n")
            bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)

if __name__ == "__main__":
    cli_interface()
