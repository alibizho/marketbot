import discord
from os.path import exists
from discord.ext import commands, tasks
from discord.utils import get
import json
from json import dump, load
import os
import random

# #
intents = discord.Intents.default()
intents.members = True
#
bot = commands.Bot(command_prefix='$$', intents = intents)
bot.remove_command("help")
#
#
#
#
#
#
#
#
#
mainshop = [{"name":"In Stock", "In Stock":"1 Million coins", "price":"$0.15/m"}]
#
#
#
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('The Cheapest Coin Shop'))
    global channel
    print(f'{bot.user} has connected to Discord!')
    channel = bot.get_channel(CHANNEL_ID)
    TimeIncreaser.start()

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(801186979772891206) # YOUR INTEGER GUILD ID HERE
    welcome_channel = guild.get_channel(801186979772891209) # YOUR INTEGER CHANNEL ID HERE
    bot_cmd = guild.get_channel(801206692792631306)
    information = guild.get_channel(801198833487839282)
    prices = guild.get_channel(801204360084324402)
    em = discord.Embed(title="Welcome To Market Port")
    em.add_field(name=f"Welcome to one of the cheapest Shop out there", value=f"{member.mention}!", inline=False)
    em.add_field(name="Coins", value=f"You can see all of our Coin Prices in {prices.mention}", inline=False)
    em.add_field(name="Stock?", value=f"You can check our Stock in {bot_cmd.mention} with !stock", inline=False)
    em.add_field(name="Rules & TOS and more information?", value=f"Make sure to check out our Rules and ToS channel {information.mention}", inline=False)
    em.add_field(name="Gamble?", value="Want to double your money or even triple it, well you can double your money thanks to our bot", inline=False)
    em.add_field(name="Need more help?", value="You can can type `$$help` for even more information", inline=False)
    em.set_thumbnail(url="https://media.discordapp.net/attachments/825796659279429642/826446222374076467/Screenshot_6.png")
    em.set_footer(text="Bot, made by alibi#6393")
    await welcome_channel.send(embed=em)




@bot.command(pass_context=True)
async def secret(ctx, name: str):
    await ctx.send("You found a secret command, wow(yep, nothing happened)")

@bot.command(aliases=["htp"])
async def howtoplay(ctx):
    em = discord.Embed(title="How To Play",
                       description="If you click on 'How To Play' it will send you on  website that will explain you how to play",
                       url="https://www.blackjackapprenticeship.com/how-to-play-blackjack/")
    await ctx.send(embed=em)

@bot.command()
async def help(ctx):
    em = discord.Embed(title="Help", description="Use $$<command> to use the command", inline=False)
    em.add_field(name="Shop Commands", value="`$$stock` to check the stock", inline=False)
    em.add_field(name="`$$Balance/bal`", value="To check the balance", inline=False)
    em.add_field(name="Leaderboard", value="`$$leaderboard/lb <top>` to check who is the most wealthiest", inline=False)
    em.add_field(name="Gambling", value="`$$blackjack/bj_start <amount>` to play blackjack and double your market coins", inline=False)
    em.add_field(name="How To Start A Game", value="`$$blackjack <value>` this command will start a blackjack game also will require to specify betting amount")
    em.add_field(name="Hit", value="`$$h` this command allow you to get another card in the round")
    em.add_field(name="Stand", value="`$$s` this command will make you stand if u like ur cards")
    em.add_field(name="How To Play", value="$$howtoplay/htp this comand will show you how to play")
    em.add_field(name="Check Warning", value="`$$checkwarning` to check your warning", inline=False)
    em.add_field(name="Admin Info", value="`$$helpadmin` to get the admin information", inline=False)
    em.add_field(name="Developer Info", value="`$$info` to get the information about developer",inline=False)
    em.set_footer(text="Made by alibi#6393")
    await ctx.send(embed=em)


