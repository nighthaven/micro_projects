## url_shortener

### prérequis

Pour ce projet nous allons utiliser une API externe dont voici le lien:   
https://cutt.ly
il faudra donc créer un compte et/ou se connecter 

#### récuperer la key de l'API
puis aller dans la section API puis API key. Il faudra alors cliquer à droite dans 
manage APIkey puis generate/change the API key et valider.
Une fois la clef visible on pourra la copier coller dans le projet dans une variable 

#### récupérer l'URL

Dans la section API on peut voir Documentation API, dedans on pourra voir l'url a utiliser  
https://cutt.ly/api/api.php (au moment ou cette documentation est écrite)

Voici la documentation si nécéssaire : https://cutt.ly/api-documentation/regular-api

#### la bibliothèque requests
pour la télécharger il faudra taper dans le terminal 
```shell
pip install requests
```