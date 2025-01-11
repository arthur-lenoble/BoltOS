import os

# Dictionnaire des sites enregistrés
registered = {
    'google': 'Google\nhttps://www.google.com',
    'chatgpt': 'ChatGPT\nhttps://www.chatgpt.com',
    'wikipedia': 'Wikipedia : l\'encyclopédie libre\nhttps://fr.wikipedia.org',
    'jeux': 'Crazy Games\nhttps://www.crazygames.com',
    'canva': 'Canva\nhttps://www.canva.com',
    'youtube': 'YouTube\nhttps://www.youtube.com',
    'github': 'GitHub\nhttps://www.github.com',
    'stackoverflow': 'Stack Overflow\nhttps://www.stackoverflow.com',
    'reddit': 'Reddit\nhttps://www.reddit.com',
    'linkedin': 'LinkedIn\nhttps://www.linkedin.com',
    'amazon': 'Amazon\nhttps://www.amazon.com',
    'twitter': 'Twitter\nhttps://www.twitter.com',
    'instagram': 'Instagram\nhttps://www.instagram.com',
    'facebook': 'Facebook\nhttps://www.facebook.com',  # Correction du lien
    'trad': 'Google Traduction\nhttps://translate.google.fr\n\nDeepL\nhttps://www.deepl.com',
    'trinket': 'Trinket\n(strongly recommended)\nhttps://www.trinket.io'
}

def dictSearch(entree):
    """Recherche les entrées correspondant à l'entrée utilisateur."""
    found = False
    for key, value in registered.items():
        if entree in key:  # Recherche partielle au lieu de startswith
            print(value)
            found = True
    if not found:
        print('Rien ne correspond à votre recherche...')

# Boucle principale
while True:
    try:
        search = input('🔎')
        search.lower()
        if not search:  # Vérifie si l'entrée est vide
            print("Veuillez entrer un mot-clé valide.")
            continue

        os.system('cls' if os.name == 'nt' else 'clear')  # Compatible Windows et Unix
        print('🔎'+search)
        dictSearch(search)

        # Suggestions basées sur le contenu
        suggestions = {
            'goo': 'Essayez Google',
            'je': 'Essayez Jeux',
            'cha': 'Essayez ChatGPT',
            'w': 'Essayez Wikipedia',
            'ca': 'Essayez Canva',
            'y': 'Essayez YouTube',
            'gi': 'Essayez GitHub',
            's': 'Essayez Stack Overflow'
        }
        for key, suggestion in suggestions.items():
            if key in search:
                print(suggestion)

    except Exception as e:
        print("Une erreur s'est produite")

    finally:
        print("C'est tout pour l'instant !")
