import re

url = input("URL: ").strip()

matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

if matches:
    username = matches.group(1)
print(username)

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(username)

