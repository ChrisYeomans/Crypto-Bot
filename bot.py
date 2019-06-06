#! usr/bin/env python3
import discord, dbl, asyncio
from crypto_price_scrape import get_price, get_crypto_list

HELP_MESSAGE = """
**This bot does all things crypto the commands are as follows:**\n
!price currency - Gives the current price of your desired currency name, use ticker codes like BTC or ETH
!list - Gives a list of currently supported Crypto-Currencies
!supported currency - Says whether or not a specific currenty is supported
!? currency - See !supported
"""

def main():
	TOKEN = input()
	client = discord.Client()

	@client.event
	async def on_ready():
		print("The bot is ready!")
	
	@client.event
	async def on_message(message):
		if message.content[:6].lower() == "!price":
			curr = message.content[7:]
			print(curr)
			price = get_price(curr.upper())
			if price:
				await message.channel.send("One "+curr.upper()+" is worth $"+str(price))
			else:
				await message.channel.send("Sorry that is not a recognised currency")
		elif message.content[:5].lower() == "!list":
			await message.channel.send("The following currencies are supported: "+', '.join(get_crypto_list()))
		elif message.content[:10].lower() == "!supported":
			if message.content[11:].upper() in get_crypto_list():
				await message.channel.send("That currency *is* supported")
			else:
				await message.channel.send("That currency *is not* supported")
		elif message.content[:2] == '!?':
			if message.content[3:].upper() in get_crypto_list():
				await message.channel.send("That currency is supported")
			else:
				await message.channel.send("That currency is not supported")
		elif message.content.lower() == "!help" or message.content.lower() == "!h":
			await message.channel.send(HELP_MESSAGE)


	client.run(TOKEN)

if __name__ == "__main__":
	main()