@bot.command()
@commands.has_permissions(administrator=True)
async def helpadmin(ctx):
    em = discord.Embed(title="Help for Admins", description="Hello new admin here are some commands that you will need to use: ")
    em.add_field(name="Kicking", value="`$$kick` to kick someone", inline=False)
    em.add_field(name="Banning", value="`$$ban` to ban someone", inline=False)
    em.add_field(name="Unbanning", value="`$$unban` to unban someone", inline=False)
    em.add_field(name="Warning", value="`$$warn <user>` to warn someone", inline=False)
    em.add_field(name="Check Warning", value="`$$checkwarnings <user>` to check someone's someone")
    em.add_field(name="Addstock", value="`$$addstock <number>` to add stock", inline=False)
    em.add_field(name="Sold", value="`$$sold <number>` to sell stock", inline=False)
    em.add_field(name="Set Price", value="`setprice <price>` to set price")
    em.add_field(name="Adding Balance", value="`$$addmc <user> <value>` to add to someones balance", inline=False)
    em.add_field(name="Removing Balance", value="`$$usedmc <user> <value>` to take away money from someones balance", inline=False)
    em.add_field(name="Adding List", value="`$$addlist <user> <invites>` to add them to the ad list", inline=False)
    em.add_field(name="Removing List", value="`$$rlist <user> <invites>` to delete them from the ad list or edit there invites", inline=False)
    em.add_field(name="Show List", value="`$$showlist` to show everyone in the list", inline=False)
    em.add_field(name="Live Transaction", value="`$$livetransaction\lt <amount> <attachment>` to show the transactions")
    await ctx.send(embed=em)


@bot.command(pass_context=True)
async def info(ctx):
    # Underneath is how to make bot react to the user's mesg
    # await ctx.message.add_reaction("✅")
    # this is how to make embede mesg
    embeded = discord.Embed(
        title="Welcome to the server",
        description="Hi, I am programmer in python, this is one of my projects. If you want to have bot you can write to me in discord.",
        color=0x1abc9c,
    )
    embeded.add_field(name="Want To Buy This Bot?", value="You Can Buy This Bot, Just DM Me")
    embeded.set_footer(text="The Market Bot was made by alibi#6393")
    msg = await ctx.send(embed=embeded)







@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has been banned')

# The below code unbans player.
@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

# The below code kicks player
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')


@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member:discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    amount = 1
    bal = await update_warnings(ctx.author)

    await update_warnings(member, amount, "warnings")
    await ctx.send(f"You added warning to {member.mention}")
    await member.send("You were given a warning in the Market Port")

@bot.command()
@commands.has_permissions(administrator=True)
async def checkwarnings(ctx, member:discord.Member):
    users = await get_bank_data()
    await open_account(member)
    user = member

    warning = users[str(user.id)]["warnings"]


    bal = await update_warnings(ctx.author)

    await ctx.send(f"The user {member.mention} has warnings: {warning}")

@bot.command()
async def checkwarning(ctx):
    user = ctx.author
    await open_account(ctx.author)
    users = await get_bank_data()
    warning = users[str(user.id)]["warnings"]


    bal = await update_warnings(ctx.author)

    await ctx.send(f"You have warnings: {warning}")

@bot.command(pass_context=True, aliases=["bal"])
async def balance(ctx):
    user = ctx.author
    await open_account(ctx.author)

    users = await get_bank_data()

    stock_amt = users[str(user.id)]["wallet"]
    if stock_amt == 0:
        stock_amt = "you're broke"

    em = discord.Embed(title = f"{ctx.author.name}'s balance", color=discord.Color.purple())
    em.add_field(name = "Wallet", value = stock_amt)
    await ctx.send(embed = em)




async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["invites"] = 0
        users[str(user.id)]["warnings"] = 0
    with open("mainbank.json", "w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    return users

async def update_warnings(user, change = 0, mode = "warnings"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["warnings"]]
    return bal



async def update_invite(user, change = 0, mode = "invites"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["invites"]]
    return bal

async def update_invite_m(user, change=0,  mode = "invites"):
    users = await get_bank_data()

    users[str(user.id)][mode] = users[str(user.id)][mode] -change

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["invites"]]
    return bal


