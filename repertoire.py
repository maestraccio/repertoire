#!/usr/bin/env python3
import ast, os

print("\nRepertoire\n")
afsluitlijst = ["X","Q"]
inputindent = "    : "
forc3 = "{:^3}".format
forr3 = "{:>3}".format
forl5 = "{:<5}".format
forl15 = "{:<15}".format
forl25 = "{:<25}".format

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

def showstyle():
    stijllijst = getstyle()
    repertoirelijst = gettrack()
    stijlindex = 0
    for i in stijllijst:
        tracks = 0
        for j in repertoirelijst:
            if i == j[0]:
                tracks += 1
        stijlindex += 1
        if stijltje.lower() in i.lower():
            print(forr3(str(stijlindex))+" : "+forl15(i)+str(tracks))
    stijllijst = sorted(stijllijst)
    return stijllijst

def newstyle():
    stijllijst = showstyle()
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
                stijllijst.append(stijl)
                stijllijst = sorted(stijllijst)
                with open("Stijlen","w") as s:
                    print(stijllijst, end = "", file = s)
                stil = False

def gettrack():
    try:
        with open("Repertoire","r") as r:
            repertoirelijst = ast.literal_eval(r.read())
    except(Exception) as error:
        print(error)
        repertoirelijst = []
    repertoirelijst = sorted(repertoirelijst)
    return repertoirelijst

def showtrack():
    repertoirelijst = gettrack()
    trackindex = 0
    trackcount = 0
    print(forr3("ID")+" : "+forl15("STIJL")+forl25("TITEL")+forc3("TIK")+forl5("TOON"))
    print(forr3(3*"-")+" : "+forl15(15*"-")+forl25(25*"-")+forc3(3*"-")+forl5(3*"-"))
    for i in repertoirelijst:
        trackindex += 1
        if stijltje.lower() in i[0].lower() and stukje.lower() in i[1].lower() and maatje.lower() in i[2].lower() and toontje.lower() in i[3].lower():
            print(forr3(str(trackindex))+" : "+forl15(i[0][:15])+forl25(i[1][:25])+forc3(i[2])+forl5(i[3]))
            trackcount += 1
    print("Aantal tracks : %s" % trackcount)
    repertoirelijst = sorted(repertoirelijst)
    return repertoirelijst

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
        stijllijst = showstyle()
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
        toon = input("in toonsoort:\n%s" % inputindent)[:4]
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

def delstyle():
    stijllijst = getstyle()
    repertoirelijst = gettrack()
    for i in repertoirelijst:
        if stijllijst[int(doei)-1] in i[0]:
            print("Stijl is in gebruik, zal niet verwijderen.")
        else:
            stijllijst.remove(stijllijst[int(doei)-1])
            with open("Stijlen","w") as s:
                print(stijllijst, end = "", file = s)
            return

def deltrack():
    repertoirelijst = gettrack()
    repertoirelijst.remove(repertoirelijst[int(doei)-1])
    with open("Repertoire","w") as r:
        print(repertoirelijst, end = "", file = r)

def seltrack():
    selt = input("Welke titel:\n%s" % inputindent)

rep = True
while rep == True:
    uit = "Y"
    stukje,stijltje,maatje,toontje = "","","",""
    keuze = input("Kies:\n  1 : Toon\n  2 : Voeg toe\n  3 : Verwijder\n  4 : Handwerk\n%s" % inputindent)
    if keuze.upper() in afsluitlijst:
        exit()
    elif keuze == "1":
        doof = True
        while doof == True:
            tos = input("Toon\n  1 : Track\n  2 : Stijl\n%s" % inputindent)
            if tos.upper() in afsluitlijst:
                break
            elif tos == "1":
                print("Filter \"AND\" (alle criteria moeten matchen)")
                stukje = input("Geef (een stukje) van de titel op:\n%s" % inputindent).strip().replace("'","").replace("’","").replace(",","").replace(".","").replace("-","").replace("_","").replace("?","").replace("!","").replace(" ","")
                if stukje.upper() in afsluitlijst:
                    break
                stijltje = input("Geef (een stukje) van de stijl op:\n%s" % inputindent)
                if stijltje.upper() in afsluitlijst:
                    break
                maatje= input("Geef (een stukje) van de maatsoort op:\n%s" % inputindent)
                if maatje.upper() in afsluitlijst:
                    break
                toontje= input("Geef (een stukje) van de toonsoort op:\n%s" % inputindent)
                if toontje.upper() in afsluitlijst:
                    break
                showtrack()
            elif tos == "2":
                stijltje = input("Geef (een stukje) van de stijl op:\n%s" % inputindent)
                if stijltje.upper() in afsluitlijst:
                    break
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
            wv = input("Verwijder\n  1 : Track\n  2 : Stijl\n%s" % inputindent)
            if wv.upper() in afsluitlijst:
                break
            elif wv == "1":
                stukje = input("Geef (een stukje) van de titel op:\n%s" % inputindent)
                stijltje,maatje,toontje = "","",""
                showtrack()
                doei = input("Geef het indexnummer van de track die je wilt verwijderen:\n%s" % inputindent)
                try:
                    deltrack()
                except(Exception) as error:
                    print(error)
            elif wv == "2":
                stijltje = input("Geef (een stukje) van de stijl op:\n%s" % inputindent)
                showstyle()
                doei = input("Geef het indexnummer van de stijl die je wilt verwijderen:\n%s" % inputindent)
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
                os.system("vim Repertoire")
            elif tos == "2":
                os.system("vim Stijlen")

