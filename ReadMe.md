# Evaluation  Conception d'une solution embarquée en temps réel.
## Marfella Julien EPSI I1 Dev 2021/2022

Dans un premier temps j'ai entamé la réalisation un diagramme d'éxecution des tâches accessible ici : https://docs.google.com/spreadsheets/d/1bnxp9DJ6vrcVCnCS7RfIDIXU48O4VAlR2Hfbt3J1KhM/edit?usp=sharing
Ce diagramme m'a permis de me rendre compte rapidement que les temps d'éxecutions de chaques tâches étaient vraiment très court ainsi que les périodes qu'elles sont sensés respectés pour se relancer à nouveau.

J'ai donc eu l'intuition que le système avec ces paramètres ne pourrait certai nement pas fonctionner.

De plus, en caclulant la valeur de U on obtient le résultat suivant :
U = 2/5 + 3/15 + 5/5 + 3/5 = 2.2

On obtient donc un U supérieur à 1, ainsi nous savons que le système n'est pas possible en raison d'une surcharge.

J'ai donc fait le choix de remplir mon réservoir au maximum et une fois plein les machines peuvent produire leurs objets respectifs
Le programme fonctionnant alors pendant 2 minutes