

# Les Stats de PL

le statistiques sont une *application django* dans le serveur Premier Langage.

Essentiellement basée sur la table answers de l'application playexo. 

## La table playexo.anwser 

https://github.com/PremierLangage/premierlangage/blob/master/server/serverpl/playexo/models.py
```python
    answers = JSONField(default='{}')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pl = models.ForeignKey(PL, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, null=True, on_delete=models.CASCADE)
    seed = models.CharField(max_length=100, default=time.time)
    date = models.DateTimeField(default=timezone.now)
    grade = models.IntegerField(null=True)
```
## La table playexo.anwser 

answers :  Réponse de l'apprenant sous forme d'un JSON,permet de faire un post traitement, par défaut vide 
user : un identifiant dans la table des utilisateurs 
pl : un identifiant dans la table des exercices 
activity: un identifiant dans la table des activités
seed: la valeur de la seed  pour le générateur aléatoire de la question, -1 si pas de seed
date= nanoseconde de la sauvegarde dans la base ?
