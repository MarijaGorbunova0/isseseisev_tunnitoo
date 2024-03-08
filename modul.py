import random
from operator import index
import smtplib, ssl
from email.message import EmailMessage
#1
def registr(nimi, parool, kasutajad:list, paroolid:list):
   if nimi in kasutajad:
       print("kirjutage uus nimi")
   else:
       kasutajad.append(nimi)
       paroolid.append(parool)
       return kasutajad,paroolid
#2
def autoris(kasutajad: list, paroolid: list, polzovateli):
    nimi = input("Kirjutage oma nimi: ")
    if nimi in kasutajad:
        nimiIndeks = kasutajad.index(nimi)
        parool = input("Kirjutage parool: ")
        if parool == paroolid[nimiIndeks]:
            print("Kõik on hästi")
            polzovateli.append(nimi)
            polzovateli.append(parool)
            return kasutajad, paroolid
        else:
            print("Vale parool")
            return kasutajad, paroolid
    else:
         print("Sulle vaja registreerida")
         return kasutajad, paroolid
#3
def uus_parool_nimi(polzovateli,kasutajad:list,paroolid:list):
    zamena = int(input("kirjutage mida te tahate vahetada parol - 1, nimi - 2"))
    if zamena == 2:
        uusNimi = input("kirjutage uus nimi ")
        polzovateli[0] = uusNimi
        kasutajad[0] = uusNimi
        print("teie nimi on edukalt muudetud!")
        return polzovateli
    elif zamena == 1:
        uusParol = input("kirjutage uus parool ")
        polzovateli[1] = uusParol
        paroolid[0] = uusParol
        print("teie parool on edukalt muudetud!")
        return polzovateli
#4
def unustanudPR(paroolid, kasutajad):
    nimi = input("kirjutage oma nimi")
    if nimi in kasutajad:
        kiri = int(input("Sain meili teel parooli lähtestamise koodi.\n näita koodi - 1 \n parooli lähtestamise tühistamine – 2"))
        while True:
            if kiri == 1:
                smtp_server = "smtp.gmail.com"
                port = 587
                sender_email = input("kirjutage mail")
                password = input("Type your password(copied gmail) ")
                #create a secure SSL conntex
                context = ssl.create_default_context()
                msg = EmailMessage()
                msg.set_content(random.randint(1, 100))
                msg["Subject"] = "Tere Roman"
                msg["From"] = "mariarapirovna@gmail.com"
                msg["To"] = "sandakovroman2@gmail.com"
                #"try to log to server and email
                try:
                    server = smtplib.SMTP(smtp_server, port)
                    server.ehlo() #can be omitted
                    server.starttls(context = context)
                    server.ehlo()
                    server.login(sender_email, password)
                    #server.sendmail(sender_email, msg)
                    server.send_message(msg)
                except Exception as Viga:
                    print(Viga)
                finally:
                    server.quit()   
                    sbros = int(input("kirjutage kood "))
                while True:
                    if sbros == msg.set_content:
                        nimiIndeks = kasutajad.index(nimi)
                        uusParol = input("kirjutage uus parool ")
                        paroolid[nimiIndeks] = uusParol
                        break
                    else:
                        print("vale kood")
                break
            elif kiri == 2:
                print("te tühistasite parooli lähtestamise")
                break
            else:
                print("vale andmetüüp, provige veel üks kord")
    else:
        print("selle nimega kasutajat pole")

