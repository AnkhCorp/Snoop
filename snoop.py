import requests
from bs4 import BeautifulSoup

class TextColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    END = '\033[0m'

text = """

  .-')       .-') _                           _ (`-.  
 ( OO ).    ( OO ) )                         ( (OO  ) 
(_)---\_,--./ ,--,' .-'),-----. .-'),-----. _.`     \ 
/    _ ||   \ |  |\( OO'  .-.  ( OO'  .-.  (__...--'' 
\  :` `.|    \|  | /   |  | |  /   |  | |  ||  /  | | 
 '..`''.|  .     |/\_) |  |\|  \_) |  |\|  ||  |_.' | 
.-._)   |  |\    |   \ |  | |  | \ |  | |  ||  .___.' 
\       |  | \   |    `'  '-'  '  `'  '-'  '|  |      
 `-----'`--'  `--'      `-----'     `-----' `--'      
"""

red_text = TextColor.RED + text + TextColor.END
print(red_text)
print("Created by AnkhCorp 2.0")


def check_social_profile(platform, username):
    if platform == "instagram":
        url = f"https://imginn.com/{username}/"
        display_url = f"https://instagram.com/{username}"
    elif platform == "twitter":
        url = f"https://nitter.privacydev.net/{username}"
        display_url = f"https://x.com/{username}"
    elif platform == "youtube":
        url = f"https://youtube.com/@{username}"
        display_url = url
    elif platform == "reddit":
        url = f"https://old.reddit.com/user/{username}"
        display_url = f"https://reddit.com/user/{username}"
    elif platform == "myanimelist":
        url = f"https://myanimelist.net/profile/{username}"
        display_url = url
    elif platform == "github":
        url = f"https://github.com/{username}"
        display_url = url
    elif platform == "snapchat":
        url = f"https://www.snapchat.com/add/{username}"
        display_url = url
    elif platform == "chess":
        url = f"https://www.chess.com/member/{username}"
        display_url = url
    elif platform == "twitch":
        url = f"https://twitchtracker.com/{username}"
        display_url = f"https://twitch.tv/{username}"
    elif platform == "minecraft":
        url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
        display_url = url
    elif platform == "bitbucket":
        url = f"https://bitbucket.org/{username}"
        display_url = url
    elif platform == "9gag":
        url = f"https://9gag.com/u/{username}"
        display_url = url
    elif platform == "pastebin":
        url = f"https://pastebin.com/u/{username}"
        display_url = url
    elif platform == "redbubble":
        url = f"https://www.redbubble.com/people/{username}"
        display_url = url
    elif platform == "openstreetmap":
        url = f"https://www.openstreetmap.org/user/{username}"
        display_url = url
    elif platform == "patreon":
        url = f"https://www.patreon.com/{username}"
        display_url = url
    elif platform == "pensador":
        url = f"https://www.pensador.com/autor/{username}"
        display_url = url
    elif platform == "vsco":
        url = f"https://vsco.co/{username}/gallery"
        display_url = url
    elif platform == "tiktok":
        url = f'https://tiktok.wpme.pl/@{username}'
        display_url = f'https://tiktok.com/@{username}'
        return check_tiktok_profile(url, display_url)
    else:
        return None

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return display_url
    elif response.status_code == 404:
        return 404
    elif response.status_code == 429:
        return 404
    elif response.status_code == 304:
        return 304 
    else:
        return None


def check_tiktok_profile(url, display_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if "API error code 10 (EMPTY_RESPONSE)" in soup.text:
            return display_url 
        elif "API error code 10221 (USER_BAN)" in soup.text:
            return 404  
        else:
            return None  # Erro desconhecido ou código não encontrado
    else:
        return None


# Lista de plataformas
platforms = [
    "instagram", "twitter", "youtube", "reddit", "myanimelist", "github", "snapchat",
    "chess", "twitch", "minecraft", "bitbucket", "9gag", "pastebin",
    "redbubble", "openstreetmap", "patreon", "pensador", "vsco", "tiktok"
]

username = input(f"{TextColor.RED}Username: {TextColor.END}")
profile_found = False

for platform in platforms:
    result = check_social_profile(platform, username)

    if result == 404:
        print(f"{TextColor.RED}Perfil não encontrado no {platform.capitalize()} (Status 404){TextColor.END}")
    elif isinstance(result, str):
        print(f"{TextColor.GREEN}Perfil encontrado no {platform.capitalize()}: {result}{TextColor.END}")
        profile_found = True
    else:
        print(f"{TextColor.YELLOW}Status do código {platform.capitalize()}: Erro desconhecido ou código não encontrado{TextColor.END}")

if not profile_found:
    print(f"{TextColor.RED}Nenhum perfil encontrado.{TextColor.END}")
else:
    print(f"{TextColor.GREEN}Processo concluído com perfis encontrados.{TextColor.END}")
