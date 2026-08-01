from datetime import datetime
import json
import os
import requests

# 1. Free API endpoint for live Bitcoin prices
URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

print("Fetching live Bitcoin price data...\n")

try:
    # Make GET request to the API
    response = requests.get(URL)

    # Check if request was successful (HTTP status code 200)
    if response.status_code == 200:
        data = response.json()

        # Extract values safely from nested JSON structure
        time_updated = data["time"]["updated"]
        usd_price = data["bpi"]["USD"]["rate"]
        code = data["bpi"]["USD"]["code"]

        print("====================================")
        print(f" 🪙 BITCOIN PRICE TRACKER")
        print("====================================")
        print(f" Last Updated : {time_updated}")
        print(f" Current Price: ${usd_price} {code}")
        print("====================================\n")

        # Ask user if they want to save this to JSON history
        save_choice = (
            input("Do you want to log this price to JSON history? (y/n): ")
            .strip()
            .lower()
        )

        if save_choice == "y":
            history_file = "crypto_history.json"

            # Create entry object
            new_log = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "price_usd": usd_price,
            }

            # Load existing history if file exists
            history = []
            if os.path.exists(history_file):
                with open(history_file, "r") as file:
                    try:
                        history = json.load(file)
                    except json.JSONDecodeError:
                        history = []

            # Append new entry and save back to JSON
            history.append(new_log)
            with open(history_file, "w") as file:
                json.dump(history, file, indent=4)

            print(f"\n✅ Price logged successfully to '{history_file}'!")

    else:
        print(f"❌ Failed to fetch data. Server status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"❌ Connection Error: {e}")