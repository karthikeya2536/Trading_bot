A **command-line trading bot** written in Python for interacting with the **Binance Futures Testnet**.  
It allows users to place **Market**, **Limit**, and **Stop-Limit** orders securely and provides detailed logging for all actions.

---

## ✨ Features

- **Multiple Order Types** – Place **Market**, **Limit**, and **Stop-Limit** orders.
- **Interactive CLI** – User-friendly command-line interface for easy operation.
- **Input Validation** – Ensures that user inputs (symbol, side, quantity, etc.) are valid before sending them to the API.
- **Robust Error Handling** – Catches and clearly displays API and order-related errors from Binance.
- **Comprehensive Logging** – Logs all major events (API requests, responses, and errors) to a `trading_bot.log` file.
- **Secure** – Uses environment variables or direct input for API keys for local use.

---

## 🛠 Requirements

- Python **3.6+**
- [`python-binance`](https://pypi.org/project/python-binance/) library

---

## 📥 Setup & Installation

1. **Clone the repository** or download the script:
    ```
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. **Install dependencies**:
    ```
    pip install python-binance
    ```

3. **Get your Binance Testnet API keys**:
    - Register for an account on the [Binance Futures Testnet](https://testnet.binancefuture.com/).
    - Generate your **API Key** and **Secret Key**.
    - **Important:** Enable Futures trading permissions for the key.

---

## ▶ How to Run

1. Navigate to the bot's directory:
    ```
    cd <your-repo-directory>
    ```

2. Run the bot:
    ```
    python trading_bot.py
    ```

3. Enter your **API credentials** when prompted:
    - For better security, set them as environment variables:
      ```
      export BINANCE_API_KEY="your_api_key"
      export BINANCE_API_SECRET="your_api_secret"
      ```

---

## 📚 Usage

Once the bot is running, you'll see:

--- Main Menu ---

Place Market Order

Place Limit Order

Place Stop-Limit Order (Bonus)

Exit

text

- Select an option by entering its number.
- Follow prompts to enter **Symbol** (`BTCUSDT`), **Side** (`buy`), **Quantity** (`0.01`), etc.
- The bot will confirm the order placement or display an error.

---

## 💰 Getting Testnet Funds

If you get:
Margin is insufficient

text
It means your account balance is 0.

- Log into the [Binance Futures Testnet](https://testnet.binancefuture.com/)
- Click **Faucet** in the UI  
- Request free testnet assets (e.g., USDT, BTC)

---

## 📝 Logging

- All transactions (successful or failed) are logged with timestamps in **`trading_bot.log`**.
- Useful for **tracking activity** and **debugging**.

---

## ⚠ Disclaimer

**This bot is for educational and demonstration purposes only.**  
It operates only on the **Binance Futures Testnet** and does **not use real money**.  
Trading cryptocurrencies carries significant risk — use responsibly.

---
