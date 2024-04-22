import requests

class TextColor:
  RED = '\033[91m'
  BLUE = '\033[94m'
  YELLOW = '\033[93m'
  END: str = '\033[0m'


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
print("Created by Faw 1.0")


def check_social_profile(platform, username):
  if platform == "instagram":
    url = f"https://imginn.com/{username}/"
    display_url = f"https://instagram.com/{username}"
  elif platform == "youtube":
    url = f"https://youtube.com/@{username}"
    display_url = f"https://youtube.com/@{username}"
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
  else:
    return None

  headers = {
      "User-Agent":
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
  }
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    return display_url
  elif response.status_code == 404:
    return 404


platforms = [
    "instagram", "youtube", "reddit", "myanimelist", "github", "snapchat",
    "chess", "twitch", "minecraft", "bitbucket", "9gag", "pastebin",
    "redbubble", "openstreetmap", "patreon", "pensador"
]

username = input("\033[31mUsername: \033[0m")
profile_found = False

for platform in platforms:
  result = check_social_profile(platform, username)

  if result == 404:
    print(
        f"\033[91mPerfil não encontrado no {platform.capitalize()} (Status 404)\033[0m"
    )
  elif isinstance(result, str):
    print(
        f"\033[92mPerfil encontrado no {platform.capitalize()}: {result}\033[0m"
    )
    profile_found = True
  else:
    print(
        f"\033[91mStatus do código {platform.capitalize()} (Status 404)\033[0m"
    )
