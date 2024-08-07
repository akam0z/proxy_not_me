# proxy_not_me

![TeXt Theme](https://raw.githubusercontent.com/akam0z/proxy_not_me/main/proxy_not_me.png)

C'est un proxy minimaliste qui a pour but de servir de base pour toute personne voulant un proxy sur mesure. Le code est très facile à prendre en main grâce à sa taille réduite.

pour l'instant :

- réduire le fingerprinting
- bloque les traker
- chiffre le trafique
- Bloquer les tracking pixels

a venir :

- bloque tout les traker grace a des filtre EASYlist
- Intégration d'une IA de reconnaissance des trackers
- bloque les pub
- Interface pour rendre plus facile l'ajout d'options supplémentaires
  
## Installation

Pour installer les dépendances nécessaires, exécutez la commande suivante :

```
pip install mitmproxy
```

## Démarrage

Pour démarrer le proxy, utilisez la commande suivante :

```
mitmproxy --mode regular@8082 -s ProxyServer.py
```

## Configuration du navigateur

Pour que votre navigateur fonctionne avec le proxy, suivez ces étapes :

- **Configurer le Proxy** : Paramétrez votre navigateur pour passer par le proxy en utilisant l'adresse `localhost` et le port `8082`.
- **Certificat** : Intégrez le certificat de mitmproxy dans votre navigateur pour éviter les erreurs de certificat SSL. Vous pouvez télécharger le certificat depuis [http://mitm.it](http://mitm.it) lorsque mitmproxy est en cours d'exécution.

## Instructions pour différents navigateurs

### Google Chrome

1. Ouvrez les paramètres de Chrome et allez dans la section "Avancé".
2. Sous "Système", cliquez sur "Ouvrir les paramètres de proxy".
3. Configurez le proxy en entrant `localhost` et `8082` comme adresse et port respectivement.
4. Pour ajouter le certificat, allez dans "Paramètres", "Avancé", "Gérer les certificats" et importez le certificat téléchargé depuis [http://mitm.it](http://mitm.it).

### Mozilla Firefox

1. Ouvrez les préférences de Firefox et allez dans la section "Général".
2. Faites défiler jusqu'à "Paramètres réseau" et cliquez sur "Paramètres...".
3. Sélectionnez "Configuration manuelle du proxy" et entrez `localhost` et `8082`.
4. Pour ajouter le certificat, allez dans "Préférences", "Vie privée & Sécurité", "Certificats" et importez le certificat téléchargé depuis [http://mitm.it](http://mitm.it).

## Contributions

Les contributions sont les bienvenues ! Si vous avez des idées d'amélioration ou des corrections, n'hésitez pas à soumettre une pull request ou à ouvrir une issue.

## YouTube

https://youtu.be/hKBtbS_8Xs8?si=HoC8Edl9b8llEImu

## Discord

- Pseudo : Akam0z
- Serveur Discord où je suis présent : https://discord.gg/cgtkxePNYx
