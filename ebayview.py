import requests 
import time
import discord 


r = requests.session()
client = discord.Client()


@client.event
asxxxxx60-==
nc def on_ready():
    print(f"Logged in {client.user}")


def viewer(url):
    print(url)

    view = 0
    while(view < 40):     ##### ADDS 40 VIEWS. BE CAREFUL GOING TO HIGH TO AVOID BANS ######
        view = view + 1
        requests.get(url)


@client.event 
async def on_message(message):
    
    if message.content.startswith('!eviews '):

        embed = discord.Embed(title="Increase Ebay Views!", description="Request recieved, sending views...", color=0xFF0000)
        embed.set_footer(text="12N EBAY VIEWER")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773434230167306251/823240693992128512/12nn.jpg")
        await message.channel.send(embed=embed)

        url = message.content.split('!view ')[1]
        viewer(url)

        embed = discord.Embed(title="Ebay Views Increased!", description="Views Successfully Sent!", color=0xFF0000)
        embed.set_footer(text="12N EBAY VIEWER")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773434230167306251/823240693992128512/12nn.jpg")
        await message.channel.send(embed=embed)

    if message.content == '!stop': await client.logout()




      

#### TOKEN GOES HERE FROM YOUR DISCORD DEVLOPER PORTAL###### 
client.run('ODA2NjMyODQxMjU2NjMyMzMx.YBsRXw.pI9BNiF0NtM16iB7o4PpM71NfpM')





