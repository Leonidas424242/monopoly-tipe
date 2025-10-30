# TIPE – Monopoly   

**Auteur :** Louis Fonteniaud  
**École :** CentraleSupélec (TIPE 2024–2025)  

---

## Sujet du projet  
Simulation et modélisation probabiliste du jeu **Monopoly**.  
L’objectif est d’étudier la dynamique du jeu à l’aide des **chaînes de Markov**, de déterminer la **distribution de probabilité des cases visitées** et d’identifier les **quartiers les plus rentables** selon différentes stratégies (prudente vs risquée).

---

## Contenu du projet  
Le projet s’articule autour de plusieurs étapes :  
1. **Modélisation mathématique du plateau** sous forme de chaîne de Markov à 43 états.  
2. **Construction de la matrice de transition**, intégrant :
   - les lancers de dés,  
   - les cartes “Chance” et “Caisse de communauté”,  
   - les passages et séjours en prison,  
   - la règle des trois doubles.  
3. **Étude spectrale de la matrice** : valeurs propres, stabilité et distribution stationnaire.  
4. **Implémentation Python** pour générer, composer et simuler les matrices.  
5. **Analyse des stratégies** :
   - *Stratégie Sécurité* : minimisation du risque de prison et gestion prudente des achats.  
   - *Stratégie Risque* : maximisation des gains en ciblant les zones les plus fréquentées.

---

## Principaux résultats  
- La distribution stationnaire converge vers un vecteur de probabilité propre.  
- Les **quartiers orange et rouge** apparaissent comme les plus rentables à long terme.  
- Les résultats sont cohérents avec les études statistiques du jeu publiées dans la littérature.  

---

## Méthodes et outils utilisés  
- **Python**, **NumPy**, **Matplotlib**  
- Calcul matriciel, valeurs propres, simulation Monte Carlo  
- Théorie des **chaînes de Markov** et convergence stochastique