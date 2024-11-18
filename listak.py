import random

def ketto():
    # 2.	Tölts fel egy listát 0-30-ig páros számokkal (range)! Egy másikat 39-től 21-ig páratlan számokkal!
    lista1 = []
    lista2 = []

    for i in range(0,31,2):
        lista1.append(i)

    for j in range(39, 20, -2):
        lista2.append(j)

    # print(lista1)
    # print(lista2)

    # a.	Fűzd egymás után a két listát az első listában!
    for index in lista2:
        lista1.append(index)
    # print(lista1)

    # b.	Minden 3. helyre illessz be egy 40 és 70 közötti véletlen számot!
    for i in range(0, len(lista1), 3):
        lista1[i] = random.randint(40,70)
    # print(lista1)

    # c.	Írasd ki a lista elemeit egy sorban, minden 5. után sortöréssel!
    szamlalo = 0
    for index in lista1:
        print(index, end=" ")
        szamlalo += 1
        if szamlalo == 5:
            print("")
            szamlalo = 0