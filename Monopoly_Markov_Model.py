import numpy as np 
import numpy.linalg as alg


## Initialisation du programme ##


def CalculProbaLancer ():
    ProbaLancer = [1,2,3,4,5,6,5,4,3,2,1]
    ProbaLancer = [x / 36 for x in ProbaLancer]
    return (ProbaLancer)


#Fonction permettant la création de MatriceLancers :

                                                            # CreationMatrice ne modifie que les colonnes de 2 à 40
def CreationMatrice (proba, matrice, dim, compteur):        # Compteur sert à compter les étapes et ça s'arrête une fois qu'on a effectué autant d'étapes qu'il y a de lignes dans la matrice
    if compteur == dim:
        return (matrice)

    dernierElement = proba.pop()                        
    proba = [dernierElement] +proba                         # On ajoute la dernière proba au début de la liste des probas (revient à effectuer un translation pour caractériser le déplacement du pion d'une case )
    matrice[:,compteur] = proba                             # La compteur+1 ème colonne est changée en la liste des probas modifiée à chaque passage dans la fonction (change avec le compteur)
    CreationMatrice (proba, matrice, dim, compteur+1)

                                                                                                                                   
#####################################################################################################################################

    
## Création MatriceLancers ##
    
ProbasCaseGo = [0]*40                                       # Initialisation de la liste des probabilités d'atteindre chacune des cases
ProbasCaseGo[2:13] = CalculProbaLancer()                    # On modifie ces probas en fonctions des résultats obtenables grâce aux lancers de dés
MatriceLancers = np.zeros((40, 40))
MatriceLancers[:,0] = ProbasCaseGo                          # On modifie la première colonne (cf. matrice de transition Markov)
CreationMatrice(ProbasCaseGo, MatriceLancers, 40, 1)
                      
## Rester en prison ##


MatriceLancers = np.column_stack((MatriceLancers, ([0] *40)))       # On modélise le fait de pouvoir rester ou non en prison par l'extension du nombre de cases de 2 : dimension de la matrice +2 
MatriceLancers = np.column_stack((MatriceLancers, ([0] *40)))

MatriceLancers = np.row_stack((MatriceLancers, ([0] *42)))
MatriceLancers = np.row_stack((MatriceLancers, ([0] *42)))


MatriceLancers[41,40] = 5/6                               # On rajoute 5/6 à la 42ème ligne 41ème colonne : on a une proba de 5/6 de ne pas faire de double et ainsi ne pas bouger
MatriceLancers[10,41] = 5/6                               # On rajoute 5/6 à la 11ème ligne 42ème colonne : quand on sort de prison, on ressort par la case Simple Visite

## Les doubles permettant de sortir de prison ##


MatriceLancers[[12,14,16,18,20,22],40] = 1/36             # Les doubles possibles sont 2,4,6,8,10,12 et comme on sort par la case Simple Visite, on ajoute les scores à 10 (numéro de case correspondante ) 
MatriceLancers[[12,14,16,18,20,22],41] = 1/36             # Deuxième cas si on en est à son deuxième tour en Prison (proba de 1/36 pour chacun des doubles obtenus car on en a 6)

                                                                                                                                
#######################################################################################################################################


## Création de la MatriceAllezPrison ##

MatriceAllezPrison = np.eye(42)

# Envoyer le joueur dans la première partie de la prison 

MatriceAllezPrison[40,30] = 1 
MatriceAllezPrison[30,30] = 0

#######################################################################################################################################



## Règles de trois doubles-> Prison ##

# Matrice ne pas faire de doubles trois fois de suite 


MatriceTroisDoublesPrison=np.eye(42)*(215/216)          #On reste sur la case sur laquelle on est avec une proba de 215/216


# Probabilité de 1/216 d'aller en prison quand on est sur n'importe quelle case


MatriceTroisDoublesPrison[41,[range(0,40)]]=1/216
MatriceTroisDoublesPrison[30,30]=0                      #Quand on est sur la case 30 : on ne reste pas sur la case 30
MatriceTroisDoublesPrison[40,30]=1                      #Quand on est sur la case 30 : on on a une proba de 1 d'aller sur la case 40 en prison

