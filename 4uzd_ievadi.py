"""
 Izveidot Python programmu, kur lietotājs ievada gar faila nosaukumu un faila formātu (paplašinājumu),
 un atkarībā no faila paplašinājuma tiek nolasīts faila saturs. 
 Nolasītā informācija ir jāizdrukā terminālī. 
 Ievērot iespejamās kļūdas!
"""
def ievadi_failu():
    try:
        with open('4uzd.txt',"x", encoding="utf8") as fail:
            fail.write(input("Ievadi nosaukumu:"))

    except FileNotFoundError:
        print("Šāds fails neeksistē!")

    if __name__=="__main__":
            ievadi_failu()