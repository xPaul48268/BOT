import asyncio
import os
import discord
from discord import player
from discord import message
from mcstatus import MinecraftServer
from mcipc.query import Client

offline=("Server ist offline oder es sind momentan keine Spieler online!")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        while True:
            server = MinecraftServer.lookup("Hoshire.de:25565")
            status = server.status()
            query = server.query()
            global join_player
            join_player = (query.players.names)
            await client.change_presence(activity=discord.Game(name=f"auf Hoshire.de | {(status.players.online)} Spieler online | {(status.latency)}"))
            await asyncio.sleep(1)
            await client.change_presence(activity=discord.Game(name=f"auf Hoshire.de | {(status.players.online)} Spieler online | {(status.latency)}"))
            await asyncio.sleep(1)
            await client.change_presence(activity=discord.Game(name=f"auf Hoshire.de | {(status.players.online)} Spieler online | {(status.latency)}"))

    async def on_message(self, message):

        if message.content.startswith("/help"):

            embed = discord.Embed(
                title  = "Hilfe",
                color = 0xA9D6EB

            )
            embed.add_field(name="Server Ip:",value="/ip",inline=False)
            embed.add_field(name="Player Online:",value="/state",inline=False)
            embed.add_field(name="Player list:",value="/list",inline=False)
            embed.add_field(name="Server Email:",value="/email",inline=False)
            embed.add_field(name="Support Email:",value="/support",inline=False)
            embed.add_field(name="Server Plugins:",value="/plugin",inline=False)

            embed.set_thumbnail(url="https://yt3.ggpht.com/N73FEJr1HeHl656np4s5Sia3bUAsAPpOQtqVNJ6WAimgL2LtvpQa7AUldUIk3BzP7AxeD_a5=s88-c-k-c0x00ffffff-no-rj")

            await message.channel.send(embed=embed)

        if message.content.startswith("/Help"):

            embed = discord.Embed(
                title  = "Hilfe",
                color = 0xA9D6EB

            )
            embed.add_field(name="Server Ip:",value="/ip",inline=False)
            embed.add_field(name="Player Online:",value="/state",inline=False)
            embed.add_field(name="Player list:",value="/list",inline=False)
            embed.add_field(name="Server Email:",value="/email",inline=False)
            embed.add_field(name="Support Email:",value="/support",inline=False)
            embed.add_field(name="Server Plugins:",value="/plugin",inline=False)

            embed.set_thumbnail(url="https://yt3.ggpht.com/N73FEJr1HeHl656np4s5Sia3bUAsAPpOQtqVNJ6WAimgL2LtvpQa7AUldUIk3BzP7AxeD_a5=s88-c-k-c0x00ffffff-no-rj")

            await message.channel.send(embed=embed)



        if message.content.startswith('/ip'):
            embed4 = discord.Embed(
                    title  = "Netzwerk Information",
                    color = 0xA9D6EB
                    )
            embed4.set_thumbnail(url="https://yt3.ggpht.com/N73FEJr1HeHl656np4s5Sia3bUAsAPpOQtqVNJ6WAimgL2LtvpQa7AUldUIk3BzP7AxeD_a5=s88-c-k-c0x00ffffff-no-rj")

            embed4.add_field(name="Server Adresse",value="cloud-trooper.plasak8s.de:30577",inline=False)
            embed4.add_field(name="Domain Adresse",value="Hoshire.de:25565",inline=False)
            embed4.add_field(name="Vereinfachte Domain",value="Hoshire.de",inline=False)
            embed4.add_field(name="Physische Adresse",value="D4-5D-64-D7-31-62",inline=False)
            embed4.add_field(name="Standardgateway",value="fe80::2e3a:fdff:fea3:6d1e%8",inline=False)
            await message.channel.send(embed=embed4)


        if message.content.startswith('/state'):
            try:
                with Client(("Hoshire.de"), int("25565"), timeout=1.5) as client:
                    basic_stats = client.stats()
                    embed3 = discord.Embed(
                    title  = "Status",
                    color = 0xA9D6EB
                    )
                    embed3.set_thumbnail(url="https://yt3.ggpht.com/N73FEJr1HeHl656np4s5Sia3bUAsAPpOQtqVNJ6WAimgL2LtvpQa7AUldUIk3BzP7AxeD_a5=s88-c-k-c0x00ffffff-no-rj")

                    embed3.add_field(name="Spieler online",value=str(basic_stats.num_players),inline=False)
                    embed3.add_field(name="Max. Spieler",value=str(basic_stats.max_players),inline=False)
                    await message.channel.send(embed=embed3)

            except:
                await message.channel.send(offline)

        if message.content.startswith('/list'):
            try:
                with Client(("Hoshire.de"), int("25565"), timeout=1.5) as client:
                    full_stats = client.stats(full=True)
                    basic_stats = client.stats
                    player_list_message = " "
                    for player_name in full_stats.players:
                        player_list_message = player_list_message + "- " + player_name + " "


                    embed2 = discord.Embed(
                    title  = "Liste",
                    color = 0xA9D6EB
                    )
                    embed2.set_thumbnail(url="https://yt3.ggpht.com/N73FEJr1HeHl656np4s5Sia3bUAsAPpOQtqVNJ6WAimgL2LtvpQa7AUldUIk3BzP7AxeD_a5=s88-c-k-c0x00ffffff-no-rj")

                    embed2.add_field(name="Spieler online",value=player_list_message,inline=False)
                    await message.channel.send(embed=embed2)

            except:
                await message.channel.send(offline)

        if message.content.startswith('/email'):
            embed5 = discord.Embed(
                    title  = "Business",
                    color = 0xA9D6EB
                    )
            embed5.set_thumbnail(url="https://yt3.ggpht.com/N73FEJr1HeHl656np4s5Sia3bUAsAPpOQtqVNJ6WAimgL2LtvpQa7AUldUIk3BzP7AxeD_a5=s88-c-k-c0x00ffffff-no-rj")

            embed5.add_field(name="Email",value="hoshire.de@gmail.com",inline=False)
            await message.channel.send(embed=embed5)

        if message.content.startswith('/support'):
            embed5 = discord.Embed(
                    title  = "Support",
                    color = 0xA9D6EB
                    )
            embed5.set_thumbnail(url="https://yt3.ggpht.com/N73FEJr1HeHl656np4s5Sia3bUAsAPpOQtqVNJ6WAimgL2LtvpQa7AUldUIk3BzP7AxeD_a5=s88-c-k-c0x00ffffff-no-rj")

            embed5.add_field(name="Email",value="hoshire.assistance@gmail.com",inline=False)
            embed5.add_field(name="Discord",value="xPaul#0044",inline=False)
            await message.channel.send(embed=embed5)


        if message.content.startswith('/plugin'):
            relevant_path = ("E:/SERVER-3 (HOSHIRE)/Lobby/plugins")
            included_extensions = ['jar']
            file_names = [fn for fn in os.listdir(relevant_path)
                        if any(fn.endswith(ext) for ext in included_extensions)]

            embed1 = discord.Embed(
            title  = "Plugins",
            color = 0xA9D6EB
)
            embed1.set_thumbnail(url="https://yt3.ggpht.com/N73FEJr1HeHl656np4s5Sia3bUAsAPpOQtqVNJ6WAimgL2LtvpQa7AUldUIk3BzP7AxeD_a5=s88-c-k-c0x00ffffff-no-rj")
            count = 0
            count1 = 1
            for element in file_names:
                total = (file_names[count])
                embed1.add_field(name=count1,value=total,inline=False)
                count += 1
                count1 += 1
            await message.channel.send(embed=embed1)



client = MyClient()
client.run("BOT CODE (BITTE BEI xPAUL#0044 ANFORDERN")
