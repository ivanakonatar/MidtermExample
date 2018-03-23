#Citamo podatke iz fajla "lista", racunamo prosjecnu visinu i dobijeni rezultat zapisujemo u tekstualni fajl rezultat.txt

sve_linije = open("lista","r").readlines()

suma_visina = 0
for linija in sve_linije:
    linija_bez_novog_reda = linija.strip()
    ime_i_visina = linija_bez_novog_reda.split(",")

    ime = str(ime_i_visina[0])
    visina = int(ime_i_visina[1])
    suma_visina += visina

prosjecna_visina = str(round((suma_visina/len(sve_linije)), 2))
rezultat = open("rezultat.txt","a").write("Prosjecna visina je: " + prosjecna_visina + "\n")