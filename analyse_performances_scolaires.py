
# Analyse des performances scolaires
# Projet Python pour analyser les notes des étudiants

nom_etudiant = input("Entrez le nom de l'etudiant : ")

note1 = float(input("Entrez la premiere note : "))
note2 = float(input("Entrez la deuxieme note : "))
note3 = float(input("Entrez la troisieme note : "))

moyenne = (note1 + note2 + note3) / 3

print("\n--- Bulletin de l'etudiant ---")
print("Nom :", nom_etudiant)
print("Moyenne :", round(moyenne, 2))

if moyenne >= 10:
    print("Resultat : Admis")
else:
    print("Resultat : Non admis")
