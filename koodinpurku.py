aakkoset = {
    "A":0,
    "B":0,
    "C":0,
    "D":0,
    "E":0,
    "F":0,
    "G":0,
    "H":0,
    "I":0,
    "J":0,
    "K":0,
    "L":0,
    "M":0,
    "N":0,
    "O":0,
    "P":0,
    "Q":0,
    "R":0,
    "S":0,
    "T":0,
    "U":0,
    "V":0,
    "W":0,
    "X":0,
    "Y":0,
    "Z":0,
    "Å":0,
    "Ä":0,
    "Ö":0
}

yleisyys = {
    "A":12.22,
    "B":0.28,
    "C":0.28,
    "D":1.04,
    "E":7.97,
    "F":0.19,
    "G":0.39,
    "H":1.85,
    "I":10.82,
    "J":2.04,
    "K":4.97,
    "L":5.76,
    "M":3.2,
    "N":8.83,
    "O":5.61,
    "P":1.84,
    "Q":0.01,
    "R":2.87,
    "S":7.86,
    "T":8.75,
    "U":5.01,
    "V":2.25,
    "W":0.09,
    "X":0.03,
    "Y":1.74,
    "Z":0.05,
    "Å":0.00,
    "Ä":3.58,
    "Ö":0.44
}

lopetus = 0
alkuperainenTeksti = ""
teksti = ""
vaihdettu = []
lisattu = []

def laskeKirjaimet():
    return aakkoset

def vaihdaKirjain(vaihdettavaKirjain, uusiKirjain):
    uusiteksti = teksti.replace(vaihdettavaKirjain, uusiKirjain)
    return uusiteksti

def vaihdaYleisin():
    y = 0
    z = 0
    keyY = ""
    keyZ = ""
    for x in aakkoset:
        if aakkoset.get(x) > z and vaihdettu.count(x) == 0:
            z = aakkoset.get(x)
            keyZ = x
    for x in yleisyys:
        if yleisyys.get(x) > y and aakkoset.get(x) != 0 and lisattu.count(x) == 0:
            y = yleisyys.get(x)
            keyY = x
    uusiteksti = teksti.replace(keyZ, keyY.lower())
    vaihdettu.append(keyZ)
    lisattu.append(keyY)
    return uusiteksti

print("""***** KOODINPURKAJA 9000 *****
Voit käyttää tätä ohjelmaa apuvälineneenä purkaessasi erityisesti yksiaakkosellisella salauksella suojattuja viestejä.
Purkaessasi viestiä huomaathan, että viestin isot kirjaimet ovat vielä salattuja ja pienet jo avattuja.
Ota tämä huomioon myös vaihtaessasi kirjaimia itse, jolloin jo vaihdetut ja vaihtamattomat kirjaimet eivät sekoitu.
""")
alkuperainenTeksti = input("Anna alkuperäinen teksti: ")
teksti = alkuperainenTeksti.upper()

for kirjain in alkuperainenTeksti:
        if kirjain != " " and kirjain != "." and kirjain != ",":
            isokirjain = kirjain.upper()
            aakkoset[isokirjain] = aakkoset[isokirjain] + 1

while lopetus != 1:
    print("""Anna käsky:
    1: Näytä alkuperäiset kirjainten määrät
    2: Näytä alkuperäinen teksti
    3: Vaihda kirjain
    4: Kokeile vaihtaa automaattisesti yleisin vaihtamaton kirjain
    5: Näytä nykyinen teksti
    6: Näytä yksittäisten kirjainten yleisyydet
    0: Lopeta ohjelma
    """)
    vastaus = input("Käsky: ")

    if vastaus == "1":
        print(laskeKirjaimet())
    elif vastaus == "2":
        print(alkuperainenTeksti)
    elif vastaus == "3":
        vaihdettavaKirjain = input("Minkä kirjaimen haluat vaihtaa? ")
        uusiKirjain = input("Minkä kirjaimen haluat laittaa tilalle? ")
        teksti = vaihdaKirjain(vaihdettavaKirjain, uusiKirjain)
        print(teksti)
    elif vastaus == "4":
        teksti = vaihdaYleisin()
        print(teksti)
    elif vastaus == "5":
        print(teksti)
    elif vastaus == "6":
        print(yleisyys)
    elif vastaus == "0":
        lopetus = 1
