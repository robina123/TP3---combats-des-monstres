# Arthur Robin
# 11/21/2022
# Combat_de_monstres

# J'importe random et je définis mes variables
import random

niveau_de_vie = 20
numero_adversaire = 1
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0


def initialisationdelapartie():
    global nombre_victoires
# Si le nombre de victoire est plus grand que deux alors la difficulte du monstres augmente autrement le force de l'adversaire ne change pas
    if nombre_victoires >= 3:
        force_adversaire = random.randint(6, 11)
    else:
        force_adversaire = random.randint(2, 11)
# permet de donner la force de l'aversaire a l'utilisateur
    print('Vous tombez face a face avec un adversaire de difficulte:', force_adversaire)
    choix = input(
        'Que voulez vous faire ?\n1- Combattre cet adversaire \n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les rèels du jeu\n4- Quitter le jeu')
    if choix == '1':
# Permet de donner des information a l'utilisateur sur le nombre de combat effectue, les victoires, defaites, son niveau de vie, etc...
        global numero_combat, numero_adversaire, niveau_de_vie, nombre_defaites, nombre_victoires_consecutives
        print('Vous avez choisi de combattre cet adversaire\n Adversaire:', numero_adversaire,
              '\n Force de l adversaire:', force_adversaire, '\n Niveau de vie de l\'usager:', niveau_de_vie,
              '\n Combat:', numero_combat, ':', nombre_victoires, 'vs', nombre_defaites)
        score_dé = random.randint(1, 6)
        score_dé2 = random.randint(1, 6)
        final_dé = score_dé + score_dé2
        print('Lancer du dés #1:', score_dé)
        print('Lancer du dés #2:', score_dé2)
        print('Total des deux dés:', final_dé)
# si l'utlisateur gagne le combat son niveau de vie agumente et une victoires consecutives est rajoute a son palmares.
        if final_dé > force_adversaire:
            print('Vous avez gagné le combat')
            niveau_de_vie = niveau_de_vie + force_adversaire
            print('Votre niveau de vie est de:', niveau_de_vie)
            nombre_victoires_consecutives = nombre_victoires_consecutives + 1
            print('Nombre de victoires consécutives:', nombre_victoires_consecutives)
            numero_adversaire = numero_adversaire + 1
            numero_combat = numero_combat + 1
            nombre_victoires = nombre_victoires + 1
# si il perd le combat son niveau de vie diminue et le numero de combat etle numero d'adversaire augmente
        else:
            print('Vous avez perdu le combat')
            niveau_de_vie = niveau_de_vie - force_adversaire
            print('Votre niveau de vie est de:', niveau_de_vie)
            numero_adversaire = numero_adversaire + 1
            numero_combat = numero_combat + 1
            nombre_defaites = nombre_defaites + 1
            nombre_victoires_consecutives = 0
            if niveau_de_vie ⩽= 0:
                print('La partie est terminée, vous avez vaincu', nombre_victoires, 'monstres')
                niveau_de_vie = 20
# Le choix 2 fait perdre une vie a l'utlisateur car il contourne le boss
    if choix == '2':
        print('Vous avez choisi de contourner le monstre, vous allez perdre une vie')
        niveau_de_vie = niveau_de_vie - 1
        print('Votre niveau de vie est de:', niveau_de_vie)
# Le choix 3 donne les regles du jeu a l'utlisateur
    if choix == '3':
        print('Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.'
              'Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n'
              'Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.\n '
              'Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n'
              'La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n'
              'L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.')

# Cette fonction sert a demander a l'utilisateur du jeu s'il veut recommencer la partie
def recommencer():
    choix = input("Voulez vous jouer? (oui/non)")
    if choix == 'oui':
        return True
    elif choix == 'non':
        return False


def main():
    while recommencer():
        initialisationdelapartie()

# Lance le code python ! :))
main()
