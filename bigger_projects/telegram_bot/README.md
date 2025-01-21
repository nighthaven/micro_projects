# telegram bot

# prerequis

Afin de pouvoir créer ce bot, nous avons bien sur besoin de télégram.

#### la bibliothèque python-telegram-bot
pour l'installer, dans le terminal tapez 
```shell
pip install python-telegram-bot
```

Nous avons aussi besoin de BotFather, pour l'obtenir, 
on va simplement taper botfather dans la barre de recherche de l'application télégram
on verra un bouton start, une fois ce bouton validé, botfather nous donnera toutes une
serie de commande.

### creer le bot

on va selectionner `/newbot` puis répondre au questions posé.
Une fois le nom du bot choisis, botfather devrait dans son message nous donner un token,
ce token sera une constante de notre code.

de plus une constante sera le nom d'utilisateur du bot qu'il faudra précédé d'un @
par exemple : `@nom_de_utilisateur_bot`

Une fois ces deux constantes mise dans le code, on peut rechercher dans la barre de recherche
de télégramme le nom de notre bot afin de le trouver. de meme on cliquera sur start
afin de garder un oeil sur les réactions du bot pendant la programmation. 

### définir l'image de notre bot

Afin de définit une image de bot, on va selectionner `/setuserpic` puis on va mettre le nom de 
notre bot a nouveau avec `@nom_de_utilisateur_bot` puis on mettra l'image.

### définir un à propos

pour cela on fait `/setabouttext`, pareil on met  `@nom_de_utilisateur_bot` puis le texte.

### définir une description

pour cela on fait `/setdescription`

### définir un groupe

pour cela on fait `/setjoingroup` ce qui permettra a notre bot d'etre ajouté à un/des groupes
par default c'est activé mais on peut le désactiver si on souhaite empecher cela.

### définir les commandes

pour cela on fait `/setcommands`.
une fois notre bot selectionner, 
on doit faire la syntaxe :  
`command1 - Description`  
`command2 - Description`  
etc...  
par exemple  
`
start - Start the bot
help - type something to chat with the bot
custom - this is a custom command
`
on peut changer cela a n'importe quel moment dans notre programme

en tapant dans le menu du bot on verra les commandes crée.  
l'application de ces commandes se fera via notre code. 