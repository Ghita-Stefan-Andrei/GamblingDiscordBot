import random
import time
import pacaneaFruits as pf
import discord
command = dict()
pf.dublaj = 0
def checkLine(numbers, first, second, third, forth, fifth):
    if numbers[first] == numbers[second] and numbers[first] == numbers[third] and numbers[first] == numbers[forth] and numbers[first] == numbers[fifth]:
        if numbers[first] == ":lemon:" or numbers[first] == ":cherries:" or numbers[first] == ":banana:":
            pf.credit += pf.bet * 15
        elif numbers[first] == ":watermelon:" or numbers[first] == ":grapes:":
            pf.credit += pf.bet * 70
        elif numbers[first] == ":seven:":
            pf.credit += pf.bet * 500
        elif numbers[first] == ":crown:":
            pf.credit += pf.bet * 100
    elif numbers[first] == numbers[second] and numbers[first] == numbers[third] and numbers[first] == numbers[forth]:
        if numbers[first] == ":lemon:" or numbers[first] == ":cherries:" or numbers[first] == ":banana:":
            pf.credit += pf.bet * 3
        elif numbers[first] == ":watermelon:" or numbers[first] == ":grapes:":
            pf.credit += pf.bet * 12
        elif numbers[first] == ":seven:":
            pf.credit += pf.bet * 25
        elif numbers[first] == ":crown:":
            pf.credit += pf.bet * 20
    elif numbers[first] == numbers[second] and numbers[first] == numbers[third]:
        if numbers[first] == ":lemon:" or numbers[first] == ":cherries:" or numbers[first] == ":banana:":
            pf.credit += pf.bet * 1
        elif numbers[first] == ":watermelon:" or numbers[first] == ":grapes:":
            pf.credit += pf.bet * 4
        elif numbers[first] == ":seven:":
            pf.credit += pf.bet * 5
        elif numbers[first] == ":crown:":
            pf.credit += pf.bet * 5

async def setMoney(message, user, channel):
    if str(message.channel.id) == pf.pacChannel:
        if not pf.runningGame:
            pf.credit = int(str(message.content).split()[1])
            if pf.credit:
                pf.runningGame = 1
                await message.channel.send('The game has begun!')
                await message.channel.send(f':moneybag: TOTAL CREDIT :moneybag:')
                await message.channel.send(f':dollar: : {pf.credit}')
        else:
            await message.channel.send("You can't change your credits after the start of the game")
command[f'{pf.commTag}setCredit'] = setMoney
    
async def setBet(message, user, channel):
    if str(message.channel.id) == pf.pacChannel:
        pf.bet = int(str(message.content).split()[1])
        if pf.bet > pf.credit:
            pf.bet = 0
            await message.channel.send(f':no_entry_sign: You do not have enough credits for that. Credit {pf.credit} :no_entry_sign:')
        else:
            await message.channel.send(f'Amount betted :money_with_wings: : {pf.bet}')
command[f'{pf.commTag}bet'] = setBet

async def invarte(message, user, channel):
    if pf.dublaj == 1:
        pf.credit += pf.winnings
    pf.dublaj = 0
    if pf.runningGame and str(message.channel.id) == pf.pacChannel:
        if pf.bet <= pf.credit and pf.credit > 0:
            await message.channel.send(f':dollar: Old Balance :dollar: : {pf.credit - pf.bet}')
            pf.credit -= pf.bet
            creditBackUp = pf.credit

            numbers = list()
            for number in range(15):
                numbers.append(pf.fruits[random.randint(0,6)])

            line1 = ""
            for elem in range(5):
                line1 += numbers[elem] + " "
            await message.channel.send(line1)
            time.sleep(0.5)

            line2 = ""
            for elem in range(5, 10):
                line2 += numbers[elem] + " "
            await message.channel.send(line2)
            time.sleep(0.5)

            line3 = ""
            for elem in range(10, 15):
                line3 += numbers[elem] + " "
            await message.channel.send(line3)
            
            #first line
            checkLine(numbers, 0, 1, 2, 3, 4)

            #second line
            checkLine(numbers, 5, 6, 7, 8, 9)

            #third line
            checkLine(numbers, 10, 11, 12, 13, 14)

            #V
            checkLine(numbers, 0, 6, 12, 8, 4)

            #main diagonal
            checkLine(numbers, 0, 1, 7, 13, 14)

            #V^(-1)
            checkLine(numbers, 10, 6, 2, 8, 14)

            #second diagonal
            checkLine(numbers, 10, 11, 7, 3, 4)

            pf.winnings = 0
            if pf.credit > creditBackUp:
                pf.winnings = pf.credit - creditBackUp
                pf.credit -= pf.winnings
            if pf.winnings > 0:
                await message.channel.send(f':money_mouth: :money_with_wings: :moneybag: YOU WON {pf.winnings} :moneybag: :money_with_wings: :money_mouth: ')
                #await message.channel.send(f':dollar: New Balance :dollar: : {pf.credit}')
                await message.channel.send("Double or nothing?")
            else:
                await message.channel.send('Better luck next time')
        else:
            if pf.credit == 0:
                await message.channel.send('Your credit is 0 the game will end.')
                pf.runningGame = 0
            else:
                await message.channel.send(f'The bet you want to place is bigger than your total credits: {pf.credit} please bet a lower amount.')
    else:
        if str(message.channel.id) != pf.pacChannel:
            pass
        if not pf.runningGame and str(message.channel.id) == pf.pacChannel:
            await message.channel.send('There is no active game.')
