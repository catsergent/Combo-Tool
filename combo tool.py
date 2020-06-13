import ctypes
import operator
import time
import re
import os
from tkinter.filedialog import askopenfilename
from datetime import datetime as date
import colorama
from colorama import Fore,Style
ctypes.windll.kernel32.SetConsoleTitleW("Combo editor")
Majuscule = ["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", 'M', 'W',
             "X", "C", "V", "B", "N"]
FILETYPES = [ ("text files", "*.txt") ]

def logo():
    print(Fore.RED+Style.BRIGHT+"""\                                                 
                                                                                               
 @@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@    @@@@@@      @@@@@@@   @@@@@@    @@@@@@   @@@       
@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@  @@@@@@@@  @@@@@@@@  @@@       
!@@       @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@       @@!    @@!  @@@  @@!  @@@  @@!       
!@!       !@!  @!@  !@! !@! !@!  !@   @!@  !@!  @!@       !@!    !@!  @!@  !@!  @!@  !@!       
!@!       @!@  !@!  @!! !!@ @!@  @!@!@!@   @!@  !@!       @!!    @!@  !@!  @!@  !@!  @!!       
!!!       !@!  !!!  !@!   ! !@!  !!!@!!!!  !@!  !!!       !!!    !@!  !!!  !@!  !!!  !!!       
:!!       !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!       !!:    !!:  !!!  !!:  !!!  !!:       
:!:       :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!       :!:    :!:  !:!  :!:  !:!   :!:      
 ::: :::  ::::: ::  :::     ::    :: ::::  ::::: ::        ::    ::::: ::  ::::: ::   :: ::::  
 :: :: :   : :  :    :      :    :: : ::    : :  :         :      : :  :    : :  :   : :: : :  
                                                                                               




 """+Style.RESET_ALL)
logo()
combo = askopenfilename(filetypes=FILETYPES)
file = open(combo, "r", encoding='utf8',errors='ignore')
try:
    lines = file.readlines()
except UnicodeDecodeError:
    print("There is character that arent accepted")
    a = input("press enter to quit")
    pass
save = "continue"




