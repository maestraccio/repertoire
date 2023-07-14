#!/usr/bin/env python3
import ast, os

versie = "1.21"
datum = "20230702"
plaats = "Pedara"

basismap = os.path.dirname(os.path.realpath(__file__)) # de map waar het pythonscript in staat moet schrijfbaar zijn
os.chdir(basismap)

inputindent = "    : "
forc3 = "{:^3}".format
forr3 = "{:>3}".format
forc4 = "{:^4}".format
forl5 = "{:<5}".format
forl8 = "{:<8}".format
forl15 = "{:<15}".format
forl30 = "{:<30}".format

afsluitlijst = ["X","Q"]
tiklijst = ["3","4","A"]
toonlijst = ["A","B","C","D","E","F","G"]

def getstyle():
    try:
        with open("Stijlen","r") as s:
            stijllijst = ast.literal_eval(s.read())
    except:
        stijllijst = []
    stijllijst = sorted(stijllijst)
    return stijllijst

def gettrack():
    try:
        with open("Repertoire","r") as r:
            repertoirelijst = ast.literal_eval(r.read())
    except(Exception) as error:
        print(error)
        repertoirelijst = []
    repertoirelijst = sorted(repertoirelijst)
    return repertoirelijst

def showstyle():
    stijllijst = getstyle()
    repertoirelijst = gettrack()
    toonstijllijst = []
    stijlindex = 0
    for i in stijllijst:
        tracks = 0
        for j in repertoirelijst:
            if i == j[0]:
                tracks += 1
        stijlindex += 1
        toonstijllijst.append(stijlindex)
        print(forr3(str(stijlindex))+" : "+forl15(i)+str(tracks))
    stijllijst = sorted(stijllijst)
    return stijllijst,toonstijllijst

