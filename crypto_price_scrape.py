#! usr/bin/env python3
import coinmarketcap as c
import sys

PRICE_DICT = {'BTC': '1', 'ETH': '1027', 'XRP': '52', 'BCH': '1831', 'LTC': '2', 'EOS': '1765', 'BNB': '1839', 'USDT': '825', 'XLM': '512', 'ADA': '2010', 'TRX': '1958', 'XMR': '328', 'DASH': '131', 'BSV': '3602', 'XTZ': '2011', 'MIOTA': '1720', 'NEO': '1376', 'ETC': '1321', 'ONT': '2566', 'XEM': '873', 'MKR': '1518', 'BAT': '1697', 'ZEC': '1437', 'CRO': '3635', 'VET': '3077', 'DOGE': '74', 'USDC': '3408', 'BTG': '2083', 'REP': '1104', 'DCR': '1168', 'WAVES': '1274', 'QTUM': '1684', 'TUSD': '2563', 'OMG': '1808', 'LSK': '1214', 'NANO': '1567', 'RVN': '2577', 'BCD': '2222', 'HOT': '2682', 'ICX': '2099', 'ZRX': '1896', 'BCN': '372', 'LINK': '1975', 'ZIL': '2469', 'BTS': '463', 'BTT': '3718', 'IOST': '2405', 'PAX': '3330', 'DGB': '109', 'NPXS': '2603', 'XVG': '693', 'ENJ': '2130', 'AE': '1700', 'KMD': '1521', 'HT': '2502', 'STEEM': '1230', 'SC': '1042', 'KCS': '2087', 'MXM': '3115', 'AOA': '2874', 'BTM': '1866', 'WTC': '1925', 'THETA': '2416', 'STRAT': '1343', 'DAI': '2308', 'FCT': '1087', 'SNT': '1759', 'XIN': '2349', 'INB': '3116', 'ABBC': '3437', 'MCO': '1776', 'CNX': '2027', 'WAX': '2300', 'GNT': '1455', 'QBIT': '3224', 'GXC': '1750', 'THR': '3144', 'VEST': '3607', 'ARDR': '1320', 'DGD': '1229', 'PPT': '1789', 'MONA': '213', 'PAI': '2900', 'MAID': '291', 'ORBS': '3835', 'ARK': '1586', 'ELF': '2299', 'GUSD': '3306', 'AION': '2062', 'NULS': '2092', 'MANA': '1966', 'HC': '1903', 'RDD': '118', 'DENT': '1886', 'XZC': '1414', 'LRC': '1934', 'ZEN': '1698', 'ELA': '2492', 'TRUE': '2457', 'NAS': '1908'}

def main():
	print(get_price("ltc"))

def get_price(crypto):
	mkt = c.Market()
	lst = mkt.listings()			
	try:
		t = mkt.ticker(PRICE_DICT[crypto.upper()], convert="EUR")
		return t["data"]["quotes"]["EUR"]["price"]
	except (TypeError, KeyError) as e:
		return ""

if __name__ == "__main__":
    main()