while save != "quit":
    print(str(len(lines)) + " lines got loaded")
    print(" 0) Quit")
    print(" 1) Replace letter by number ")
    print(" 2) Replace number by letter ")
    print(" 3) Upper the 1st character of the password ")
    print(" 4) Email to user ")
    print(" 5) User to email ")
    print(" 6) Domain changer")
    print(" 7) Add character at the end of pass")
    print(" 8) Add character at the beginning of the pass")
    print(" 9) Remove a character")
    print(" 10) Sorter A to Z")
    print(" 11) Extractor")
    print(" 12) Assembler")
    print(" 13) Line Splitter")
    print(" 14) Antiduplicate ")
    print(" 15) Combo optimiser (impossible password remover) ")
    print(" 16) Domain / extension splitter")
    print(" 17) Disassembler")
    print(" 18) Cleaner")
    print(" 19) Combiner")
    print(" 20) Capture remover")
    print(" 21) email:hash and hash:pass to email:pass")
    print(" 22) Email Name = pass")
    print(" 23) Email,Pass extractor")
    print(" 24) Capture sorter")
    choix1 = int(input(" Make your choice "))
    os.system('cls')
    if choix1 > 24:
        while choix1 > 24:
            choix1 = int(input("    Make your choice between 1 and 23 "))
    if choix1 == 1:
        path = "Letter to Number"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + "  " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/number.txt", "w")
        print(" 1) Replace letter everywhere")
        print(" 2) Replace letter in password")
        print(" 3) Replace letter in email(everything between @ and : will be keept")
        choix2 = int(input("1/2/3 ?"))
        print(" 1) Make difference between upper and lower case) ")
        print(" 2) Change every character (upper and lower case) ")
        choix3 = int(input("1/2 ? "))
        lettre = input("Choose the letter (1 only)")
        nombre = input("Choose the number (1 only)")
        print(" editing")
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').split(":")
            compte = line
            if len(compte) == 2:
                email = compte[0]
                pwd = compte[1]
                email = email.split("@")
                user = email[0]
                if choix3 == 1:
                    if choix2 == 1:
                        user = user.replace(lettre, nombre)
                        pwd = pwd.replace(lettre, nombre)
                    elif choix2 == 2:
                        pwd = pwd.replace(lettre, nombre)
                    elif choix2 == 3:
                        user = user.replace(lettre, nombre)
                    else:
                        while choix2 > 3:
                            choix2 = int(input("1/2/3 ?"))
                elif choix3 == 2:
                    if choix2 == 1:
                        user = user.replace(lettre.lower(), nombre).replace(lettre.upper(), nombre)
                        pwd = pwd.replace(lettre.lower(), nombre).replace(lettre.upper(), nombre)
                    elif choix2 == 2:
                        pwd = pwd.replace(lettre.lower(), nombre).replace(lettre.upper(), nombre)
                    elif choix2 == 3:
                        user = user.replace(lettre.lower(), nombre).replace(lettre.upper(), nombre)
                    else:
                        while choix2 > 3:
                            choix2 = int(input("1/2/3 ?"))
                else:
                    while choix3 > 2:
                        choix3 = int(input("1/2 ? "))
                email[0] = user
                compte[0] = str(email).replace("['", "").replace("', '", "@").replace("']", "")
                compte[1] = pwd
                compte = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                file1.write(str(compte) + '\n')
        print(" Done result save in " + path)
    elif choix1 == 2:
        path = "Number to letter"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/letter.txt", "w")
        print(" 1) Replace number everywhere")
        print(" 2) Replace number in password")
        print(" 3) Replace number in email(everything between @ and : will be keept")
        choix2 = int(input("1/2/3 ?"))
        lettre = input("Choose the letter ")
        nombre = input("Choose the number ")
        print(" editing")
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').split(":")
            compte = line
            if len(compte) == 2:
                email = compte[0]
                pwd = compte[1]
                email = email.split("@")
                user = email[0]
                domaine = email[1]
                if choix2 == 1:
                    user = user.replace(nombre, lettre)
                    pwd = pwd.replace(nombre, lettre)
                elif choix2 == 2:
                    pwd = pwd.replace(nombre, lettre)
                elif choix2 == 3:
                    user = user.replace(nombre, lettre)
                else:
                    while choix2 > 3:
                        choix2 = int(input("1/2/3 ?"))
                email[0] = user
                compte[0] = str(email).replace("['", "").replace("', '", "@").replace("']", "")
                compte[1] = pwd
                compte = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                file1.write(str(compte) + '\n')
        print(" Done result save in " + path)
    elif choix1 == 3:
        path = "Upper"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/Upper.txt", "w")
        print(" editing")
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').split(":")
            compte = line
            if len(compte) == 2:
                compte[1] = compte[1].title()
                compte = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                file1.write(str(compte) + '\n')
        print(" Done result save in " + path)
    elif choix1 == 4:
        path = "Email to user"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/User.txt", "w")
        print(" editing")
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').split(":")
            compte = line
            if len(compte) == 2:
                email = compte[0]
                email = email.split("@")
                email = email[0]
                compte[0] = email
                compte = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                file1.write(str(compte) + '\n')
        print(" Done result save in " + path)
    elif choix1 == 5:
        path = "User to Email"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/user to Email.txt", "w")
        domain = input("what domain name you want ? (example @gmail.com) ")
        print(" editing")
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').split(":")
            compte = line
            if len(compte) == 2:
                user = compte[0]
                email = user + domain
                compte[0] = email
                compte = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                file1.write(str(compte) + '\n')
        print(" Done result save in " + path)
    elif choix1 == 6:
        path = "Domain Changer"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/Domain changer.txt", "w")
        print(" 1) Change specifique domain ")
        print(" 2) Change every domain")
        aa = int(input(" Choose "))
        if aa > 2:
            while aa > 2:
                aa = int(input(" Choose "))
        elif aa == 1:
            domain1 = input("Domain to be change (example gmail.com) ")
            domain2 = input("Domain to change to (example hotmail.com) ")
            print(" editing")
            for i in range(0, len(lines)):
                line = lines[i]
                line = line.rstrip('\n').split(":")
                compte = line
                if len(compte) == 2:
                    email = compte[0]
                    pwd = compte[1]
                    email = email.split("@")
                    user = email[0]
                    domaine = email[1]
                    if str(domaine) == str(domain1):
                        domaine = domain2
                        email[1] = domaine
                        email = str(email).replace("['", "").replace("', '", "@").replace("']", "")
                        compte = str(email) + ":" + str(compte[1])
                        file1.write(str(compte) + '\n')
                print(" Done result save in " + path)
        elif aa == 2:
                domain2 = input("Domain to change to (example hotmail.com) ")
                print(" editing")
                for i in range(0, len(lines)):
                    line = lines[i]
                    line = line.rstrip('\n').split(":")
                    compte = line
                    if len(compte) == 2 and len(compte[0]) > 0 and len(compte[1]) > 1:
                        email = compte[0]
                        pwd = compte[1]
                        email = email.split("@")
                        user = email[0]
                        domaine = email[1]
                        domaine = domain2
                        email[1] = domaine
                        email = str(email).replace("['", "").replace("', '", "@").replace("']", "")
                        compte = str(email) + ":" + str(compte[1])
                        file1.write(str(compte) + '\n')
                print(" Done result save in " + path)
        file1.close()
    elif choix1 == 7:
        path = "Suffix"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/Suffix.txt", "w")
        suffix = input("What do you want to add at the end of the password ")
        print(" editing")
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').split(":")
            compte = line
            if len(compte) == 2:
                pwd = compte[1]
                pwd = pwd + suffix
                compte[1] = pwd
                compte = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                file1.write(str(compte) + '\n')
        print(" Done result save in " + path)
    elif choix1 == 8:
        path = "Prefix"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/prefix.txt", "w")
        suffix = input("What do you want to add at the begining of the password ")
        print(" editing")
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').split(":")
            compte = line
            if len(compte) == 2:
                pwd = compte[1]
                pwd = suffix + pwd
                compte[1] = pwd
                compte = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                file1.write(str(compte) + '\n')
        print(" Done result save in " + path)
    elif choix1 == 9:
        path = "Remover"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/removed.txt", "w")
        letter = input("what letter you want to remove")
        print(" editing")
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').replace(letter, "")
            file1.write(str(line) + '\n')
        print(" Done result save in " + path)
    elif choix1 == 10:
        path = "Sorted A to Z"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        print(" 1) Sort A to Z")
        print(" 2) Sort A to Z by domaine ")
        print(" 3) Sort A to Z by extension ")
        print(" 4) Sort A to Z by paswword")
        choix4 = int(input("Make your choice "))
        print(" editing")
        if choix4 == 1:
            lines.sort()
            file1 = open(path + "/Sorted A to Z.txt", "w")
            file1.write("".join(lines))
            file1.close()
        elif 5 < choix4 > 1:
            autre_liste = []
            for i in range(0, len(lines)):
                line = lines[i]
                line = line.rstrip('\n').split(":")
                compte = line
                if len(compte) == 2:
                    email = compte[0]
                    email = email.split("@")
                    pwd = compte[1]
                    user = email[0]
                    domaine = email[1]
                    domaines = domaine.split(".")
                    extension = domaines[1]
                    if choix4 == 2:
                        autre_liste.append([compte[0] + ":" + pwd, domaine])
                    if choix4 == 3:
                        autre_liste.append([compte[0] + ":" + pwd, extension])
                    if choix4 == 4:
                        autre_liste.append([compte[0] + ":" + pwd, pwd])
            autre_liste = sorted(autre_liste, key=operator.itemgetter(1))
            file1 = open(path + "/Sorted A to Z.txt", "w")
            file1.write("".join(autre_liste))
            file1.close()
            print(" Done result save in " + path)
    elif choix1 == 11:
        path = "Extracted"
        print(" 1) Extract every line with the character" )
        print(" 2) Extract every line without the character")
        choix2 = int(input("Make your choice "))
        if choix2 > 2:
            while choix2 > 2:
                choix2 = int(input("Make your choice "))
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        fichier1 = open(path + "/Extracted.txt", "w")
        print(" 1) Define manually")
        print(" 2) Use preset")
        choix3 = int(input(" Make your choice "))
        if choix3 > 2:
            while choix3 > 2:
                choix3 = int(input(" Make your choice "))
        elif choix3 == 1:
            extr1 = input("What do you want extract (gonna extract every line with ure quiery) ")
            extr = []
            extr.append(extr1)
            extr1 = input("Do you want to put an other quiery? (if no type endee) dont use if you want to use ")
            extr.append(extr1)
            if extr1 != "endee":
                while extr1 != "endee":
                    extr1 = input("Do you want to put an other quiery? (if no type endee) ")
                    if extr1 not in extr:
                        extr.append(extr1)
                    else:
                        print("this is already in the list")
                        print(str(extr))
                else:
                    extr.remove(extr[-1])
        if choix3 == 2:
            extr = []
            combo1 = askopenfilename(filetypes=FILETYPES)
            file2 = open(combo1, "r", encoding='utf8', errors='ignore')
            extr = file2.readlines()
            for a in range(0,len(extr)):
                extr[a] = extr[a].rstrip("\n")
        if choix2 == 1:
            print(str(extr))
            print(len(extr))
            for i in range(0, len(lines)):
                line = lines[i]
                for a in range (0,len(extr)):
                     if extr[a] in line:
                         fichier1.write(line)
        elif choix2 == 2:
            list2 = []
            for i in range(0, len(lines)):
                line = lines[i]
                if extr[0] not in line:
                    list2.append(line)
            for a in range (0,len(extr)):
                for i in range(0, len(list2)):
                    line = list2[i]
                    if extr[a] not in line:
                        list2.append(line)
            fichier1.write("".join(list2))
        fichier1.close()
        print(" Done result save in " + path)
    elif choix1 == 12:
        path = "Assembler"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        fichier4 = open(path + "/Assembled.txt", "w")
        combo1 = askopenfilename(filetypes=FILETYPES)
        combo2 = askopenfilename(filetypes=FILETYPES)
        separator = input("choose the separator ")
        fichier2 = open(combo1, "r")
        fichier3 = open(combo2, "r")
        print("Processing")
        try:
            lines1 = fichier2.readlines()
        except UnicodeDecodeError:
            print("There is character that arent accepted")
            a = input("press enter to quit")
            pass
        try:
            lines2 = fichier3.readlines()
        except UnicodeDecodeError:
            print("There is character that arent accepted")
            a = input("press enter to quit")
            pass
        if len(lines1) >= len(lines2):
            for i in range(0, len(lines1)):
                fichier4.write(lines1[i] + separator + lines2[i])
        elif len(lines2) > len(lines1):
            for i in range(0, len(lines2)):
                fichier4.write(lines1[i] + separator + lines2[i])
        print(" Done result save in " + path)
    elif choix1 == 13:
        path = "Splitter"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        print(" 1) Split per X line")
        print(" 2) Split in X file")
        liste = []
        a = 0
        linemax = 0
        choix2 = int(input("Make your choice "))
        if choix2 == 1:
            linemax = int(input("How many line per file "))
        if choix2 == 2:
            filemax = int(input("How many file "))
            linemax = int(len(lines) / filemax)
        for i in range(0, len(lines)):
            line = lines[i]
            liste.append(line)
            e = len(lines) - i
            if len(liste) == linemax:
                a = a + 1
                file2 = open(path + "/Split " + str(a) + ".txt", "w")
                file2.write("".join(liste))
                liste = []
        if e < linemax:
            a = a + 1
            file2 = open(path + "/Split" + str(a) + ".txt", "w")
            file2.write("".join(liste))
            file2.close()
            liste = []
        print(" Done result save in " + path)
    elif choix1 == 14:
        path = "Antiduplicate"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
            file1 = open(path + "/Antiduplicate.txt", "w")
            file2 = open(path + "/Duplicate.txt", "w")
            antidupe = []
            dupe = []
            ant = 0
            dup = 0
            print("Processing ")
            print("Do you want totaly remove the duplicate or keep at least one of them ?")
            choix22 = int(input("1 = Keep at least one of the duplicate in the antidupe file" + "\n" + "2 = If a line is duplicate its gonna get totaly remove from antidupe (take more time)" + "\n" + "Make your choice "))
            if choix22 > 2:
                while choix22 > 2:
                     choix22 = int(input("Make your choice between 1 and 2 "))
            debut = time.time()
            if choix22 == 1:
                for i in range(0, len(lines)):
                    line = lines[i]
                    line = line.rstrip('\n')
                    if line not in antidupe:
                        antidupe.append(line)
                        ant += 1
                    else:
                        dupe.append(line)
                        dup += 1
                if i > 0:
                    centage = i / len(lines) * 100
                else:
                    centage = 0
                ctypes.windll.kernel32.SetConsoleTitleW("Good | " + str(ant) + " Duplicate | " + str(dup) + " " + str(round(centage)) + "% " + "Left : " + str(len(lines) - i))

            if choix22 == 2:
                antidupe1 = []
                for i in range(0, len(lines)):
                    line = lines[i]
                    line = line.rstrip('\n')
                    if line not in antidupe1:
                        antidupe1.append(line)
                    else:
                        dupe.append(line)
                        dup += 1
                for i in range(0,len(antidupe1)):
                    line = antidupe1[i]
                    if line in dupe:
                        pass
                    else:
                        antidupe.append(line)
                        ant += 1
                if i > 0:
                    centage = i / len(lines) * 100
                else:
                    centage = 0
            ctypes.windll.kernel32.SetConsoleTitleW("Good | " + str(ant) + " Duplicate | " + str(dup) + " " + str(round(centage)) + "% " + "Left : " + str(len(lines) - i))
        antidupe = str(antidupe).replace("['", "").replace("', '", "\n").replace("']", "")
        file1.write(str(antidupe))
        file2.write("".join(dupe))
        file1.close()
        file2.close()
        fin = time.time()
        print(str(fin - debut))
        ant = len(lines) - ant
        print(str(ant) + " duplicate removed")
    elif choix1 == 15:
        path = "Impossible password optimiser"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        file1 = open(path + "/good.txt", "w")
        fichierbad = open(path + "/removed.txt", "w")
        fichier = open("result.txt", "w")
        Maj = int(input('Does it need to have at least one Uppercase ? 1 = yes 2 = no '))
        Num = int(input('Does it need to have at least one number? 1 = yes 2 = no '))
        lene = int(input("Minimum lenght of the password "))
        debut = time.time()
        good = 0
        bad = 0
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').split(":")
            compte = line
            if len(compte) == 2:
                mot = compte[1]
                if Maj == 1 and Num == 1:
                    x = re.findall('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).(?=.*?[0-9]).{1,}$', mot)
                elif Maj == 1 and Num != 1:
                    x = re.findall('^(?=.*?[A-Z])(?=.*?[a-z]).{1,}$', mot)
                elif Maj != 1 and Num == 1:
                    x = re.findall('^(?=.*?[a-z]).(?=.*?[0-9]).{1,}$', mot)
                else:
                    x = str(re.findall('^(?=.*?[a-z]).{1,}$', mot))
                if len("".join(x)) > lene:
                    comptes = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                    file1.write(str(comptes) + '\n')
                    good = good + 1
                else:
                    bad = bad + 1
                    comptes = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                    fichierbad.write(str(comptes) + '\n')
                if i > 0:
                    centage = i / len(lines) * 100
                else:
                    centage = 0
                ctypes.windll.kernel32.SetConsoleTitleW("Good | " + str(good) + " removed | " + str(bad) + " " + str(round(centage)) +  "% " + "Left : " + str(len(lines) - i))
        fichier.close()
        fichierbad.close()
        file1.close()
        print(("Good | " + str(good) + " removed | " + str(bad)))
        fin = time.time()
        temps = fin - debut
        print(str(len(lines)) + " compte on etait checker en " + str(temps) + " sec ")
    elif choix1 == 16:
        path = "Sorter v2"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        extensions = []
        domainess = []
        print(" 1) Sort per extension")
        print(" 2) Sort per domaine")
        choix5 = int(input("Make your choice "))
        if choix5 == 1:
            path = path + "/Extension/"
            if not os.path.exists(path):
                os.mkdir(path)
            for i in range(0, len(lines)):
                line = lines[i]
                line = line.rstrip('\n').split(":")
                compte = line
                if len(compte) == 2:
                    email = compte[0]
                    email = email.split("@")
                    pwd = compte[1]
                    user = email[0]
                    if len(email) == 2:
                        domaine = email[1]
                        domaines = domaine.split(".")
                        if len(domaines) == 2:
                            extension = domaines[1]
                        elif len(domaines) == 3:
                            extension = domaine[1] + domaine[2]
                        else:
                            continue
                        if extension not in extensions:
                            extensions.append(extension)
                            file1 = open(path + extension + ".txt", "w")
                            comptes = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                            file1.write(str(comptes) + "\n")
                            file1.close()
                        else:
                            file1 = (open(path+ extension + ".txt", "a"))
                            comptes = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                            file1.write(str(comptes) + "\n")
                            file1.close()
                        if i > 0:
                            centage = i / len(lines) * 100
                        else:
                            centage = 0
                        ctypes.windll.kernel32.SetConsoleTitleW("Extension | " + str(len(extensions)) + str(round(centage)) + "% " + "Left : " + str(len(lines) - i))
        elif choix5 == 2:
            path = path + "/Domaine/"
            if not os.path.exists(path):
                os.mkdir(path)
            for i in range(0, len(lines)):
                    line = lines[i]
                    line = line.rstrip('\n').split(":")
                    compte = line
                    if len(compte) == 2:
                        email = compte[0]
                        email = email.split("@")
                        pwd = compte[1]
                        user = email[0]
                        if len(email) == 2:
                            domaine = email[1]
                        else:
                            continue
                        if domaine not in domainess:
                            domainess.append(domaine)
                            file2 = open(path + domaine + ".txt", "w")
                            comptes = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                            file2.write(str(comptes) + "\n")
                            file2.close()
                        else:
                            file2 = (open(path + domaine + ".txt", "a"))
                            comptes = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                            file2.write(str(comptes) + "\n")
                            file2.close()
                        if i > 0:
                            centage = i / len(lines) * 100
                        else:
                            centage = 0
                        ctypes.windll.kernel32.SetConsoleTitleW("Domaines | " + str(len(domainess)) + "   " + str(round(centage)) + "% " + " Left : " + str(len(lines) - i))
        print(" Done result save in " + path)
    elif choix1 == 17:
        print(" delimiter is :")
        path = "Disassembler"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        fichier5 = open(path + "/Left.txt", "a")
        fichier6 = open(path + "/Right.txt", "a")
        for i in range(0, len(lines)):
            line = lines[i]
            compte = line.rstrip('\n').split(":")
            if len(compte) == 2:
                left = str(compte[0]) + "\n"
                right = str(compte[1]) + "\n"
                fichier5.write(left)
                fichier6.write(right)
        fichier5.close()
        fichier6.close()
    elif choix1 == 18:
        print(" This tool gonna remove line that dosnt have : ")
        path = "Cleaner"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        fichier5 = open(path + "/Good.txt", "w")
        fichier6 = open(path + "/Bad.txt", "w")
        good = 0
        bad = 0
        for i in range(0, len(lines)):
            line = lines[i]
            compte = line.rstrip('\n').split(":")
            if len(compte) == 2:
                fichier5.write(":".join(compte) + "\n")
                good = good + 1
            else:
                fichier6.write(":".join(compte) + "\n")
                bad = bad + 1
        fichier5.close()
        fichier6.close()
        print(" Result in Cleaner there is " + str(good) + " good lines and " + str(bad) + " bad lines" )
    elif choix1 == 19:
        print(" This tool gonna combine several combo into one file ")
        path = "Combiner"
        if not os.path.exists(path):
            os.mkdir(path)
        print("Choose your combo (Ps the combo you choose at first wont be combined )")
        combo = askopenfilename(filetypes=FILETYPES)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        result = open(path + "/combined.txt","w")
        combo1 = open(combo,"r")
        result.write("".join(combo1) + "\n")
        end = "end"
        num = 0
        combos = [combo]
        num2 = 1
        while num != 1:
            num = int(input("if you want to stop type 1 else type any other number "))
            if num != 1:
                num2 = num2 + 1
                print(" Ok you gonna add combo number : " + str(num2))
                combo = askopenfilename(filetypes=FILETYPES)
                if combo not in combos:
                    combo1 = open(combo,"r")
                    result.write("".join(combo1) + "\n")
                    combos.append(combo)
                else:
                    print(" you already put a combo with that name")
                    print(" ".join(combos))
                    num2 = num2 - 1
        result.close()
        combo1.close()
        print(" Done result save in " + path)
    elif choix1 == 20:
        path = "Capture remover"
        if not os.path.exists(path):
            os.mkdir(path)
        b = input("choose ure seperator")
        a = int(input("in what position the account ? start at 0 "))
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        fichier5 = open(path + "/result.txt", "w")
        print("Processing capture remover")
        for i in range(0, len(lines)):
            line = lines[i]
            compte = line.rstrip('\n').split(b)
            if len(compte) >= a + 1:
                comptes = compte[a]
                fichier5.write(comptes + "\n")
            else:
                print("error at line " + i)
        fichier5.close()
        print(" Done result save in " + path)
    elif choix1 == 21:
        path = "Comparator"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        fichier5 = open(path + "/in.txt", "w",  encoding='utf8',errors='ignore')
        fichier6 = open(path + "/not-in.txt","w", encoding='utf8',errors='ignore')
        print("Choose the hash:pass")
        combo1 = askopenfilename(filetypes=FILETYPES)
        file1 = open(combo1, "r",encoding='utf8',errors='ignore' )
        lines2 = file1.readlines()
        list3 = []
        list4 = []
        i = -1
        a = -1
        f = 0
        y = 0
        print("comparing")
        while a != len(lines2):
            i = i + 1
            a = a + 1
            if a < len(lines2):
                line11 = lines[i]
                line22 = lines2[a]
                line1 = line11.rstrip('\n').split(":")
                line2 = line22.rstrip('\n').split(":")
                if len(line1) == 2 and len(line2) == 2:
                    if line1[1] == line2[0]:
                        list3.append(line1[0] + ":" + line2[1])
                        y = y +1
                    else:
                        a = a - 1
                        list4.append(line11)
                        f = f + 1
                else:
                    pass
        fichier5.write("\n".join(list3))
        fichier6.write("".join(list4))
        fichier5.close()
        fichier6.close()
        print(str(y) + " got found and " + str(f) + " are not in the list")
    elif choix1 == 22:
        path = "Email Name to pass"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        fichier5 = open(path + "/result.txt", "w", encoding='utf8', errors='ignore')
        fichier = file
        for i in range(0, len(lines)):
            line = lines[i]
            line = line.rstrip('\n').split(":")
            compte = line
            if len(compte) == 2:
                email = compte[0]
                email = email.split("@")
                user = email[0]
                compte[1] = user
                fichier5.write(":".join(compte) + "\n")
    elif choix1 == 23:
        path = "Email,Pass extractor"
        if not os.path.exists(path):
            os.mkdir(path)
        print(" 1) Email")
        print(" 2) Pass")
        choix2 = int(input(" Make your choice"))
        if choix2 == 1:
            path = path + "/Email"
            if not os.path.exists(path):
                os.mkdir(path)
            path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
            if not os.path.exists(path):
                os.mkdir(path)
            fichier5 = open(path + "/email.txt", "w", encoding='utf8', errors='ignore')
        elif choix2 == 2:
            path = path + "/Pass"
            if not os.path.exists(path):
                os.mkdir(path)
            path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + " " + str(date.now().hour) + "h" + str(date.now().minute))
            if not os.path.exists(path):
                os.mkdir(path)
            fichier5 = open(path + "/email.txt", "w", encoding='utf8', errors='ignore')
        else:
            while choix2 > 2:
                choix2 = int(input(" Make your choice between 1 and 2"))
        if choix2 == 1:
            for i in range(0, len(lines)):
                line = lines[i]
                line = line.rstrip('\n').split(":")
                compte = line
                if len(compte) == 2:
                    email = compte[0]
                    fichier5.write(email + "\n")
        if choix2 == 2:
            for i in range(0, len(lines)):
                line = lines[i]
                line = line.rstrip('\n').split(":")
                compte = line
                if len(compte) == 2:
                    email = compte[1]
                    fichier5.write(email + "\n")
        print(" Done result save in " + path)
    elif choix1 == 24:
        path = "Capture sorter"
        if not os.path.exists(path):
            os.mkdir(path)
        path = (path + "/Result " + str(date.now().day) + "-" + str(date.now().month) + "-" + str(date.now().year) + "  " + str(date.now().hour) + "h" + str(date.now().minute))
        if not os.path.exists(path):
            os.mkdir(path)
        splite = input("Choose the separtor ")
        place = int(input("Choose the position of capture (exemple account | sucription | country to sort by country it number 2) "))
        extensions = []
        print("Processing")
        for i in range(0,len(lines)):
            line = lines[i]
            compte = line.rstrip('\n').split(splite)
            extension = compte[place]
            if extension not in extensions:
                extensions.append(extension)
                file1 = open(path  + "\ " + extension + "X 1" + ".txt", "w")
                file1.write(splite.join(compte) + "\n")
                file1.close()
            else:
                file1 = (open(path + "\ " + extension + "X 1" + ".txt", "a"))
                file1.write(splite.join(compte) + "\n")
                xx = len(file1)
                os.rename(path + "\ " + extension + "X 1" + ".txt", "")
                file1.close()
        print(" Done result save in " + path)
    save = input("Type quit (without cap) to quit else type continue ")
    if save != "quit":
        cob = input("Do you want to choose an other combo? Y / N ")
        if cob == "Y":
            combo = askopenfilename(filetypes=FILETYPES)
            file = open(combo, "r", encoding='utf8', errors='ignore')
            try:
                lines = file.readlines()
            except UnicodeDecodeError:
                print("There is character that arent accepted")
                a = input("press enter to quit")
                pass
    os.system('cls')
aaaaaaa = input("press enter to quit")
