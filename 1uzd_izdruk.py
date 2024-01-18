# Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā)

def lasit():
    try:
        with open('parbaude.txt', "r", encoding="utf8") as datne:
            for x in datne:
                print(x)

    except FileNotFoundError:
        print("Datne nav atrasta failā!")



if __name__=="__main__":
    lasit()