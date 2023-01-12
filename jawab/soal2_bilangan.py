inp = int(input("Ketik angka\t: "))

bilangan = []

def num(nilai):
    if nilai == nilai:
        bulat = "bulat"
        bilangan.append(bulat)

    nilai = nilai
    if nilai >= 0:
        cacah = "cacah"
        bilangan.append(cacah)

    nilai = nilai
    if nilai < 0:
        negatif = "negatif"
        bilangan.append(negatif)

    nilai = nilai
    if nilai == 0:
        nol = "nol"
        bilangan.append(nol)

    if nilai > 0:
        asli = "asli"
        bilangan.append(asli)

    nilai = nilai
    if nilai % 2 != 0:
        ganjil = "ganjil"
        bilangan.append(ganjil)

    nilai = nilai
    if nilai % 2 == 0:
        genap = "genap"
        bilangan.append(genap)

    nilai = nilai
    if nilai > 1 :
        for i in range(2, nilai):
            if(nilai % i) == 0:
                komposit = "komposit"
                bilangan.append(komposit)
                break
            else:
                prima = "prima"
                bilangan.append(prima)
                break

    return bilangan

num(inp)
print(bilangan)