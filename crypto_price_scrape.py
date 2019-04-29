#! usr/bin/env python3
import ccxt

bittrex = ccxt.bittrex()

def main():
	print(get_crypto_list())
	print(get_price("BTC"))
	print(printable_crypto_list())

def get_price(crypto):
	if crypto.upper() in get_crypto_list():
		return ccxt.coinmarketcap().fetch_ticker(crypto.upper()+"/USD")['info']['price_usd']
	return ""

def get_crypto_list():
	return {s.split('/')[0] for s in ccxt.coinmarketcap().fetch_tickers()}

if __name__ == "__main__":
    main()