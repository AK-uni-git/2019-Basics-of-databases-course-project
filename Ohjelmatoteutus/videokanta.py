

# AK-uni-git
# 23.7.2019

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
import sqlite3 
import sys



def valikko():
	print("""Anna haluamasi toiminnon numero seuraavasta valikosta:
Haut:
1) Listaa kaikkien videoiden tiedot
2) Listaa videoiden kaikki ajankohdat
3) Listaa henkilöiden osoitteet
4) Etsi kaikki ajankohdat tietyn paikan mukaan 
5) Etsi kaikki ajankohdat tietyn henkilön mukaan

Muut:
6) Muokkaa henkilön tietoja
7) Lisää uusi video
8) Luo videon ajankohtien määrästä kuvaaja
0) Lopeta""")

def main():
    # Yhdistetään tietokantaan.
    conn = sqlite3.connect('HT_test.sqlite3')
    kursori = conn.cursor()
    print("Tervetuloa video tietokantaan!\n")

    while True:
            valikko()
            valinta = (input("Valintasi: "))
            print("\n")
            if valinta == 0:
                print("Kiitos ohjelman käytöstä.")
                # Suljetaan tietokanta.
                conn.close()
                break
            elif valinta == '1':
                videoTiedot(kursori)
            elif valinta == '2':
                videoAjankohdat(kursori)
            elif valinta == '3':
                henkiloOsoitteet(kursori)
            elif valinta == '4':
                etsiPaikanMukaan(kursori)
            elif valinta == '5':
                etsiHenkilonMukaan(kursori)
            elif valinta == '6':
                paivitaHenkilo(kursori)
            elif valinta == '7':
                LisaaVideo(kursori)
            elif valinta == '8':
                visualisoi_Bokeh(kursori)
            else:
                print("Tuntematon syöte!\n")

    syote_s = input("Syötä halutun koiran nimi: ")
    #Tehdään tuple
    syote = (syote_s,)


def videoTiedot(kursori):
    kursori.execute('''SELECT * FROM "Video";''')
    rivit = kursori.fetchall()
    print("{:<10} {:<64} {:<64} {:<32}".format("VideoID", "Nimi", "Tiedostopolku", "Kesto"))
    for rivi in rivit:
        #Muutetaan listaksi, jotta None arvot voidaan muuttaa tyhjiksi merkkijonoiksi.
        rivi = list(rivi)
        index = 0
        while index < len(rivi):
            if rivi[index] == None:
                rivi[index] = ''
            index += 1
        print("{:<10} {:<64} {:<64} {:<32}".format(rivi[0], rivi[1], rivi[2], rivi[3]))
    print("\n")

def videoAjankohdat(kursori):
    kursori.execute('''SELECT "Video"."nimi" AS 'Videon nimi', "Video"."Tiedostopolku", "Video"."Kesto" AS 'Videon kesto',
    "Ajankohta"."Nimi" AS 'Ajankohdan nimi', "Ajankohta"."Pvm", "Ajankohta"."Alku", "Ajankohta"."Loppu"  FROM "Video" 
    INNER JOIN "VideonAjankohta" ON "VideonAjankohta"."VideoID" = "Video"."VideoID"
    INNER JOIN "Ajankohta" ON "Ajankohta"."AjankohtaID" = "VideonAjankohta"."AjankohtaID";''')
    rivit = kursori.fetchall()
    print("{:<32} {:<32} {:<32} {:<32} {:<16} {:<16} {:<16}".format("Videon nimi", "Tiedostopolku", "Videon kesto", "Ajankohdan nimi", "Päivämäärä", "Alku", "Loppu"))
    for rivi in rivit:
        #Muutetaan listaksi, jotta None arvot voidaan muuttaa tyhjiksi merkkijonoiksi.
        rivi = list(rivi)
        index = 0
        while index < len(rivi):
            if rivi[index] == None:
                rivi[index] = ''
            index += 1
        print("{:<32} {:<32} {:<32} {:<32} {:<16} {:<16} {:<16}".format(rivi[0], rivi[1], rivi[2], rivi[3], rivi[4], rivi[5], rivi[6]))
    print("\n")