def showtrack():
    stukje = input("Geef een stukje van de titel op, of meerdere, gescheiden door komma's:\n%s" % inputindent).strip().replace(" ,",",").replace(", ",",").replace("'","").replace("’","").replace(".","").replace("-","").replace("_","").replace("?","").replace("!","").replace(" ","").split(",")
    if stukje[0].upper() in afsluitlijst:
        return
    stijltje = input("Geef een stukje van de stijl op, of meerdere, gescheiden door komma's:\n%s" % inputindent).replace(" ","").split(",")
    if stijltje[0].upper() in afsluitlijst:
        return
    maatje= input("Geef een stukje van de maatsoort op, of meerdere, gescheiden door komma's:\n%s" % inputindent).split(",")
    if maatje[0].upper() in afsluitlijst:
        return
    toontje= input("Geef een stukje van de toonsoort op, of meerdere, gescheiden door komma's:\n%s" % inputindent).split(",")
    if toontje[0].upper() in afsluitlijst:
        return
    repertoirelijst = gettrack()
    toontracklijst = []
    trackindex = 0
    trackcount = 0
    eenoftwee = input("Wil je de output in 1, 2 of 3 kolommen:\n%s" % inputindent)
    if eenoftwee.upper() in afsluitlijst:
        return
    elif eenoftwee == "1":
        with open("Repertoirelijst.txt","w") as r:
            for i in repertoirelijst:
                trackindex += 1
                for j in stukje:
                    for k in stijltje:
                        for l in maatje:
                            for m in toontje:
                                if k.lower() in i[0].lower() and j.lower() in i[1].lower() and l.lower() in i[2].lower() and m.lower() in i[3].lower():
                                    if trackcount % 42 == 0:
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"))
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"),file = r)
                                        print(forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON"))
                                        print(forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON"),file = r)
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"))
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"),file = r)
                                    print(forr3(str(trackindex))+" : "+forl15(i[0][:15])+forl30(i[1][:30])+forc4(i[2])+forl5(i[3]))
                                    print(forr3(str(trackindex))+" : "+forl15(i[0][:15])+forl30(i[1][:30])+forc4(i[2])+forl5(i[3]),file = r)
                                    toontracklijst.append(trackindex)
                                    trackcount += 1
            print("Aantal tracks : %s" % trackcount)
    elif eenoftwee == "2":
        with open("Repertoirelijst.txt","w") as r:
            breed = []
            for i in repertoirelijst:
                trackindex += 1
                for j in stukje:
                    for k in stijltje:
                        for l in maatje:
                            for m in toontje:
                                if k.lower() in i[0].lower() and j.lower() in i[1].lower() and l.lower() in i[2].lower() and m.lower() in i[3].lower():
                                    if trackcount % 42 == 0:
                                        print()
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"))
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"),file = r)
                                        print(forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON")+"\\"+forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON"))
                                        print(forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON")+"\\"+forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON"),file = r)
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"), end = "")
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"),file = r, end = "")
                                    if trackcount == 0:
                                        print()
                                    if len(breed) == 0:
                                        if trackcount > 0:
                                            print("\\", end = "")
                                            print("\\", end = "",file = r)
                                    elif len(breed) == 1 and i[0] == breed[0][0]:
                                        print("\\", end = "")
                                        print("\\", end = "",file = r)
                                    else:
                                        print()
                                        print("",file = r)
                                        breed = []
                                    print(forr3(str(trackindex))+" : "+forl15(i[0][:15])+forl30(i[1][:30])+forc4(i[2])+forl5(i[3]),end = "")
                                    print(forr3(str(trackindex))+" : "+forl15(i[0][:15])+forl30(i[1][:30])+forc4(i[2])+forl5(i[3]),end = "",file = r)
                                    trackcount += 1
                                    breed.append(i)
                                    toontracklijst.append(trackindex)
            print()
            print("Aantal tracks : %s" % trackcount)
            print("Aantal tracks : %s" % trackcount,file = r)
    elif eenoftwee == "3":
        with open("Repertoirelijst.txt","w") as r:
            breed = []
            for i in repertoirelijst:
                trackindex += 1
                for j in stukje:
                    for k in stijltje:
                        for l in maatje:
                            for m in toontje:
                                if k.lower() in i[0].lower() and j.lower() in i[1].lower() and l.lower() in i[2].lower() and m.lower() in i[3].lower():
                                    if trackcount % 42 == 0:
                                        print()
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"))
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"),file = r)
                                        print(forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON")+"\\"+forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON")+"\\"+forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON"))
                                        print(forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON")+"\\"+forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON")+"\\"+forr3("ID")+" : "+forl15("STIJL")+forl30("TITEL")+forc4("TIK")+forl5("TOON"),file = r)
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"))
                                        print(forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(5*"-")+"\\"+forr3("+"+2*"-")+"-+-"+forl15(14*"-"+"+")+forl30(29*"-"+"+")+forc4(3*"-"+"+")+forl5(4*"-"+"+"),file = r)
                                    if len(breed) == 0:
                                        if trackcount > 0:
                                            print("\\", end = "")
                                            print("\\", end = "",file = r)
                                    elif len(breed) == 1 and i[0] == breed[0][0]:
                                        if trackcount % 42 == 0:
                                            pass
                                        else:
                                            print("\\", end = "")
                                            print("\\", end = "",file = r)
                                    elif len(breed) == 2 and i[0] == breed[1][0] and trackcount % 42 != 0:
                                        print("\\", end = "")
                                        print("\\", end = "",file = r)
                                    else:
                                        if trackcount % 42 == 0:
                                            pass
                                        else:
                                            print()
                                            print("",file = r)
                                        breed = []
                                    print(forr3(str(trackindex))+" : "+forl15(i[0][:15])+forl30(i[1][:30])+forc4(i[2])+forl5(i[3]),end = "")
                                    print(forr3(str(trackindex))+" : "+forl15(i[0][:15])+forl30(i[1][:30])+forc4(i[2])+forl5(i[3]),end = "",file = r)
                                    trackcount += 1
                                    breed.append(i)
                                    toontracklijst.append(trackindex)
            print()
            print("Aantal tracks : %s" % trackcount)
            print("Aantal tracks : %s" % trackcount,file = r)
    repertoirelijst = sorted(repertoirelijst)
    return repertoirelijst,toontracklijst

def newstyle():
    stijllijst = showstyle()[0]
    stil = True
    while stil == True:
        stijla = input("Geef een nieuwe stijl op:\n%s" % inputindent).strip()
        if stijla.upper() in afsluitlijst:
            return
        elif stijla == "":
            pass
        else:
            stijlb = stijla.split(" ")
            stijlc = []
            stijl = ""
            for i in stijlb:
                stijlc.append(i.capitalize())
            for i in stijlc:
                stijl += i
            if stijl not in stijllijst:
                stijllijst.append(stijl.replace(" ",""))
                stijllijst = sorted(stijllijst)
                with open("Stijlen","w") as s:
                    print(stijllijst, end = "", file = s)
                stil = False

