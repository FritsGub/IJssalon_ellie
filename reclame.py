from  algemene_functies import mijn_functie_2

smaak = "aardbei"
prijs = 4
korting = 0.1

def aanbieding_1(str1,str2,str3):
    bedrag=str2-(str2*str3)
    bedrag_netjes = f"{bedrag:.2f}".replace(".", ",")
    uitvoer= f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {str1}, van {str2} euro voor {bedrag_netjes} euro."
    return uitvoer
aanbieding_1(smaak,prijs,korting)
mijn_aanbieding=aanbieding_1 (smaak,prijs,korting)
print (mijn_aanbieding)

inkomsten= [220,430,125,160,205,90,345,0.09]
def inkomsten_totaal(inkomsten):
    global totaal
    global btw_bedrag
    totaal=0
    btw=inkomsten[-1]
    for getal in inkomsten[0:7]:
      totaal += getal
    btw_bedrag=btw*totaal
    return totaal, btw_bedrag
inkomsten_totaal (inkomsten)
print(f"Mijn totaal van alle inkomsten van deze week is {totaal} euro,  waarover {btw_bedrag} euro btw betaald dient te worden.")

def laag_en_hoog(inkomsten):
    global mijn_max, mijn_min
    mijn_max = max(inkomsten[:7])
    mijn_min = min(inkomsten [:7])
    return mijn_max, mijn_min
laag_en_hoog(inkomsten)
# print (mijn_max, mijn_min)

mijn_lijst= [220,430,125,160,205,90,345]
def gemiddelde(mijn_lijst):
    samen=0
    for i in mijn_lijst :
        samen += i
    mean =samen/7
    return mean
gemiddelde(mijn_lijst)
mijn_gemiddelde = gemiddelde(mijn_lijst)
mijn_gemiddelde_netjes= f"{mijn_gemiddelde:.2f}".replace(".", ",")
print (f"De gemiddelde inkomsten deze week zijn {mijn_gemiddelde_netjes} euro.")

invoerlijst = [10,5,3,2,1,2,9]
def meervoudig(invoerlijst): 
    laag_en_hoog(invoerlijst)
    return mijn_max, mijn_min
meervoudig(invoerlijst)
# print (mijn_max, mijn_min)

invoerlijst_2=[2,4]
def combinatie(invoerlijst_2):
    global mijn_max, mijn_min
    laag_en_hoog(invoerlijst_2)
    return mijn_max, mijn_min
combinatie(invoerlijst_2)
# print (mijn_max, mijn_min)
korte_lijst=[mijn_max, mijn_min]

mijn_functie_2(korte_lijst[0], korte_lijst[1])
resultaat=mijn_functie_2(korte_lijst[0], korte_lijst[1])
# print (resultaat)

