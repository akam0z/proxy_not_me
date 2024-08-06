# proxy_not_me
# Installation

Pour installer les dépendances nécessaires, exécutez la commande suivante :

```
pip install mitmproxy
```

Démarrage

Pour démarrer le proxy, utilisez la commande suivante :

```
mitmproxy --mode regular@8082 -s ProxyServer.py
```

# Configuration du navigateur

Pour que votre navigateur fonctionne avec le proxy, suivez ces étapes :

    - Configurer le Proxy : Paramétrez votre navigateur pour passer par le proxy en utilisant l'adresse localhost et le port 8082.
    - Certificat : Intégrez le certificat de mitmproxy dans votre navigateur pour éviter les erreurs de certificat SSL. Vous pouvez télécharger le certificat depuis http://mitm.it lorsque mitmproxy est en cours d'exécution.

# Instructions pour différents navigateurs
# Google Chrome

    Ouvrez les paramètres de Chrome et allez dans la section "Avancé".
    Sous "Système", cliquez sur "Ouvrir les paramètres de proxy".
    Configurez le proxy en entrant localhost et 8082 comme adresse et port respectivement.
    Pour ajouter le certificat, allez dans "Paramètres", "Avancé", "Gérer les certificats" et importez le certificat téléchargé depuis http://mitm.it.

# Mozilla Firefox

    Ouvrez les préférences de Firefox et allez dans la section "Général".
    Faites défiler jusqu'à "Paramètres réseau" et cliquez sur "Paramètres...".
    Sélectionnez "Configuration manuelle du proxy" et entrez localhost et 8082.
    Pour ajouter le certificat, allez dans "Préférences", "Vie privée & Sécurité", "Certificats" et importez le certificat téléchargé depuis http://mitm.it.


Contributions

Les contributions sont les bienvenues ! Si vous avez des idées d'amélioration ou des corrections, n'hésitez pas à soumettre une pull request ou à ouvrir une issue.

# youtube :
https://youtu.be/hKBtbS_8Xs8?si=HoC8Edl9b8llEImu

# discorde 
pseudo : Akam0z
serveur discorde ou je suis present : https://discord.gg/cgtkxePNYx

