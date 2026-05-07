import requests
from bs4 import BeautifulSoup

class TextColor:
    RED_1 = '\033[38;5;196m'
    RED_2 = '\033[38;5;160m'
    RED_3 = '\033[38;5;124m'
    RED_4 = '\033[38;5;88m'
    RED_5 = '\033[38;5;52m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    ORANGE = '\033[38;5;208m'
    END = '\033[0m'

text = rf"""
{TextColor.RED_1}  .-')       .-') _                           _ (`-.  
{TextColor.RED_1} ( OO ).    ( OO ) )                         ( (OO  ) 
{TextColor.RED_2}(_)---\_,--./ ,--,' .-'),-----. .-'),-----. _.`     \ 
{TextColor.RED_2}/    _ ||   \ |  |\( OO'  .-.  ( OO'  .-.  (__...--'' 
{TextColor.RED_3}\  :` `.|    \|  | /   |  | |  /   |  | |  ||  /  | | 
{TextColor.RED_3} '..`''.|  .     |/\_) |  |\|  \_) |  |\|  ||  |_.' | 
{TextColor.RED_4}.-._)   |  |\    |   \ |  | |  | \ |  | |  ||  .___.' 
{TextColor.RED_4}\       |  | \   |    `'  '-'  '  `'  '-'  '|  |      
{TextColor.RED_5} `-----'`--'  `--'      `-----'     `-----' `--'      {TextColor.END}
"""

print(text)
print("Created by AnkhCorp 2.1")


def check_social_profile(platform, username):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Snoop/2.1"
    }

    if platform == "instagram":
        display_url = f"https://instagram.com/{username}"
        return check_instagram_profile(username, display_url)
    elif platform == "twitter":
        display_url = f"https://x.com/{username}"
        return check_twitter_profile(username, display_url)
    elif platform == "youtube":
        url = f"https://youtube.com/@{username}"
        display_url = url
    elif platform == "reddit":
        display_url = f"https://reddit.com/user/{username}"
        return check_reddit_profile(username, display_url)
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
        display_url = f"https://vsco.co/{username}"
        return check_vsco_profile(username, display_url)
    elif platform == "tiktok":
        url = f'https://www.tikwm.com/api/user/info?unique_id={username}'
        display_url = f'https://tiktok.com/@{username}'
        return check_tiktok_profile(url, display_url)
    elif platform == "rapfame":
        url = f'https://rapfame.app/user/{username}'
        display_url = url
    elif platform == "telegram":
        display_url = f"https://t.me/{username}"
        return check_telegram_profile(username, display_url)
    elif platform == "linktree":
        url = f"https://linktr.ee/{username}"
        display_url = url
    elif platform == "gravatar":
        url = f"https://en.gravatar.com/{username}.json"
        display_url = f"https://en.gravatar.com/{username}"
    elif platform == "keybase":
        url = f"https://keybase.io/{username}"
        display_url = url
    elif platform == "roblox":
        display_url = f"https://www.roblox.com/user.aspx?username={username}"
        return check_roblox_profile(username, display_url)
    elif platform == "about.me":
        url = f"https://about.me/{username}"
        display_url = url
    else:
        return None

    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        return None

    if response.status_code == 200:
        return display_url
    elif response.status_code == 404:
        return 404
    elif response.status_code == 429:
        return 404
    elif response.status_code == 304:
        return 304
    elif response.status_code == 500:
        return 404
    else:
        return None


def check_tiktok_profile(url, display_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        return None

    if response.status_code == 200:
        try:
            data = response.json()
            if data.get('code') == 0:
                return display_url
            elif data.get('code') == -1:
                return 404
            else:
                return None
        except ValueError:
            return None
    else:
        return None

def check_reddit_profile(username, display_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Snoop/2.1'
    }
    url = f"https://www.reddit.com/user/{username}/about.json"
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        return None

    if response.status_code == 200:
        try:
            data = response.json()
            if 'error' in data:
                return 404
            elif data.get('data', {}).get('is_suspended', False):
                return 404
            else:
                return display_url
        except ValueError:
            return None
    elif response.status_code == 404 or response.status_code == 403:
        return 404
    else:
        return None

def check_twitter_profile(username, display_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }
    
    try:
        url = f"https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names={username}"
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200:
            data = res.json()
            if isinstance(data, list) and len(data) > 0:
                return display_url
            elif isinstance(data, list) and len(data) == 0:
                return 404
    except Exception:
        pass

    NITTERS = [
        "https://nitter.poast.org",
        "https://nitter.cz",
        "https://nitter.privacydev.net",
        "https://nitter.unixfox.eu",
        "https://nitter.moomoo.me",
        "https://nitter.catsarch.com",
        "https://nitter.net"
    ]
    
    for instance in NITTERS:
        url = f"{instance}/{username}"
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                if 'User not found' in response.text or 'Profile not found' in response.text or 'not found' in response.text.lower():
                    return 404
                if f"(@{username.lower()})" in response.text.lower():
                    return display_url
                continue
            elif response.status_code == 404:
                return 404
        except requests.exceptions.RequestException:
            continue
            
    return None

def check_telegram_profile(username, display_url):
    url = f"https://t.me/{username}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_title = soup.find('meta', property='og:title')
            if meta_title and meta_title.get('content') == 'Telegram':
                return 404
            if soup.find('div', class_='tgme_page_title'):
                return display_url
            return 404
        return 404
    except Exception:
        return None

def check_roblox_profile(username, display_url):
    url = f"https://api.roblox.com/users/get-by-username?username={username}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('success') is False or 'errorMessage' in data:
                return 404
            return display_url
        return 404
    except Exception:
        return None

def check_roblox_profile(username, display_url):
    url = "https://users.roblox.com/v1/usernames/users"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "usernames": [username],
        "excludeBannedUsers": False
    }
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        if res.status_code == 200:
            data = res.json()
            if data.get("data") and len(data["data"]) > 0:
                user_id = data["data"][0]["id"]
                return f"https://www.roblox.com/users/{user_id}/profile"
            return 404
        elif res.status_code == 404:
            return 404
    except Exception:
        pass
        
    return None

