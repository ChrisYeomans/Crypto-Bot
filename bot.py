#! usr/bin/env python3
import discord, dbl, asyncio
from crypto_price_scrape import get_price, get_crypto_list

def main():
	TOKEN = "NTcxNDk3MTU0Nzc5MTUyMzg0.XMOtTw.6FfMMiNuvIws67IpFNMKgf_pJaU"
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
		if message.content[:5].lower() == "!list":
			await message.channel.send("The following currencies are supported: "+', '.join(get_crypto_list()))
		if message.content[:10].lower() == "!supported":
			if message.content[11:].upper() in get_crypto_list():
				await message.channel.send("That currency is supported")
			else:
				await message.channel.send("That currency is not supported")

	client.run(TOKEN)

if __name__ == "__main__":
	main()