async def update_bank(user, change = 0, mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"]]
    return bal

async def update_bj(user, change = 0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)]["wallet"] = users[str(user.id)]["wallet"] + change * 2

    with open("mainbank.json", "w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"]]
    return bal
async def update_tie(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)]["wallet"] = users[str(user.id)]["wallet"] + change

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["wallet"]]
    return bal


async def add_mc(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users["wallet"] += change

    with open("stat.json", "w") as f:
        json.dump(users, f)

    bal = [users["wallet"]]

    return bal
async def update_bank_m(user, change = 0, mode = "wallet"):
    users = await get_bank_data()
    if users[mode] > change:
        return False
    else:
        users[mode] -= change

    with open("stat.json", "w") as f:
        json.dump(users, f)

    bal = [users["wallet"]]

    return bal

@bot.command(aliases = ["lb"])
async def leaderboard(ctx,x = 10):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"]
        leader_board[total_amount] = name
        total.append(total_amount)


    total = sorted(total,reverse=True)

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        member = await bot.fetch_user(id_)
        name = member.name

        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)

@bot.command(aliases = ["lt"])
@commands.has_permissions(administrator=True)
async def livetransaction(ctx, amount=None):
    amount = int(amount)
    attachment = ctx.message.attachments[0]
    await ctx.channel.purge(limit=1)
    await ctx.send(f"Just sold {amount} millions feeling good. Thanks for purchasing, proof: {attachment.url}")

    # file=discord.File("")
    # await ctx.send(file=file)





