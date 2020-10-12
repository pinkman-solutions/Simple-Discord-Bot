import discord 
from discord.ext import commands

client = commands.Bot(command_prefix=".")

rules = [":one: Don't upload any file/picture/video that has viruses, illegal, pornographic or shocking content.",

":two: No scams (staff will not be covering any private selling).",

":three: No discussions about religion, politics or anything that could bring to a fight.",

":four: The only allowed language is English And Hebrew.",

":five: If you don't reply for more than 24 hours in a ticket, it will be closed.",

":six: No use of vulgar words, doing so will result in a warning.",

":seven: Payment is BTC (Bitcoin) only for every purchase made from the @𝘼𝙙𝙢𝙞𝙣𝙨.",]


filter_words = ["shit","jew","Shit","fuck","Fuck","motherfucker","Motherfucker","2g1c","2 girls 1 cup","acrotomophilia","alabama hot pocket","bitch","Bitch","stealing","Stealing","copy","copyed","stolen"]



@client.event
async def on_ready():
	print("Bot is ready!")

@client.event
async def on_message(msg):
	for word in filter_words:
		if word in msg.content:
			await msg.delete()

	await client.process_commands(msg)



@client.command()
async def rule(ctx,*,number):
	await ctx.send(rules[int(number)-1])

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
	await member.send("You have been kicked from Nova Buy & Sell, Because:"+reason)
	await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
	await ctx.send(member.name + " has been banned from Nova Buy & Sell, Because:"+reason)
	await member.ban(reason=reason)






























client.run("TOKEN here")



