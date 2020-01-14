import requests 
import time
import discord 


r = requests.session()
client = discord.Client()


@client.event
async def on_ready():
    print(f"Logged in {client.user}")


def viewer(url):
    print(url)

    view = 0
    while(view < 40):     ##### ADDS 40 VIEWS. BE CAREFUL GOING TO HIGH TO AVOID BANS ######
        view = view + 1
        requests.get(url)


@client.event 
async def on_message(message):
    
    if message.content.startswith('!view '):

        embed = discord.Embed(title="Increase Ebay Views!", description="Request recieved, sending views...", color=0xFF0000)
        embed.set_footer(text="Ebay View Bot made by @UndefinedErrors")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJ4oZ9W_GeyDogIPC4EuS2eBs_VrAaRO8P8Yyesr97_JPIJiKjIw&s")
        await message.channel.send(embed=embed)

        url = message.content.split('!view ')[1]
        viewer(url)

        embed = discord.Embed(title="Ebay Views Increased!", description="Views Successfully Sent!", color=0xFF0000)
        embed.set_footer(text="Ebay View Bot made by @UndefinedErrors")
        embed.set_thumbnail(url="https://cdn-b.william-reed.com/var/wrbm_gb_hospitality/storage/images/1/5/0/8/498051-3-eng-GB/Hotels-can-expect-increased-demand-in-2014-but-must-adapt-to-modern-travellers_wrbm_small.jpg")
        await message.channel.send(embed=embed)

    if message.content == '!stop': await client.logout()





      

#### TOKEN GOES HERE FROM YOUR DISCORD DEVLOPER PORTAL###### 
client.run('TOKEN')





