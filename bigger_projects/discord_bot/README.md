# discord bot

### installation de la bibliothèque discord
dans le terminal, tapez :
```shell
pip install discord
```

### Creation d'une application discord

Afin de créer le bot discord, il est nécéssaire de se rendre ici :  
`https://discord.com/developers/applications`  
de se logger si ce n'est pas fait.  
ici on pourra cliquer sur _new application_ et on lui donnera un nom.

#### Creation du bot

A présent que l'application est crée, on va dans l'onglet bot, ici on peut changer 
le nom du bot et lui donner une image. une fois cela sauvegarder on pourra rénitialiser
le token.

Pour des raisons de sécurité il est aussi nécéssaire d'activer _message content intent

### créer l'authentification pour l'acces du bot

dans l'onglet Oauth2, on va selectionner le scopes:
- bot
- et on va mettre toutes les permissions text
cela va générer un lien d'authentification du bot au bas de la page 

on va copier coller ce lien dans le navigateur, ca va ouvrir discord et nous demander
d'ajouter ce bot a un server discord. 

A ce stade le bot est présent, c'est le code qui fera les fonctionnalités de celui ci.