MatriceTroisDoublesPrison[41,41]=1                      #On ignore les effets de la règle des doubles pour sortir de prison déjà pris en compte dans la matrice MatriceLancers
MatriceTroisDoublesPrison[40,40]=1                      #ie : quand on est en prison, on reste en prison !
                                                                                                                                    
######################################################################################################################################

## Création MatriceChance ##->Cartes chance aux positions 7,22 et 36


# Envoie à la case départ
# Envoie en prison
# Envoie vers l'avenue Henri-Martin
# Envoie vers le boulevard de la Villette  
# Envoie vers la rue de la Paix
# Envoie vers la gare de Lyon
# Reculer de 3 cases


MatriceChance = np.eye(42)

MatriceChance[:,7] = [0]*42
MatriceChance[[0, 40, 24, 11, 39, 15, 4],7] = 1/16                # On affecte à chacun une proba de 1/16 : dans l'ordre : [Départ, Prison, Henri-Martin, la Villette, Paix, gare de Lyon, reculer de 3 cases]
#On retire les lignes suivantes provenant du Monopoly anglais
#MatriceChance[15,7] = 2/16                                 # Proba qui provient des 2 cartes chances qui emmènent à la gare la plus proche (en l'occurence la case 15)
#MatriceChance[7,7] = 6/16                                  # Proba qui provient des 6 cartes chances qui ne modifient pas la position du joueur
MatriceChance[7,7] = 9/16



MatriceChance[:,22] = [0]*42
MatriceChance[[0, 40, 24, 11, 39, 15, 19],22] = 1/16
#MatriceChance[25,22] = 2/16                                # Proba qui provient des 2 cartes chances qui emmènent à la gare la plus proche (en l'occurence la case 25)
MatriceChance[22,22] = 9/16                                # Proba qui provient des 6 cartes chances qui ne modifient pas la position du joueur

MatriceChance[:,36] = [0]*42
MatriceChance[[0, 40, 24, 11, 39, 15, 33], 36] = 1/16
#MatriceChance[5,36] = 3/16
MatriceChance[36,36] = 9/16                                # Proba qui provient des 6 cartes chances qui ne modifient pas la position du joueur

                                                                                                                            
#########################################################################################################################################


## Création MatriceCom ##->Caisses communautés aux positions 2,17 et 33


# Envoie à la case départ
# Envoie en prison
#il faut aussi prndre en compte le fait qu'une carte invite à tirer un carte chance impliquant un éventuelle redirection

MatriceCom = np.eye(42)

MatriceCom[[0,40],2] = 1/16 + 1/256                 #On ajoute les probas liées au fait de retourner à la case départ ou en prison via carte chance
MatriceCom[2,2] = 13/16 + 9/256                     #On rajoute la proba de ne pas bouger en tirant la carte communauté qui nous fait tirer une carte chance
MatriceCom[[24, 11, 15],2] = 1/256                  #deux cartes chances peuvent m'emener case 39
MatriceCom[39,2] = 2/256

MatriceCom[[0,40],17] = 1/16 + 1/256
MatriceCom[17,17] = 13/16 + 9/256
MatriceCom[[24, 11, 39, 15, 14], 17] = 1/256

MatriceCom[0,33] = 1/16 + 1/256
MatriceCom[33,33] = 13/16
MatriceCom[40,33] = 1/16 + 2/256
MatriceCom[[24, 11, 39, 15], 33] = 1/256
                                                                                                                                    

########################################################################################################################################


MatriceFinale = np.dot(np.dot(np.dot(np.dot(MatriceCom, MatriceChance), MatriceAllezPrison), MatriceLancers), MatriceTroisDoublesPrison)        # On multiplie entre elles toutes les matrices créées
MatriceDesVecteursPropres = alg.eig(MatriceFinale)[1]                                           # On extrait la matrice dont la ième colonne représente le vecteur propre associé à la ième valeur propre
VecEtatStationaire = MatriceDesVecteursPropres[:,0]                                             # On extrait le vecteur propre associé à la valeur propre 1

VecEtatStationaire = VecEtatStationaire/sum(VecEtatStationaire)                                 # Pour que ce vecteur soit considéré comme un vecteur de probabilité, il est nécessaire de normaliser

for i in range(len(VecEtatStationaire)):
    
    print (i,end="")
    print(VecEtatStationaire[i])


