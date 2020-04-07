# Lien Interne

## Idée Générale :
  L'idée c'est de fournir une syntaxe brève, afin de pouvoir écrire des liens internes vers des ressources de notre système,ainsi quand on parse du text contenant #TYPENUMERO c'est remplacé par un lien vers 
  l'objet de type TYPE et d'ID NUMERO en fonction du type de l'objet c'est le mode preview ou accès  standard comme dans le cas d'une demande.
  
  - Des activités (#A_ID_activity)
  - Des évaluations (#E_ID_eval)
  - Des exercices (#X_ID_exo)
  - Des AAV (#V_ID_AAV)     (tout AAV est une réponse dans un QA)
  - Des QA  (#Q_ID_QA)
  - Des utilisateurs (@User)
  - Des cercles (@0_Cercle)
  
 

Les liens internes seront surtout utilisés dans les AAV et QA.

## Obtention des liens internes :
  Il doit être possible de récupérer le lien interne d'une ressource.

## Syntaxe proposée :
  
Le mieux est de pouvoir référencer tout ce qui concerne des personnes avec `@` suivit du nom de la personne / groupe :

* `@qcoumes`
* `@admin`
* `@AP1_2019`
* `@editor`
* ...

et les objets avec `#` suivit de l'ID de l'objet (`#21`). Il n'est pas forcément nécessaire de différencier l'objet si ceux si possède chacun une clé unique.

