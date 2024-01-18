# Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu

def lasit_rinda():
    try:
        with open('parbaude.txt',"r", encoding="utf8") as datne:
            for z in datne:
                print(datne.readline())

    except FileNotFoundError:
        print("Nav atrasta datne fails!")

if __name__=="__main__":
    lasit_rinda()