def check_vsco_profile(username, display_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    
    # 1. API Direta
    api_url = f"https://vsco.co/api/2.0/sites?subdomain={username}"
    try:
        res = requests.get(api_url, headers=headers, timeout=5)
        if res.status_code == 200:
            data = res.json()
            if data.get("sites") and len(data["sites"]) > 0:
                return display_url
            return 404
        elif res.status_code == 404:
            return 404
    except Exception:
        pass

    # 2. Site Principal
    url = f"https://vsco.co/{username}"
    try:
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200:
            if '<title>Page Not Found' in res.text or 'Page not found' in res.text:
                return 404
            return display_url
        elif res.status_code == 404:
            return 404
    except Exception:
        pass
        
    # 3. AllOrigins Proxy Bypasser (Contorna Cloudflare Local)
    try:
        proxy_url = f"https://api.allorigins.win/get?url=https://vsco.co/{username}"
        res = requests.get(proxy_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if res.status_code == 200:
            data = res.json()
            status_code = data.get("status", {}).get("http_code")
            if status_code == 200:
                contents = data.get("contents", "")
                if '<title>Page Not Found' in contents or 'Page not found' in contents:
                    return 404
                return display_url
            elif status_code == 404:
                return 404
    except Exception:
        pass
        
    # 4. CodeTabs Proxy Bypasser
    try:
        proxy2 = f"https://api.codetabs.com/v1/proxy?quest=https://vsco.co/{username}"
        res = requests.get(proxy2, timeout=10)
        if res.status_code == 200:
            if '<title>Page Not Found' in res.text or 'Page not found' in res.text:
                return 404
            return display_url
        elif res.status_code == 404:
            return 404
    except Exception:
        pass

    return None

def check_instagram_profile(username, display_url):
    # 1. API interna do Instagram
    try:
        api_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"

        api_headers = {
            "x-ig-app-id": "936619743392459",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Referer": "https://www.instagram.com/",
            "Accept": "*/*"
        }

        api_res = requests.get(api_url, headers=api_headers, timeout=8)

        if api_res.status_code == 200:
            try:
                data = api_res.json()
                user = data.get("data", {}).get("user")

                if user:
                    return display_url
                else:
                    return 404

            except Exception:
                pass

        elif api_res.status_code == 404:
            return 404

    except Exception:
        pass

    # 2. Fallback direto no Instagram Web
    try:
        url = f"https://www.instagram.com/{username}/"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Sec-Fetch-Mode": "navigate",
        }

        res = requests.get(
            url,
            headers=headers,
            timeout=8,
            allow_redirects=True
        )

        if res.status_code == 404:
            return 404

        if res.status_code == 200:
            if '"HttpErrorPage"' in res.text:
                return 404

            if 'Page Not Found' in res.text:
                return 404

            return display_url

    except Exception:
        pass

    # 3. Imginn via proxy (fallback com validação rigorosa)
    try:
        proxy_url = f"https://api.codetabs.com/v1/proxy?quest=https://imginn.com/{username}/"
        res = requests.get(proxy_url, timeout=10)
        if res.status_code == 200:
            text = res.text
            # Ignorar páginas da Cloudflare ou vazias
            if 'cloudflare' in text.lower() or 'challenge-platform' in text.lower() or len(text) < 500:
                return None
            if '<title>404' in text or 'page not found' in text.lower():
                return 404
            # Verificar se o conteúdo realmente tem dados do perfil
            if f'@{username}' in text.lower() or f'>{username}<' in text.lower():
                return display_url
    except Exception:
        pass

    return None


# Lista de plataformas
platforms = [
    "instagram", "twitter", "tiktok", "reddit", "telegram", "linktree", "github",
    "youtube", "gravatar", "keybase", "roblox", "snapchat", "chess",
    "twitch", "minecraft", "myanimelist", "pastebin", "about.me", "vsco", "patreon",
    "9gag", "redbubble", "openstreetmap", "pensador", "rapfame", "bitbucket"
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
        print(f"{TextColor.ORANGE}Status do código {platform.capitalize()}: Erro desconhecido ou perfil não encontrado{TextColor.END}")

if not profile_found:
    print(f"{TextColor.RED}Nenhum perfil encontrado.{TextColor.END}")
else:
    print(f"{TextColor.GREEN}Processo concluído com perfis encontrados.{TextColor.END}")
