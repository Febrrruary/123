import csv
import time
import multiprocessing
from web3 import Web3
from eth_account import Account

# подключение к Infura
w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/DIoADHKb1zV4aBKBHTye93L6m9QPcipq"))

# чтение мнемонических фраз из файла
with open('/Users/ivan/Desktop/Seed/valid_mnemonic_phrases.txt') as f:
    mnemonics = [line.strip() for line in f]

def process_mnemonic(mnemonic):
    Account.enable_unaudited_hdwallet_features()
    # преобразование мнемонической фразы в приватный ключ
    private_key = w3.eth.account.from_mnemonic(mnemonic).privateKey.hex()

    # получение баланса по адресу, связанному с приватным ключом
    address = w3.eth.account.from_key(private_key).address
    balance = w3.eth.get_balance(address)

    return [private_key, balance]

if __name__ == '__main__':
    start_time = time.time()

    # запись результатов в файл CSV
    with open('/Users/ivan/Desktop/Seed/balances.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Private Key', 'Balance'])

        with multiprocessing.Pool() as pool:
            results = pool.map(process_mnemonic, mnemonics)

        for result in results:
            # запись результатов в файл CSV
            writer.writerow(result)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