def newtrack():
    tit = True
    while tit == True:
        repertoirelijst = gettrack()
        tracklijst = []
        for i in repertoirelijst:
            tracklijst.append(i[1].lower())
        titela = input("Geef de titel van de track:\n%s" % inputindent).strip().replace("'","").replace("’","").replace(",","").replace(".","").replace("-","").replace("_","").replace("?","").replace("!","")
        if titela.upper() in afsluitlijst:
            return
        elif titela == "":
            pass
        else:
            titelb = titela.split(" ")
            titelc = []
            titel = ""
            for i in titelb:
                titelc.append(i.capitalize())
            for i in titelc:
                titel += i
            if titel.lower() in tracklijst:
                print("Titel bestaat al.")
                return
            else:
                tit = False
    style = False
    while style == False:
        print("in stijl")
        stijllijst = showstyle()[0]
        stijl = input(inputindent)
        if stijl.upper() in afsluitlijst:
            return
        try:
            if len(stijllijst) < int(stijl) or int(stijl) < 1:
                print("Dat kan niet")
            else:
                style = True
        except:
            print("Geef het nummer op")
    tak = True
    while tak == True:
        tik = input("in 3, 4 of \"A\"nders:\n%s" % inputindent).upper()
        if tik.upper() in afsluitlijst:
            return
        elif tik not in tiklijst:
            print("3, 4 of \"A\"")
        else:
            tak = False
    doof = True
    while doof == True:
        toon = input("in toonsoort:\n%s" % inputindent).replace(" ","").replace("ineur","").replace("majeur","").replace("inor","").replace("major","")
        if toon.upper() in afsluitlijst:
            return
        elif toon == "":
            pass
        elif toon[0].upper() not in toonlijst:
            pass
        else:
            toon = toon.capitalize()
            doof = False
    nieuwetrack = [stijllijst[int(stijl)-1],titel,tik,toon]
    repertoirelijst = gettrack()
    repertoirelijst.append(nieuwetrack)
    repertoirelijst = sorted(repertoirelijst)
    with open("Repertoire","w") as r:
        print(repertoirelijst, file = r)

def changestyle():
    lijsten = showstyle()
    stijllijst = lijsten[0]
    toonstijllijst = lijsten[1]
    welke = input("Welke stijl wil je wijzigen:\n%s" % inputindent)
    if welke.upper() in afsluitlijst:
        return
    try:
        if int(welke) in toonstijllijst:
            stijla = input("Geef deze stijl een nieuwe naam:\n%s" % inputindent).strip()
            if stijla.upper() in afsluitlijst:
                return
            elif stijla == "":
                pass
            else:
                stijlb = stijla.split(" ")
                stijlc = []
                stijl = ""
                for i in stijlb:
                    stijlc.append(i.capitalize())
                for i in stijlc:
                    stijl += i
                stijllijst[int(welke)-1] = stijl
                stijllijst = sorted(stijllijst)
                with open("Stijlen","w") as s:
                    print(stijllijst, end = "", file = s)
        else:
            print("Dat indexnummer staat niet in de lijst.")
    except(Exception) as error:
        print("Typ een geldig indexnummer (getal)")

def changetrack():
    tracklijsten = showtrack()
    repertoirelijst = tracklijsten[0]
    toontracklijst = tracklijsten[1]
    welke = input("Welke track wil je wijzigen:\n%s" % inputindent)
    if welke.upper() in afsluitlijst:
        return
    try:
        if int(welke) in toontracklijst:
            wat = input("Wat wil je hieraan wijzigen:\n  1 : Stijl\n  2 : Naam\n  3 : Maatsoort\n  4 : Toonsoort\n%s" % inputindent)
            if wat.upper() in afsluitlijst:
                return
            elif wat == "1":
                stil = True
                while stil == True:
                    print("Kies een nieuwe stijl:")
                    stijllijsten = showstyle()
                    stijllijst = stijllijsten[0]
                    toonstijllijst = stijllijsten[1]
                    welkestijl = input(inputindent)
                    if welkestijl.upper() in afsluitlijst:
                        return
                    elif welkestijl == "":
                        pass
                    else:
                        try:
                            if len(stijllijst) < int(welkestijl) or int(welkestijl) < 1:
                                print("Dat indexnummer staat niet in de lijst.")
                            else:
                                repertoirelijst[int(welke)-1][0] = stijllijst[int(welkestijl)-1]
                                with open("Repertoire", "w") as r:
                                    print(repertoirelijst, end = "", file = r)
                                stil = False
                        except(Exception) as error:
                            print("Typ een geldig indexnummer (getal)")
            elif wat == "2":
                tit = True
                while tit == True:
                    titela = input("Corrigeer de naam:\n%s" % inputindent)
                    if titela.upper() in afsluitlijst:
                        return
                    elif titela == "":
                        pass
                    else:
                        titelb = titela.split(" ")
                        titelc = []
                        titel = ""
                        for i in titelb:
                            titelc.append(i.capitalize())
                        for i in titelc:
                            titel += i
                        tracklijst = []
                        for i in repertoirelijst:
                            tracklijst.append(i[1].lower())
                        if titel.lower() in tracklijst:
                            print("Titel bestaat al.")
                            return
                        else:
                            repertoirelijst[int(welke)-1][1] = titel
                            with open("Repertoire", "w") as r:
                                print(repertoirelijst, end = "", file = r)
                            tit = False
            elif wat == "3":
                tak = True
                while tak == True:
                    tik = input("in 3, 4 of \"A\"nders:\n%s" % inputindent).upper()
                    if tik.upper() in afsluitlijst:
                        return
                    elif tik not in tiklijst:
                        print("3, 4 of \"A\"")
                    else:
                        repertoirelijst[int(welke)-1][2] = tik
                        with open("Repertoire", "w") as r:
                            print(repertoirelijst, end = "", file = r)
                        tak = False
            elif wat == "4":
                doof = True
                while doof == True:
                    toon = input("in toonsoort:\n%s" % inputindent).replace(" ","").replace("ineur","").replace("majeur","").replace("inor","").replace("major","")
                    if toon.upper() in afsluitlijst:
                        return
                    elif toon == "":
                        pass
                    elif toon[0].upper() not in toonlijst:
                        pass
                    else:
                        toon = toon.capitalize()
                        repertoirelijst[int(welke)-1][3] = toon
                        with open("Repertoire", "w") as r:
                            print(repertoirelijst, end = "", file = r)
                        doof = False
    except(Exception) as error:
        print(error)
        print("Typ een geldig indexnummer (getal)")

