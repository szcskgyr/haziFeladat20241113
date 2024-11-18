def beolvas():
    szoveg = input("Kérem, adjon meg egy szöveget! ")
    return szoveg

def beolvasIrasjelekNelkul():
    irasjelek = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    szoveg = input("Kérem, adjon meg egy szöveget!")
    irasjelek_nelkul = ""
    for betu in szoveg:
        if betu not in irasjelek:
            irasjelek_nelkul += betu
    return irasjelek_nelkul

def beolvasBetu():
    betu = input("Kérem, adjon meg egy betűt! ")
    while not((len(betu) == 1) and not betu.isdigit()):
        betu = input("Kérem, adjon meg egy betűt! ")
    return betu

def beolvasSzo():
    szo = input("Kérem, adjon meg egy szót! ")
    while not ellenoriz(szo):
        szo = input("Kérem, adjon meg egy szót! ")
    return szo

def ellenoriz(szoveg):
    joe = True
    nemMegengedett = "0123456789 ,.'\"+!%/=()<>#&@{};.,-*€"
    for betu in szoveg:
        if betu in nemMegengedett:
            joe = False
            # az első egyezés esetén lépjünk ki a ciklusból, ne vizsgáljuk tovább!
            break
    return joe

def egy():
    # 1.	Kérj be tetszőleges szöveget, majd írasd ki a hosszát.
    szoveg = input("Kérem, adjon meg egy szöveget! ")
    # print(type(szoveg))
    print("A szöveg hossza: " + str(len(szoveg)) + " karakter.")

def ketto():
    # 2.	Kérj be tetszőleges szöveget, majd írasd ki úgy, hogy  minden karaktere egymás alatt legyen.
    szoveg = beolvas()
    # kiírás index szerint
    for index in range(0, len(szoveg), 1):
        print(szoveg[index])
    print("")

    #kiírás érték szerint
    for betu in szoveg:
        print(betu)

def harom():
    # 3.	Kérj be tetszőleges szöveget, majd mindek karakterét cseréld nagybetűsre.
    szoveg = beolvas()
    nagybetus = szoveg.upper()
    print("A szöveg nagybetűkkel: "+nagybetus)

def negy():
    # 4.	Kérj be tetszőleges szöveget, majd írasd ki visszafelé.
    szoveg = beolvas()
    for index in range(len(szoveg)-1, -1, -1):
        print(szoveg[index], end="")

def ot():
    # 5.	Írjon programot, mely megszámolja, hogy az inputként érkező mondatban hány darab ”a” betű van!
    szoveg = beolvas()
    darab = 0
    for index in range(0, len(szoveg), 1):
        if szoveg[index].lower() == "a":
            darab += 1
    print("Az a betűk száma: "+str(darab)+" db.")

def hat():
    szoveg = beolvas()
    betu = beolvasBetu()
    # print(betu)
    darab = 0
    for index in range(0, len(szoveg), 1):
        if szoveg[index].lower() == betu:
            darab += 1
    print("A(z) " + betu + " betűk száma: "+str(darab)+" db.")

# 7.	Az input szövegből távolítsa el a szóközöket!

def hetA():
    szoveg =  beolvas()
    print("A szöveg szóközök nélkül: ", end="")
    szokoznelkuli = szoveg.replace(" ", "")
    print(szokoznelkuli)

def hetB():
    szoveg = beolvas()
    print("A szöveg szóközök nélkül: ", end="")
    for index in range(0, len(szoveg), 1):
        if szoveg[index] != " ":
            print(szoveg[index], end="")

def hetC():
    szoveg = beolvas()
    darabolt = szoveg.split(" ") # lista
    print("A szöveg szóközök nélkül: ", end="")
    for index in range(0, len(darabolt), 1):
        print(darabolt[index], end="")

def nyolc():
    # 8.	Olvasson be egy mondatot és egy szót! Mondja meg, hogy a szó szerepel-e a mondatban!
    mondat = beolvas()
    szo = beolvasSzo()
    if szo in mondat:
        print("A szó szerepel a mondatban.")
    else:
        print("A szó nem szerepel a mondatban.")

def kilenc():
    # 9.	A beolvasott mondat kisbetűit alakítsa nagybetűsre, a nagybetűs karaktereket pedig kisbetűsre!
    szoveg = beolvas()
    print("A szöveg kis-és nagybetűi invertálva: ", end="")
    for betu in szoveg:
        if betu.isupper():
            betu = betu.lower()
            print(betu, end="")
        else:
            betu = betu.upper()
            print(betu, end="")

def tiz():
    # 10. Kérj be két szót, majd döntese el a program, hogy ugyanazok-e?
    szo1 = beolvasSzo().lower()
    szo2 = beolvasSzo().lower()
    if szo1 == szo2:
        print("A két szó azonos!")
    else:
        print("A két szó eltérő!")

def tizenegy():
    # 11. A beolvasott mondatról döntse el, hogy az visszafelé is ugyanazt jelenti-e!
    mondat = beolvasIrasjelekNelkul().lower()
    mondatvissza = ""
    for index in range(len(mondat)-1, -1, -1):
        mondatvissza += mondat[index]
    if mondat == mondatvissza:
        print("A mondat visszafelé olvasva is azonos.")
    else:
        print("A mondat visszafelé olvasva nem azonos.")

def tizenketto():
    # 12. Írj programot ami beolvas egy nevet, és megadja a monogramját (a név két szóból álljon, egy szóközzel elválasztva)
    nev = beolvas().upper().split(" ")
    print("A beírt név monogramja: " + nev[0][0] + nev[1][0])

def tizennegy():
    # 14. Írjon programot, mely megszámolja, hogy az inputként érkező mondatban hány darab ”h” betű van!
    mondat = beolvas()
    szamlalo = 0
    for betu in mondat:
        if betu.lower() == "h":
            szamlalo +=1
    print("A szövegben "+str(szamlalo)+" db h betű van")