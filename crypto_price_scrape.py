#! usr/bin/env python3
import cryptocompare

def main():
	print(get_crypto_list())
	print(get_price("BTC"))

def get_price(crypto):
	if crypto.upper() in get_crypto_list():
		return cryptocompare.get_price('BTC',curr='USD',full=True)['RAW'][crypto.upper()]['USD']['PRICE']
	return ""

def get_crypto_list():
	return [e for e in cryptocompare.get_coin_list(format=False)]

if __name__ == "__main__":
    main()