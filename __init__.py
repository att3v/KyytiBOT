from app.mac import mac, signals
import os
import random


try:
    sjokiFile = open("/home/atte/yowsapp-framework/modules/KyytiBOT/sjoki.txt", "r")
    sjokiFile.close()
except:
    sjokiFile = open("/home/atte/yowsapp-framework/modules/KyytiBOT/sjoki.txt", "w+")
    sjokiFile.close()

try:
    prismaFile = open("/home/atte/yowsapp-framework/modules/KyytiBOT/prisma.txt", "r")
    prismaFile.close()
except:
    prismaFile = open("/home/atte/yowsapp-framework/modules/KyytiBOT/prisma.txt", "w+")
    prismaFile.close()

try:
    koveroFile = open("/home/atte/yowsapp-framework/modules/KyytiBOT/kovero.txt", "r")
    koveroFile.close()
except:
    koveroFile = open("/home/atte/yowsapp-framework/modules/KyytiBOT/kovero.txt", "w+")
    koveroFile.close()

try:
    autoFile = open("/home/atte/yowsapp-framework/modules/KyytiBOT/auto.txt", "r")
    autoFile.close()
except:
    autoFile = open("/home/atte/yowsapp-framework/modules/KyytiBOT/auto.txt", "w+")
    autoFile.close()

'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.command_received.connect
def handle(message):
    if message.command == "ohjeet":
        ohjeet(message)
    elif message.command == "sjoki":
        sjoki(message)
    elif message.command == "prisma":
        prisma(message)
    elif message.command == "kovero":
        kovero(message)
    elif message.command == "auto":
        auto(message)
    elif message.command == "peruutus":
        peruutus(message)
    elif message.command == "lista":
        lista(message)
    elif message.command == "uusilista":
        uusilista(message)
    elif message.command == "vapaa":
        vapaa(message)
    elif message.command == "hyväbotti":
        hyväbotti(message)
    elif message.command == "lepo":
        lepo(message)

'''
Actual module code
==========================================================
'''
def ohjeet(message):
    answer = """Hei, olen *KyytiBOT* ja minut on koodannut kaikkien janoisten sankari, Atte Viertola.
    \n*Mahdolliset komennot:*
    \n*!sjoki* - Ilmoittaudut KyytiBOTille töihin seuraavaksi päiväksi ja ilmoitat tulevasi kyytiin Kivistön S-Marketilta. Sinut lisätään minun ylläpitämään listaan.
    \n*!kovero* - Ilmoittaudut KyytiBOTille töihin seuraavaksi päiväksi, sinut lisätään Koverolta noukittavien listaan.
    \n*!prisma* - Ilmoittaudut KyytiBOTille töihin seuraavaksi päiväksi, sinut lisätään Prisman rampilta noukittavien listaan.
    \n*!auto* - Ilmoittaudut KyytiBOTille töihin seuraavaksi päiväksi ja ilmoitat ajavasi seuraavana päivänä, sinun EI tarvitse ilmoittautua töihin erikseen. Jos olet kerennyt jo ilmoittautua ilman autoa, tämä komento lisää auton ilmoittautumiseesi.
    \n*!peruutus* - Peruutat ilmoittautumisesi töihin, perut samalla myös mahdolllisesti ilmoittamasi auton.
    \n*!lista* - Lähetän viestin, johon on listattu kaikki töihin tulevat, heidän noutopaikkansa sekä luvatut autot.
    \n*!uusilista* - Tyhjää edellisen päivän listan ja uudet ilmoittautumiset voi aloittaa.
    \n*HUOM! En pidä kirjaa mahdollisista erikoisjärjestelyistä kuten vain toiseen suuntaan tulemisesta, joten muista edelleen kertoa näistä erikseen!*
    """
    mac.send_message(answer, message.conversation)

def sjoki(message):
    who_name = message.who_name
    sjokiNames = getNames("sjoki")
    prismaNames = getNames("prisma")
    koveroNames = getNames("kovero")
    autoNames = getNames("auto")

    if who_name in sjokiNames or who_name in prismaNames or who_name in koveroNames or who_name in autoNames:
        answer = "*{}*, olet jo ilmoittautunut.".format(who_name)
        mac.send_message(answer, message.conversation)

    else:
        with open("/home/atte/yowsapp-framework/modules/KyytiBOT/sjoki.txt", "a") as sjokiFile:
            sjokiFile.write("{}\n".format(who_name))
        answer = "*{}*, ilmoittautumisesi on otettu vastaan.".format(who_name)
        mac.send_message(answer, message.conversation)

def prisma(message):
    who_name = message.who_name
    sjokiNames = getNames("sjoki")
    prismaNames = getNames("prisma")
    koveroNames = getNames("kovero")
    autoNames = getNames("auto")

    if who_name in sjokiNames or who_name in prismaNames or who_name in koveroNames or who_name in autoNames:
        answer = "*{}*, olet jo ilmoittautunut.".format(who_name)
        mac.send_message(answer, message.conversation)

    else:
        with open("/home/atte/yowsapp-framework/modules/KyytiBOT/prisma.txt", "a") as prismaFile:
            prismaFile.write("{}\n".format(who_name))
        answer = "*{}*, ilmoittautumisesi on otettu vastaan.".format(who_name)
        mac.send_message(answer, message.conversation)