def henkiloOsoitteet(kursori):
    kursori.execute('''SELECT "Henkilo"."Etunimi", "Henkilo"."Sukunimi", "Osoite"."Katu" AS 'Katuosoite',
    "Postinumero"."Kaupunki", "Postinumero"."Numero" AS 'Postinumero', "Osoite"."Maa" FROM "Henkilo"
    LEFT OUTER JOIN "Osoite" ON "Henkilo"."OsoiteID" = "Osoite"."OsoiteID"
    LEFT OUTER JOIN "Postinumero" ON "Osoite"."PostID" = "Postinumero"."PostID"; ''')
    rivit = kursori.fetchall()
    print("{:<32} {:<32} {:<32} {:<32} {:<16} {:<32}".format("Etunimi", "Sukunimi", "Katuosoite", "Kaupunki", "Postinumero", "Maa"))
    for rivi in rivit:
        #Muutetaan listaksi, jotta None arvot voidaan muuttaa tyhjiksi merkkijonoiksi.
        rivi = list(rivi)
        index = 0
        while index < len(rivi):
            if rivi[index] == None:
                rivi[index] = ''
            index += 1
        print("{:<32} {:<32} {:<32} {:<32} {:<16} {:<32}".format(rivi[0], rivi[1], rivi[2], rivi[3], rivi[4], rivi[5]))
    print("\n")

def etsiPaikanMukaan(kursori):
    syote_s = input("Syötä paikannimi, jonka mukaan etsitään: ")
    #Tehdään tuple
    syote = (syote_s,)
    kursori.execute('''SELECT "Paikka"."Nimi" AS 'Paikan nimi', 'on ajankohdassa' AS "Selite 1",
    "Ajankohta"."Nimi" AS 'Ajankohdan nimi', "Ajankohta"."Pvm", "Ajankohta"."Alku", "Ajankohta"."Loppu"  FROM "Ajankohta" 
    INNER JOIN "AjankohdanP" ON "Ajankohta"."AjankohtaID" = "AjankohdanP"."AjankohtaID"
    INNER JOIN "Paikka" ON "AjankohdanP"."PaikkaID" = "paikka"."PaikkaID"
    WHERE "Paikka"."Nimi" = ?;''', syote)
    rivit = kursori.fetchall()
    print("{:<32} {:<32} {:<32} {:<16} {:<16} {:<16}".format("Paikan nimi", "Selite", "Ajankohdan nimi", "Päivämäärä", "Alku", "Loppu"))
    for rivi in rivit:
        #Muutetaan listaksi, jotta None arvot voidaan muuttaa tyhjiksi merkkijonoiksi.
        rivi = list(rivi)
        index = 0
        while index < len(rivi):
            if rivi[index] == None:
                rivi[index] = ''
            index += 1
        print("{:<32} {:<32} {:<32} {:<16} {:<16} {:<16}".format(rivi[0], rivi[1], rivi[2], rivi[3], rivi[4], rivi[5]))
    print("\n")

def etsiHenkilonMukaan(kursori):
    syote_s = input("""Syötä henkilönnimi ("etunimi sukunimi"), jonka mukaan etsitään: """)
    syote_s = syote_s.split(' ')
    #Virheentarkistus
    if len(syote_s) != 2:
        sys.exit("Annoit virheellisen nimen. Ohjelma lopetetaan.\n")

    #Tehdään tuple
    syote = (syote_s[0], syote_s[1], )
    kursori.execute('''SELECT "Henkilo"."Etunimi", "Henkilo"."sukunimi", 'on ajankohdassa' AS "Selite 1",
    "Ajankohta"."Nimi" AS 'Ajankohdan nimi', "Ajankohta"."Pvm", "Ajankohta"."Alku", "Ajankohta"."Loppu"  FROM "Ajankohta" 
    INNER JOIN "AjankohdanH" ON "Ajankohta"."AjankohtaID" = "AjankohdanH"."AjankohtaID"
    INNER JOIN "Henkilo" ON "AjankohdanH"."HenkiloID" = "Henkilo"."HenkiloID"
    WHERE "Henkilo"."Etunimi" = ? AND "Henkilo"."sukunimi" = ? ;''', syote)
    rivit = kursori.fetchall()
    print("{:<32} {:<32} {:<32} {:<32} {:<16} {:<16} {:<16}".format("Etunimi", "Sukunimi", "Selite", "Ajankohdan nimi", "Päivämäärä", "Alku", "Loppu"))
    for rivi in rivit:
        #Muutetaan listaksi, jotta None arvot voidaan muuttaa tyhjiksi merkkijonoiksi.
        rivi = list(rivi)
        index = 0
        while index < len(rivi):
            if rivi[index] == None:
                rivi[index] = ''
            index += 1
        print("{:<32} {:<32} {:<32} {:<32} {:<16} {:<16} {:<16}".format(rivi[0], rivi[1], rivi[2], rivi[3], rivi[4], rivi[5], rivi[6]))
    print("\n")

