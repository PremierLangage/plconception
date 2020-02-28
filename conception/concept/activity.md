
# Activité

Une activité est une Ressource.
Elle est transformée en asset à la ajout dans une classe.

Une activité peut être utilisé dans plusieurs cours, mais il existe une instance distincte dans chaque cours. 

Une activité  est définie par un fichier au format pl contenant des références d'exercices, et une balise **runner** inidiquant sont comportement. 

Une activité a un barème (outil permettant le calcul d'une note).

Activité= P O S F E  I N B  (spécial: sd* td*) 
i=introduction  
S= Strategie   
F= pltp  (ensembles de référence d'exercices ou d'activités)
N=navigation  
B=Barem (comment est calculé la nte qui remonte à moodle)
E=aquisitor (permet de calculer l'aquisition de l'activité) 
R=Runner (permet de calculer le chemin suivi par l'apprenant)

En discution: Défini dans la ressource ou dans l'asset ? Fonction de du cours ? 
P= Prérequis 
O= Objectifs (AAV et ontologie)

CHANGEMENT les éléments suivant ne sont plus intégrés dans toutes les activités. 
Une activité exporte des tableaux de bord : studentactivitydashboard, teacheracivitydashboard utilisables dans les tableaux de bords correspondants.
sd=student dashboard  
td=teacher dashboard  
Une version simplifié sera proposé sur la base de l'aquisition de l'activité.

## Aquisition

une activité réussie par un utilisateur et dite aquise. C'est l'activité qui défini cet état de fait.




## LTI et activités

L'activité est l'unité de partage entre les LMS (moodle and co) et PL, mais l'avtivité doit être associé à un cours visible du MLS et de PL.

FIXME Une activité à une URL qui peut être utilisé dans le connecteur LTI.  Le connecteur LTI définie un identifiant externe qui est utilisé pour identifier l'activité dans PL.