def delstyle():
    lijsten = showstyle()
    stijllijst = lijsten[0]
    dellijst = lijsten[1]
    doei = input("Geef het indexnummer van de stijl die je wilt verwijderen:\n%s" % inputindent)
    repertoirelijst = gettrack()
    try:
        for i in repertoirelijst:
            if stijllijst[int(doei)-1] in i[0]:
                print("Stijl is in gebruik, zal niet verwijderen.")
            else:
                if int(doei) in dellijst:
                    stijllijst.remove(stijllijst[int(doei)-1])
                    with open("Stijlen","w") as s:
                        print(stijllijst, end = "", file = s)
                else:
                    print("Dat indexnummer staat niet in de lijst.")
                return
    except:
        print("Typ een geldig indexnummer (getal)")

def deltrack():
    lijsten = showtrack()
    repertoirelijst = lijsten[0]
    dellijst = lijsten[1]
    doei = input("Geef het indexnummer van de track die je wilt verwijderen:\n%s" % inputindent)
    try:
        if int(doei) in dellijst:
            repertoirelijst.remove(repertoirelijst[int(doei)-1])
            with open("Repertoire","w") as r:
                print(repertoirelijst, end = "", file = r)
        else:
            print("Dat indexnummer staat niet in de lijst.")
        return
    except:
        print("Typ een geldig indexnummer (getal)")

####################################################################################################

rep = True
while rep == True:
    uit = "Y"
    stukje,stijltje,maatje,toontje = [],[],[],[]
    keuze = input("  1 : Toon\n  2 : Voeg toe\n  3 : Verwijder\n  4 : Bewerk\n%s" % inputindent)
    if keuze.upper() in afsluitlijst:
        exit()
    elif keuze == "1":
        doof = True
        while doof == True:
            tos = input("Toon\n  1 : Track\n  2 : Stijl\n%s" % inputindent)
            if tos.upper() in afsluitlijst:
                break
            elif tos == "1":
                showtrack()
            elif tos == "2":
                showstyle()
    elif keuze == "2":
        bij = True
        while bij == True:
            tos = input("Voeg toe\n  1 : Track\n  2 : Stijl\n%s" % inputindent)
            if tos.upper() in afsluitlijst:
                break
            elif tos == "1":
                newtrack()
            elif tos == "2":
                newstyle()
    elif keuze == "3":
        weg = True
        while weg == True:
            tos = input("Verwijder\n  1 : Track\n  2 : Stijl\n%s" % inputindent)
            if tos.upper() in afsluitlijst:
                break
            elif tos == "1":
                try:
                    deltrack()
                except(Exception) as error:
                    print(error)
            elif tos == "2":
                try:
                    delstyle()
                except(Exception) as error:
                    print(error)
    elif keuze == "4":
        hand = True
        while hand == True:
            tos = input("Bewerk\n  1 : Track\n  2 : Stijl\n%s" % inputindent)
            if tos.upper() in afsluitlijst:
                break
            elif tos == "1":
                changetrack()
            elif tos == "2":
                changestyle()
    elif keuze == "0":
        print(forl8("Versie")+forc3(":")+versie)
        print(forl8("Datum")+forc3(":")+datum)
        print(forl8("Plaats")+forc3(":")+plaats)