def LisaaVideo(kursori):
    syote_s = input('Syötä videon tiedot muodossa "nimi tiedostopolku HH:MM:SS":')
    syote_s = syote_s.split(' ')
    
    #Virheentarkistus
    try:
        #Tehdään tuple
        syote = (syote_s[0], syote_s[1], syote_s[2], )
    except:
        sys.exit("Annoit virheellisen syotteen. Ohjelma lopetetaan.\n")
    
    kursori.execute('''INSERT INTO "Video" ("Nimi", "Tiedostopolku", "Kesto") VALUES (?, ?, ?);''', syote)
    videoTiedot(kursori)
    print("\n")

def paivitaHenkilo(kursori):
    haettava = input("Anna päivitettävän henkilön nimi muodossa 'etunimi sukunimi': ")
    haettava = haettava.split()
    syote_s = input('Syötä henkilön uudet tiedot muodossa "OsoiteID Etunimi Sukunimi DD-MM-YYYY": ')
    syote_s = syote_s.split(' ')
    #Virheentarkistus
    try:
        #Tehdään tuple
        syote = (syote_s[0], syote_s[1], syote_s[2], syote_s[3], haettava[0], haettava[1], )
        #Tarkistetaan syntymäajan muoto:
        Testattava = syote_s[3]
        Testattava = Testattava.split('-')
        if len(Testattava) != 3:
            raise Exception('Syntymäajassa ei ollut 3 arvoa.')
        for alkio in Testattava:
            if alkio.isnumeric() == False:
                raise Exception('Ei numeraalinen syntymäaika.')
    except:
        sys.exit("Annoit virheellisen syotteen. Ohjelma lopetetaan.\n")
    kursori.execute('''UPDATE "Henkilo" SET
   "OsoiteID" = ?, "Etunimi" = ?, "Sukunimi" = ?, "Synt_aika" = ?
   WHERE "Etunimi" = ? AND "Sukunimi" = ?;''', syote)

    #Tarkistetaan päivitys
    tulostaHenkilonTiedot(kursori, syote_s[1], syote_s[2])
    
def tulostaHenkilonTiedot(kursori, etunimi, sukunimi):
    syote = (etunimi, sukunimi, )
    kursori.execute('''SELECT * FROM "Henkilo"
    WHERE "Etunimi" = ? AND "Sukunimi" = ?;''', syote)
    rivit = kursori.fetchall()
    print("{:<16} {:<16} {:<32} {:<32} {:<16}".format("HenkiloID", "OsoiteID", "Etunimi", "Sukunimi", "Syntymäaika") )
    for rivi in rivit:
        #Muutetaan listaksi, jotta None arvot voidaan muuttaa tyhjiksi merkkijonoiksi.
        rivi = list(rivi)
        index = 0
        while index < len(rivi):
            if rivi[index] == None:
                rivi[index] = ''
            index += 1
        print("{:<16} {:<16} {:<32} {:<32} {:<16}".format(rivi[0], rivi[1], rivi[2], rivi[3], rivi[4]))
    print("\n")
    

def visualisoi_Bokeh(kursori):
    
    # Tallennettavan tiedoston nimi.
    output_file("videotJaAjankohdat.html")

    kursori.execute('''SELECT "Video"."Nimi" AS 'Videon nimi', COUNT ("Ajankohta") AS 'Ajankohtia' FROM "Video" 
    INNER JOIN "VideonAjankohta" ON "VideonAjankohta"."VideoID" = "Video"."VideoID"
    INNER JOIN "Ajankohta" ON "Ajankohta"."AjankohtaID" = "VideonAjankohta"."AjankohtaID"
    GROUP BY "Video"."VideoID";''')

    videot = []
    maarat = []

    rivit = kursori.fetchall()
    for rivi in rivit:
        videot.append(rivi[0])
        maarat.append(rivi[1])

    source = ColumnDataSource(data=dict(videot=videot, maarat=maarat))

    p = figure(x_range=videot, plot_height=350, toolbar_location=None, title="Ajankohdat per video")
    p.vbar(x='videot', top='maarat', width=0.9, source=source, legend="videot",
        line_color='white', fill_color=factor_cmap('videot', palette=Spectral6, factors=videot))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 9
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    print("Kuvaaja avattu uuteen ikkunaan.\n\n")
    show(p)

main()

