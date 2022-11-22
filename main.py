import random
niveau_de_vie = 20
numero_adversaire = 1
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
def initialisationdelapartie():
    global nombre_victoires
    if nombre_victoires > 3:
        force_adversaire = random.randint(6, 11)
        print(force_adversaire)
    else:
        force_adversaire = random.randint(1, 11)
        print(force_adversaire)
    print ('Vous tombez face a face avec un adversaire de difficulte:', force_adversaire)
    choix = input('Que voulez vous faire ?\n1- Combattre cet adversaire \n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les rèels du jeu\n4- Quitter le jeu')
    if choix == '1':
        global numero_combat
        global numero_adversaire
        global niveau_de_vie
        global nombre_defaites
        global nombre_victoires_consecutives
        print('Vous avez choisi de combattre cet adversaire\n Adversaire:', numero_adversaire, '\n Force de l adversaire:', force_adversaire, '\n Niveau de vie de l\'usager:', niveau_de_vie, '\n Combat:', numero_combat, ':', nombre_victoires, 'vs', nombre_defaites)
        score_dé = random.randint(1, 6)
        score_dé2 = random.randint(1, 6)
        final_dé = score_dé + score_dé2
        print('Lancer du dé:', final_dé)
        if final_dé > force_adversaire:
            print('Vous avez gagné le combat')
            niveau_de_vie = niveau_de_vie + force_adversaire
            print('Votre niveau de vie est de:', niveau_de_vie)
            nombre_victoires_consecutives = nombre_victoires_consecutives + 1
            print('Nombre de victoires consécutives:', nombre_victoires_consecutives)
            numero_adversaire = numero_adversaire + 1
            numero_combat = numero_combat + 1
            nombre_victoires = nombre_victoires + 1
        else:
            print('Vous avez perdu le combat')
            niveau_de_vie = niveau_de_vie - force_adversaire
            print('Votre niveau de vie est de:', niveau_de_vie)
            numero_adversaire = numero_adversaire + 1
            numero_combat = numero_combat + 1
            nombre_defaites = nombre_defaites + 1
            nombre_victoires_consecutives = 0
            if niveau_de_vie == 0:
                print('La partie est terminée, vous avez vaincu', nombre_victoires, 'monstres')
                niveau_de_vie = 20
    if choix == '2':
        print('Vous avez choisi de contourner le monstre, vous allez perdre une vie')
        niveau_de_vie = niveau_de_vie - 1
        print('Votre niveau de vie est de:', niveau_de_vie)
    if choix == '3':
        print('Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.'
              'Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n'
              'Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.\n '
              'Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n'
              'La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n'
              'L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.')
def recommencer():
    choix = input("Voulez vous jouer? (oui/non)")
    if choix == 'oui':
        return True
    elif choix == 'non':
        return False
def main():
    while recommencer():
        initialisationdelapartie()


main()
