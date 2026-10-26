import string

print("Tervetuloa salausohjelmaan (Caesar Cipher)")
print("")

syote = input("Syötä koodi jonka haluat salata... Koodin numeroita ei muuteta! \n >>").lower()

kirjaimet = "abcdefghijklmnopqrstuvwxyz"

# MITEN SAAN stringistä yhden kirjaimen? miten siirrän 3 pykälää



for kirjain in syote:
    if kirjain in kirjaimet:
        vanha_indeksi = kirjaimet.index(kirjain)

        uusi_indeksi = (vanha_indeksi + 3) % 26

        uusi_kirjain = kirjaimet[uusi_indeksi]

        print(uusi_kirjain, end="")

    else:
        print(kirjain, end="")
#y = chr(65)
#print(y)



#merkki = "a"
#if merkki in string.digits:
    #print(f"Merkki {merkki} on numero!")
#else:
    #print(f"Merkki {merkki} ei ole numero")