@bot.command(pass_context=True, aliases=["rlist"])
@commands.has_permissions(administrator=True)
async def removelist(ctx, member: discord.Member, amount):
    users = await get_bank_data()
    await open_account(ctx.author)
    await open_account(member)



    bal = await update_invite(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("MAN he doesnt hav that much ")
        return False
    else:
        await update_invite(member, -amount, "invites")
        await ctx.send(f"You removed {member.mention}")


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def addlist(ctx, member: discord.Member,  amount =None):
    users = await get_bank_data()
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("Please enter the amount of invites for the user")
        return

    bal = await update_invite(ctx.author)

    amount = int(amount)
    await update_invite(member, amount)
    await ctx.send(f"You have put {member.mention} and {amount} invites to your list")



@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def showlist(ctx):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["invites"]
        leader_board[total_amount] = name
        if total_amount> 0:
            total.append(total_amount)

    total = sorted(total)
    em = discord.Embed(title=f"Top priority",
                       description="This is your list for today",
                       color=discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        member = await bot.fetch_user(id_)
        name = member.name

        em.add_field(name=f"{index}. {name}", value=f"{member.mention}  {amt} Invites", inline=False)
        index +=1

    await ctx.send(embed=em)













@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def addmc(ctx, member:discord.Member, amount = None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    await update_bank(member, amount, "wallet")
    await ctx.send(f"You added {amount} market coins to {member.mention}")

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def usedmc(ctx, member:discord.Member, amount = None):
    users = await get_bank_data()
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("That man is already broke... ")
        await update_bank_m(member, -1*amount, "wallet")
    else:
        await update_bank(member, -amount, "wallet")
        await ctx.send(f"You took {amount} market coins from {member.mention}")







million = "Million"
billion = "Billion"




@bot.command(pass_context=True)
async def stock(ctx):
    users = await get_stock_data()
    em = discord.Embed(title="Stock")
    for item in mainshop:
        name = item["name"]
        instock = users["stock"]
        price = users["price"]
        if instock < 1000:
            em.add_field(name=name, value=f"{instock} {million}", inline=True)
        elif instock >= 1000:
            instock = instock / 1000
            em.add_field(name=name, value=f"{instock} {billion}", inline=True)
        # if len(str(price)) >= 2:
        #     price = price / 100
        # elif len(str(price)) < 2:
        #     price = price / 100
        em.add_field(name="Price", value=f"${price}/mil", inline=False)
    await ctx.send(embed=em)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def addstock(ctx,  amount = None):
    global inst
    inst = 0
    bal = await update_stock_min(ctx.author)

    if amount == None:
        await ctx.send("Please enter the amount")
        return


    # bal = await update_bank_plus(ctx.author)

    amount = int(amount)

    await update_stock_plus(ctx.author, amount)
    await ctx.send(f"You added {amount} million coins to stock")

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def setprice(ctx, amount = None):
    pric = await set(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return
    amount = float(amount)
    await set(ctx.author, amount)
    await ctx.send(f"You set price to {amount}")


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def sold(ctx, amount = None):
    global inst
    # await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return
    bal = await update_stock_min(ctx.author)


    amount = int(amount)

    if await update_stock_min(ctx.author, amount) == False:
        await ctx.send("NO")
    else:
        await ctx.send(f"You sold {amount} million coins from stock")
async def open_stock(user):
    global inst
    inst = 0
    pric = 0.15

    users = await get_stock_data()

    users = {}
    users["stock"] = inst
    users["price"] = float(pric)
    with open("stat.json", "w") as f:
        json.dump(users,f)
    return True

async def get_stock_data():
    with open("stat.json", "r") as f:
        users = json.load(f)
    return users



async def set(user, change = float(0), mode="price"):
    users = await get_stock_data()

    users[mode] = float(change)

    with open("stat.json", "w") as f:
        json.dump(users, f)

    bal = [users["price"]]

    return bal
async def update_stock_plus(user, change = 0, mode = "stock"):
    users = await get_stock_data()

    users["stock"] += change


    with open("stat.json", "w") as f:
        json.dump(users,f)

    bal = [users["stock"]]



    return bal

async def update_stock_min(ctx, change = 0, mode = "stock"):
    users = await get_stock_data()
    if users["stock"] < change:
        return False
    else:
        users[mode] = users[mode] - change

    with open("stat.json", "w") as f:
        json.dump(users,f)

    bal = [users["stock"]]
    return bal



DEFAULT_CONFIG = {
            "Token":                "ODI2NTE4MzEyNzkwOTE3MTIw.YGNpKQ.QgnZ0q98tmvi7c1xIJ4LHYC_1n4",
            "Channel_ID":           "827112804846141470",
            "Prefix":               "$$",
            "Start_Game":           "blackjack",
            "Hit":                  "hit",
            "Stand":                "stand",
            "TimeOut":              "20",
            "CoolDown":             "1"
        }


if not exists("Config.json"):
    with open("Config.json", 'w') as file:
        dump(DEFAULT_CONFIG, file)

with open('Config.json', 'r') as file:
    CONFIG = load(file)


TOKEN = CONFIG["Token"]

CHANNEL_ID = int(CONFIG["Channel_ID"])

PREFIX = CONFIG["Prefix"]

START_GAME = CONFIG["Start_Game"]

HIT = CONFIG["Hit"]

STAND = CONFIG["Stand"]

TIMEOUT = int(CONFIG["TimeOut"])

COOLDOWN = int(CONFIG["CoolDown"])


channel = None


class BlackJack:
    def __init__(self):
        #self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4


    def deal(self):
        hand = []
        for _ in range(2):
            random.shuffle(self.deck)
            card = self.deck.pop()
            if card == 11: card = "J"
            if card == 12: card = "Q"
            if card == 13: card = "K"
            if card == 14: card = "A"
            hand.append(card)
        return hand

    def deal_dealer(self):
        hand = []
        random.shuffle(self.deck)
        card = self.deck.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
        return hand

    def Reset_Values(self):
        global GameStarted, Player_Hand, Dealer_Hand, Hit, Timer,Current_Player
        Timer = 0
        Hit = 0
        GameStarted = True
        Current_Player = ""
        Player_Hand = ""
        Dealer_Hand = ""
        self.__init__()

    def total(self,hand):
        total = 0
        for card in hand:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A":
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += card
        return total

    def hit(self,hand:list):
        card = self.deck.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
        return hand

    def CreateEmbed(self,DealerInfo,PlayerInfo,username, equation="\u200b"):
        embed = discord.Embed(title="Market Port BlackJack Game")
        embed.add_field(name=f"{username[0:username.find('#')]}", value=PlayerInfo, inline=True)
        embed.add_field(name="Dealer",value=DealerInfo,inline=True)
        embed.add_field(value=equation, name="\u200b", inline=False)
        return embed

    async def print_results(self,dealer_hand, player_hand, username):
        global Player_Hand,Dealer_Hand
        for i in dealer_hand[1:]:
            Dealer_Hand += f"{random.choice(['♥', '♦', '♠', '♣'])} {i} "
        return self.CreateEmbed(f"Cards - {Dealer_Hand} \n Total - {self.total(dealer_hand)}", f"Cards - {Player_Hand} \n Total - {self.total(player_hand)}", username)


    async def blackjack(self,dealer_hand, player_hand,channel,username, user, amount, ctx):

        if self.total(player_hand) == 21 and self.total(dealer_hand) == 21:
            await channel.send(embed=await self.print_results(dealer_hand, player_hand,username))
            await channel.send("It is Tie both the dealer and the player got 21\n")
            await update_tie(user, amount, "wallet")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")
            self.Reset_Values()

        elif self.total(player_hand) == 21:
            await channel.send(embed=await self.print_results(dealer_hand, player_hand,username))
            await channel.send("Congratulations! You got a Blackjack!\n")
            await update_bj(user, amount, "wallet")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")
            self.Reset_Values()

        elif self.total(dealer_hand) == 21:
            await channel.send(embed = await self.print_results(dealer_hand, player_hand,username))
            await channel.send("Sorry the dealer got a Blackjack! you lose\n")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")
            self.Reset_Values()


    async def score(self,dealer_hand, player_hand,channel,username, user, amount, ctx):
        if self.total(player_hand) == 21 and self.total(dealer_hand) == 21:
            await channel.send(embed=await self.print_results(dealer_hand, player_hand, username))
            await channel.send("It is Tie both the dealer and the player got 21\n")
        elif self.total(player_hand) == 21:
            await channel.send(embed=await self.print_results(dealer_hand, player_hand, username))
            await channel.send("Congratulations! You got a Blackjack!\n")
            await update_bj(user, amount, "wallet")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")

        elif self.total(dealer_hand) == 21:
            await channel.send(embed=await self.print_results(dealer_hand, player_hand, username))
            await channel.send("Sorry, you lose. The dealer got a blackjack.\n")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")

        elif self.total(player_hand) > 21:
            await channel.send(embed=await self.print_results(dealer_hand, player_hand, username))
            await channel.send("Sorry. You busted. You lose.\n")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")

        elif self.total(dealer_hand) > 21:
            await channel.send(embed=await self.print_results(dealer_hand, player_hand, username))
            await channel.send("Dealer busts. You win!\n")
            await update_bj(user, amount, "wallet")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")

        elif self.total(player_hand) < self.total(dealer_hand):
            await channel.send(embed=await self.print_results(dealer_hand, player_hand, username))
            await channel.send("Sorry. Your score isn't higher than the dealer. You lose.\n")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")

        elif self.total(player_hand) > self.total(dealer_hand):
            await channel.send(embed=await self.print_results(dealer_hand, player_hand, username))
            await channel.send("Congratulations. Your score is higher than the dealer. You win\n")
            await update_bj(user, amount, "wallet")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")

        else:
            await channel.send(embed=await self.print_results(dealer_hand, player_hand, username))
            await channel.send("It is a tie both the player and the dealer got the same total amount\n")
            users = await get_bank_data()
            stock_amt = users[str(user.id)]["wallet"]
            await ctx.send(f"You now have {stock_amt} market coins")

bj = BlackJack()

dealer_hand = []
player_hand = []

GameStarted = True

Current_Player = ""

Player_Hand = ""

Dealer_Hand = ""

Hit = 0
Timer = 0




@tasks.loop(seconds=1)
async def TimeIncreaser():
    global Timer,GameStarted,channel

    if not GameStarted:
        Timer+=1

    if Timer==TIMEOUT:
        await channel.send("Time is out you can start a new match")
        bj.Reset_Values()

@bot.command(pass_context = True, aliases=[START_GAME])
async def bj_start(ctx, amount = None):
    ''' this function start a blackjack match '''
    global dealer_hand,player_hand,Current_Player,GameStarted,PREFIX,Player_Hand,Dealer_Hand


    if GameStarted:
        bot.amount = int(amount)
        users = await get_bank_data()
        await open_account(ctx.author)
        if amount == None:
            await ctx.send("Please enter the amount")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("YOU DON'T HAVE THAT MUCH.")
            await update_bank_m(ctx.author, -1 * amount, "wallet")
        if amount < 10:
            await ctx.send("Minimum is 10")
            await update_bank_m(ctx.author, -1 * amount, "wallet")
        else:
            await update_bank(ctx.author, -amount, "wallet")
        Current_Player = str(ctx.message.author)
        dealer_hand = bj.deal_dealer()
        player_hand = bj.deal()


        for i in player_hand:
            Player_Hand += f"{random.choice(['♥', '♦', '♠', '♣'])} {i} "

        Dealer_Hand += f"{random.choice(['♥', '♦', '♠', '♣'])} {dealer_hand[0]} "
        await channel.send(f"Type {PREFIX}h to **hit**, Type {PREFIX}s to **stand** ->{TIMEOUT}sec match<-")
        await channel.send(embed = bj.CreateEmbed(f"cards - {Dealer_Hand} \n Total - ?", f"Cards -  {Player_Hand} \n Total - {bj.total(player_hand)}" ,Current_Player, f"K,Q,K=10 | A=1 or 11"))
        GameStarted = False
        await bj.blackjack(dealer_hand, player_hand, channel, Current_Player, ctx.author, bot.amount, ctx)

@commands.cooldown(rate=1, per=1)
@bot.command(pass_context = True, aliases=[HIT])
async def h(ctx):
    '''write it if you want to get another card in the round'''
    global dealer_hand,player_hand,channel, Current_Player,GameStarted,Player_Hand,Dealer_Hand,Hit,Timer
    Timer = 0
    if str(ctx.message.author) == Current_Player:
        bj.hit(player_hand)
        Player_Hand += f"{random.choice(['♥', '♦', '♠', '♣'])} {player_hand[-1]} "

        if Hit==3 or bj.total(player_hand)>=21:
            GameStarted = True
            while bj.total(dealer_hand) < 17:
                bj.hit(dealer_hand)
            await bj.score(dealer_hand, player_hand,channel,Current_Player, ctx.author, bot.amount, ctx)
            bj.Reset_Values()
        else:
            await channel.send(f"Type {PREFIX}h to **hit**, Type {PREFIX}s to **stand**")
            await channel.send(embed=bj.CreateEmbed(f"cards - {Dealer_Hand} \n Total - ?",f"Cards -  {Player_Hand} \n Total - {bj.total(player_hand)}",Current_Player, f"K,Q,K=10 | A=1 or 11"))
        Hit+=1

@commands.cooldown(rate=1, per=1)
@bot.command(pass_context = True, aliases=[STAND])
async def s(ctx):
    '''write it if you want to stand your round'''
    global dealer_hand, player_hand, channel

    if str(ctx.message.author) == Current_Player:
        while bj.total(dealer_hand) < 17:
            bj.hit(dealer_hand)
        await bj.score(dealer_hand, player_hand,channel,Current_Player, ctx.author, bot.amount, ctx)
        bj.Reset_Values()

@bot.command(pass_context = True)
async def time(ctx):
    '''this command shows the time left for a match'''
    global Timer,TIMEOUT,channel,GameStarted

    if not GameStarted:
        await channel.send(f"Time left for match {TIMEOUT-Timer} seconds")
    else:
        await channel.send("No match was started")



@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: str):
    if amount == "all":
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=(int(amount) + 1))

bot.run('TOKEN', bot=True, reconnect=True)
