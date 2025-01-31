import json

FICHIER = "taches.json"

# ici je charge le fichier taches.json en lecture avec r qui veut dire read
def charger_taches():
    try:
        with open(FICHIER, "r") as fichier:
            contenu = fichier.read().strip()  # strip permet d'enlever les espaces vides
            return json.loads(contenu) if contenu else []  # Ici je vérifie si le fichier est vide ou pas
    except (FileNotFoundError, json.JSONDecodeError):  
        return []  

# Ensuite ici je sauvegarde le fichier taches.json en écriture avec w qui veut dire write
def sauvegarder_taches(taches):
    with open(FICHIER, "w") as fichier:
        json.dump(taches, fichier, indent=4)

# Cette fonction permet d'ajouter une nouvelle tache
def ajouter_tache():
    titre = input("Veuillez entrez le titre de la tâche : ")
    description = input("Veuillez entrez la description de la tâche : ")
    taches = charger_taches() #ici je fais appel à la première fonction
    taches.append({"titre": titre, "description": description, "terminee": False})
    sauvegarder_taches(taches)#ici à la deuxième fonction
    print("La tâche a été ajoutée avec succès !")

# Cette fonction permet d' afficher toutes les tâches qui se trouvent dans le fichier taches.json
def afficher_taches():
    taches = charger_taches()
    if not taches:
        print("Aucune tâche n'a été enregistrée.")
        return
    for i, tache in enumerate(taches):
        statut = "Terminée" if tache["terminee"] else " En cours"
        print(f"{i}. {tache['titre']} - {tache['description']} ({statut})")

# Cette fonction permet de modifier une tâche
def modifier_tache():
    afficher_taches() #ici je fais appel à la fonction d'affichage pour choisir l'élément que je veux modifier
    taches = charger_taches()
    numtaches = int(input("Veuillez entrez le numéro de la tâche à modifier : "))
    if 0 <= numtaches < len(taches):
        taches[numtaches]["titre"] = input("Veuillez entrez le nouveau titre : ")
        taches[numtaches]["description"] = input("Veuillez entrez la nouvelle description : ")
        sauvegarder_taches(taches)
        print("Votre tâche a été modifiée avec succès ")
    else:
        print("Le numéro saisi n'existe pas")

# Cette fonction permet de marquer une tâche comme étant terminée
def terminer_tache():
    afficher_taches()
    taches = charger_taches()
    numtaches = int(input("Veuillez entrez le numéro de la tâche à modifier : "))
    if 0 <= numtaches < len(taches):
        taches[numtaches]["terminee"] = True
        sauvegarder_taches(taches)
        print("La tâche a été marquée terminée ")
    else:
        print("Le numéro saisi n'existe pas")

# Supprimer une tâche
def supprimer_tache():
    afficher_taches()
    taches = charger_taches()
    numtaches = int(input("Veuillez entrez le numéro de la tâche à modifier : "))
    if 0 <= numtaches < len(taches):
        del taches[numtaches]
        sauvegarder_taches(taches)
        print("La tâche a été supprimée avec succès ")
    else:
        print("Le numéro saisi n'existe pas")

# Menu interactif
def menu():
    while True:
        print("\n Menu Gestion des Tâches")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Modifier une tâche")
        print("4. Marquer une tâche comme terminée")
        print("5. Supprimer une tâche")
        print("6. Quitter")
        
        choix = input("Choisissez une option entre (1-6) : ")
        
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            modifier_tache()
        elif choix == "4":
            terminer_tache()
        elif choix == "5":
            supprimer_tache()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Le numéro saisi n'existe pas. Veuillez réessayer")

# Exécution du programme
if __name__ == "__main__":
    menu()