def kovero(message):
    who_name = message.who_name
    sjokiNames = getNames("sjoki")
    prismaNames = getNames("prisma")
    koveroNames = getNames("kovero")
    autoNames = getNames("auto")

    if who_name in sjokiNames or who_name in prismaNames or who_name in koveroNames or who_name in autoNames:
        answer = "*{}*, olet jo ilmoittautunut.".format(who_name)
        mac.send_message(answer, message.conversation)

    else:
        with open("/home/atte/yowsapp-framework/modules/KyytiBOT/kovero.txt", "a") as koveroFile:
            koveroFile.write("{}\n".format(who_name))
        answer = "*{}*, ilmoittautumisesi on otettu vastaan.".format(who_name)
        mac.send_message(answer, message.conversation)

def auto(message):
    who_name = message.who_name
    autoNames = getNames("auto")

    if who_name in autoNames:
        answer = "*{}*, olet jo ilmoittautunut.".format(who_name)
        mac.send_message(answer, message.conversation)
        return

    sjokiNames = getNames("sjoki")

    if who_name in sjokiNames:
        with open("/home/atte/yowsapp-framework/modules/KyytiBOT/sjoki.txt", "w") as sjokiFile:
            for name in sjokiNames:
                if name != who_name:
                    sjokiFile.write("{}\n".format(name))
        with open("/home/atte/yowsapp-framework/modules/KyytiBOT/auto.txt", "a") as autoFile:
            autoFile.write("{}\n".format(who_name))
        answer = "*{}*, sinut on siirretty autollisten listaan.".format(who_name)
        mac.send_message(answer, message.conversation)
        return
        
    prismaNames = getNames("prisma")
    koveroNames = getNames("kovero")

    if who_name in prismaNames or who_name in koveroNames:
        answer = "*{}*, vain Kivistön S-Marketin kautta tulevat voivat ilmoittaa auton.".format(who_name)
        mac.send_message(answer, message.conversation)
        return

    else:
        with open("/home/atte/yowsapp-framework/modules/KyytiBOT/auto.txt", "a") as autoFile:
            autoFile.write("{}\n".format(who_name))
        answer = "*{}*, ilmoittautumisesi on otettu vastaan.".format(who_name)
        mac.send_message(answer, message.conversation)

def peruutus(message):
    who_name = message.who_name

    if who_name in getNames("sjoki"):
        removeName("sjoki", who_name)
        answer = "*{}*, ilmoittautumisesi on peruutettu.".format(who_name)
        mac.send_message(answer, message.conversation)

    elif who_name in getNames("prisma"):
        removeName("prisma", who_name)
        answer = "*{}*, ilmoittautumisesi on peruutettu.".format(who_name)
        mac.send_message(answer, message.conversation)

    elif who_name in getNames("kovero"):
        removeName("kovero", who_name)
        answer = "*{}*, ilmoittautumisesi on peruutettu.".format(who_name)
        mac.send_message(answer, message.conversation)

    elif who_name in getNames("auto"):
        removeName("auto", who_name)
        answer = "*{}*, ilmoittautumisesi on peruutettu.".format(who_name)
        mac.send_message(answer, message.conversation)

    else:
        answer = "*{}*, et ole vielä ilmoittautunut.".format(who_name)
        mac.send_message(answer, message.conversation)

def lista(message):
    
    sjokiList = getNames("sjoki")
    prismaList = getNames("prisma")
    koveroList = getNames("kovero")
    carList = getNames("auto")

    total = len(sjokiList) + len(prismaList) + len(koveroList) + len(carList)
    totalSjoki = len(sjokiList)
    totalPrisma = len(prismaList)
    totalKovero = len(koveroList)
    totalCars = len(carList)

    sjokiString = "\n ".join(sjokiList)
    prismaString = "\n ".join(prismaList)
    koveroString = "\n ".join(koveroList)
    carString = "\n ".join(carList)
    answer = """*Yhteensä tulossa: {}*
    \n*Kivistön S-Market: {}*
    {}
    \n*Prisman ramppi: {}*
    {}
    \n*Koveron Shell: {}*
    {}
    \n*Autolliset: {}*
    {}""".format(total, totalSjoki, sjokiString, totalPrisma, prismaString, totalKovero, koveroString, totalCars, carString)
    mac.send_message(answer, message.conversation)

def uusilista(message):
    emptyList("sjoki")
    emptyList("prisma")
    emptyList("kovero")
    emptyList("auto")

    answer = "*Lista tyhjennetty, uudet ilmoittautumiset voi alkaa.*"
    mac.send_message(answer, message.conversation)

def vapaa(message):
    mac.send_message("*MENISIT SINÄKI TÖI_HI*", message.conversation)

def hyväbotti(message):
    mac.send_message("beep boop, botti kiittää", message.conversation)

def lepo(message):
    mac.send_message("Shutdown in 3, 2, 1...", message.conversation)
    emptyList("sjoki")
    emptyList("prisma")
    emptyList("kovero")
    emptyList("auto")


##############################################################

#APUFUNKTIOT

##############################################################

def getNames(list):
    with open("/home/atte/yowsapp-framework/modules/KyytiBOT/{}.txt".format(list), "r") as file:
        names = file.read().splitlines()
    return names

def emptyList(list):
    open("/home/atte/yowsapp-framework/modules/KyytiBOT/{}.txt".format(list), "w+")
    return

def removeName(list, name):
    names = []
    with open("/home/atte/yowsapp-framework/modules/KyytiBOT/{}.txt".format(list), "r") as file:
        for i in getNames(list):
            if i != name:
                names.append(i)
    with open("/home/atte/yowsapp-framework/modules/KyytiBOT/{}.txt".format(list), "w") as file:
        for name in names:
            file.write("{}\n".format(name))
        return