command[f'{pf.commTag}roll'] = invarte

async def test(message, user, channel):
    await message.channel.send(pf.winnings)
command[f'{pf.commTag}test'] = test

async def freeRoll(message, user, channel):
    if str(message.channel.id) == pf.pacChannel:
        numbers = list()
        for number in range(15):
            numbers.append(pf.fruits[random.randint(0,6)])

        line1 = ""
        for elem in range(5):
            line1 += numbers[elem] + " "
        await message.channel.send(line1)
        time.sleep(0.5)

        line2 = ""
        for elem in range(5, 10):
            line2 += numbers[elem] + " "
        await message.channel.send(line2)
        time.sleep(0.5)

        line3 = ""
        for elem in range(10, 15):
            line3 += numbers[elem] + " "
        await message.channel.send(line3)
command[f'{pf.commTag}freeRoll'] = freeRoll

async def endGame(message, user, channel):
    if str(message.channel.id) == pf.pacChannel:
        await message.channel.send('Game stopped.')
        pf.credit = 0
        pf.runningGame = 0
command[f'{pf.commTag}end'] = endGame

async def setChannel(message, user, channel):
    flag = 0
    for role in range(len(message.author.roles)):
        if "Pacanea Maintenance" == str(message.author.roles[role]):
            flag = 1
    if flag:
    	pf.pacChannel = str(channel.id)
    	await message.channel.send('This channel has been selected')
command[f'{pf.commTag}setPacaneaChannel'] = setChannel

async def help(message, user, channel):
    await message.channel.send('''```HELLO AND WELCOME TO YOUR NEW ADDICTION,  ENJOOOOOY...
    -First you will have to select a channel where you will be playing using /setPacaneaChannel in the channel where the game is supposed to take place(you need to do this once per server or when you want to change the channel) Admin use only
    -To curse your days for the decisions you\'ve taken, you need money so start a game with /setCredit <Amount to lose>
    -Also you will be betting a smaller amount every time you roll, to set it use /bet <value to be betted>
    -And the most amazing and wonderful part.... /roll
    -After you lost all your money or by a miracle you still have some and just got bored please use /end to stop you current session so others can suff*cough*... enjoy it too
    -To see prizes /prize
    -If you want to see this again /help
    
    -Author GitHub: https://github.com/Ghita-Stefan-Andrei ```''')
command[f'{pf.commTag}help'] = help

async def prize(message, user, channel):
    await message.channel.send(':seven: : 5: 500x |           4:  25x  |          3:  5x')
    await message.channel.send(':crown: : 5:  100x |           4:  20x |           3:  5x')
    await message.channel.send(':grapes: : 5:    70x |           4:   12x |           3:  4x')
    await message.channel.send(':watermelon: : 5:    70x |           4:   12x |           3:  4x')
    await message.channel.send(':banana: : 5:     15x |           4:     3x |           3:  1x')
    await message.channel.send(':cherries: : 5:     15x |           4:     3x |           3:  1x')
    await message.channel.send(':lemon: : 5:     15x |           4:     3x |           3:  1x')
command[f'{pf.commTag}prize'] = prize
