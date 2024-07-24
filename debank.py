import requests
import csv
from datetime import datetime

class DebankAPI:
    def __init__(self, access_key):
        self.base_url = 'https://pro-openapi.debank.com/v1'
        self.headers = {
            'accept': 'application/json',
            'AccessKey': access_key
        }

    def get_chain_balance(self, user_id, chain_id):
        endpoint = f'{self.base_url}/user/chain_balance'
        params = {
            'id': user_id,
            'chain_id': chain_id
        }
        response = requests.get(endpoint, headers=self.headers, params=params)
        return response.json()

class Balance:
    def __init__(self, network, balance, currency, last_updated, explorer):
        self.network = network
        self.balance = balance
        self.currency = currency
        self.last_updated = last_updated
        self.explorer = explorer

    @staticmethod
    def from_api_response(response_data):
        balances = []
        for chain in response_data['result']:
            network = chain['name']
            balance = chain['balance']
            currency = chain['symbol']
            last_updated = chain['time_at']
            explorer = chain['explorer']

            # Parse the last updated timestamp
            last_updated_dt = datetime.fromtimestamp(last_updated)
            formatted_date = last_updated_dt.strftime("%d %b %Y, %I:%M %p IST")

            balances.append(Balance(network, balance, currency, formatted_date, explorer))
        return balances

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_balances(self, balances):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write headers
            writer.writerow(["Network", "Balance", "Last updated", "Explorer"])
            # Write data
            for balance in balances:
                writer.writerow([balance.network, f'{balance.balance} {balance.currency}', balance.last_updated, balance.explorer])
        print(f"Data saved to {self.filename}")

def main():
    access_key = '375d605d871858a9b3f21b88adbabbf96192b8d3'
    user_id = '0x5853ed4f26a3fcea565b3fbc698bb19cdf6deb85'
    chain_id = 'eth'
    csv_filename = 'chain_balance.csv'

    api = DebankAPI(access_key)
    response_data = api.get_chain_balance(user_id, chain_id)
    print(response_data)  # Print the JSON response to understand its structure

    balances = Balance.from_api_response(response_data)
    csv_writer = CSVWriter(csv_filename)
    csv_writer.write_balances(balances)

if __name__ == "__main__":
    main()
