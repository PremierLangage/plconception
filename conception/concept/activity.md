
# Activité

Une activité est une Ressource.
Elle est transformée en asset à la ajout dans une classe.

Une activité peut être utilisé dans plusieurs cours, mais il existe une instance distincte pour chaque cours. 

Une activité contient à minima une Stratégie standard et au moins un fichier pltp.

Une activité exporte des tableaux de bord : studentactivitydashboard, teacheracivitydashboard utilisables dans les tableaux de bords correspondants.

une activité a une navigation 
Une activité a un barème (outil permettant le calcul d'une note).

Activité= P O S F*+ E  I N B  (spécial: sd* td*) 
i=introduction  
S= Strategie   
F= pltp  
N=navigation  
B=Barem (comment est calculé la nte qui remonte à moodle)
E=Evaluator (permet de calculer la validation de l'activité) 

En discution: Défini dans la ressource ou dans l'asset ? Fonction de du cours ? 
P= Prérequis 
O= Objectifs (AAV et ontologie)

CHANGEMENT les deux éléments suivant ne sont plus intégrés dans toutes les activités. 
sd=student dashboard  
td=teacher dashboard  


Références : modules WIMS

## LTI et activités

L'activité est l'unité de partage entre les LMS (moodle and co) et PL, mais l'avtivité doit être associé à un cours visible du MLS et de PL.

FIXME Une activité à une URL qui peut être utilisé dans le connecteur LTI.  Le connecteur LTI définie un identifiant externe qui est utilisé pour identifier l'activité dans PL.


