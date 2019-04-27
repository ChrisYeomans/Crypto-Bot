#! usr/bin/env python3
import discord, dbl, asyncio
from crypto_price_scrape import get_price

def main():
	TOKEN = input()
	client = discord.Client()

	@client.event
	async def on_ready():
		print("The bot is ready!")
	
	@client.event
	async def on_message(message):
		if message.content[:6] == "!price":
			curr = message.content[7:]
			print(curr)
			price = get_price(curr.upper())
			if price:
				await message.channel.send("One "+curr.upper()+" is worth €"+str(price))
			else:
				await message.channel.send("Sorry that is not a recognised currency")

	client.run(TOKEN)

if __name__ == "__main__":
	main()