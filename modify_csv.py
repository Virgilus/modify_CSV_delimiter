#Modify the delimiter of a CSV file. For exemple from ";" to ",".
#opening and writing the file with the csv module.

import csv

print ("Ce programme vous permet de modifier les séparateurs d'un fichier CSV.")

PathFileInput = input("Entrez le chemin du CSV que vous désirez modifier :  ")
Separator = input("Entrez le type de séparateur actuel de votre fichier CSV :  ")

NewSeparator = input("Entrez le nouveau type de séparateur pour votre nouveau fichier CSV :  ")
PathFileOutput = input("Entrez le chemin du CSV que vous désirez créer, en terminant par .csv :  ")

with open(PathFileInput, newline='', encoding='utf-8') as csvfile:  
    f_i = csv.reader(csvfile, delimiter=Separator, quotechar='"')
    
    with open(PathFileOutput, 'w', newline='', encoding='utf-8') as csvfile_2:  
        f_o = csv.writer(csvfile_2, delimiter=NewSeparator, quotechar='"')
        f_o.writerows(f_i)
print ("Fini, le programme a traité",f_i.line_num, "ligne(s)")
