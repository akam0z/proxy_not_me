#!/bin/bash

# Vérifiez si mitmproxy est installé
if ! command -v mitmproxy &> /dev/null
then
    echo "mitmproxy n'est pas installé. Veuillez l'installer avec 'pip install mitmproxy'."
    exit 1
fi

# Répertoire où le certificat sera généré
CERT_DIR="$HOME/.mitmproxy"
CERT_FILE="$CERT_DIR/mitmproxy-ca-cert.pem"

# Vérifiez si le répertoire des certificats existe, sinon, créez-le
if [ ! -d "$CERT_DIR" ]; then
    echo "Le répertoire des certificats n'existe pas. Création du répertoire..."
    mkdir -p "$CERT_DIR"
fi

# Vérifiez si le certificat existe
if [ ! -f "$CERT_FILE" ]; then
    echo "Certificat CA non trouvé. Démarrage de mitmproxy pour générer le certificat..."

    # Démarrer mitmproxy pour générer le certificat
    mitmproxy --listen-port 8080 &
    MITMPROXY_PID=$!

    echo "mitmproxy est en cours d'exécution pour générer le certificat CA. Veuillez patienter..."

    # Attendre un moment pour permettre à mitmproxy de générer le certificat
    sleep 10

    # Arrêter mitmproxy
    kill $MITMPROXY_PID 2>/dev/null

    if [ ! -f "$CERT_FILE" ]; then
        echo "Erreur : Le certificat CA n'a pas été généré. Assurez-vous que mitmproxy fonctionne correctement."
        exit 1
    else
        echo "Certificat CA généré à: $CERT_FILE"
    fi
else
    echo "Certificat CA déjà trouvé à: $CERT_FILE"
fi

# Fournir des instructions pour l'installation du certificat
OS=$(uname -s)
case "$OS" in
    Linux*)
        echo "Pour installer le certificat CA sur Linux, copiez le fichier .pem dans le répertoire des certificats de confiance de votre système."
        echo "  sudo cp $CERT_FILE /usr/local/share/ca-certificates/mitmproxy.crt"
        echo "  sudo update-ca-certificates"
        ;;
    Darwin*)
        echo "Pour installer le certificat CA sur macOS, utilisez le trousseau d'accès."
        echo "  sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain $CERT_FILE"
        ;;
    MINGW*|MSYS*|MINGW32*|MINGW64*)
        echo "Pour installer le certificat CA sur Windows, ouvrez le fichier .pem et suivez les instructions pour l'ajouter au magasin de certificats racines de confiance."
        ;;
    *)
        echo "Système d'exploitation non pris en charge pour l'installation automatique du certificat."
        ;;
esac

echo "Processus terminé. Assurez-vous d'installer le certificat CA conformément aux instructions fournies."

