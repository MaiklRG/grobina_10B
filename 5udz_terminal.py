"""
Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī. 
Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt"). 
Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas. 
Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu.
"""
def terminal():
    try:
        with open('5udz.txt', "w", encoding="utf8") as vards:
            vards.write(input("Ievadi savu vārdu:"))
            
            print(f"Vārds ievadīts!")
    
    except FileNotFoundError:
        print("Fails netika atrasts!")

if __name__=="__main__":
    terminal()