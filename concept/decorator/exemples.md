
# Quelques décorateurs 

## La familles des parametreurs 

Les parametreurs permettent de changer une des balise de l'exercice. Ils ne change pas le comportement d'évaluation de l'exercice.


Par exemple:

```
  deco.before.seed==
  seed=12
  ==

  deco.before.listseed==
  import random
  seed=random.choice([12,4,56,1000,14,7,17,1789789])
  ==

  deco.before.enonce==
  text="""
  LE nouvel énoncé de cet exercice
  """
  ==
```

## Famille des feedback 

Les décorateurs de la famille des feedback agissent sur le résultat de l'exercice.
```
  deco.after.setfeedback==
  if not grade['success']:
    grade['feedback']="""et bien non bannane c'est pas ça""" # pas très gentil comme feedback 
  ==

  deco.after.coolification==
  grade['feedback']= "Cool".join(grade['feedback'].split("Bonne réponse"))
  ==
```


