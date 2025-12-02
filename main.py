import httpx, time, string, random
url = "https://bonk2.io/scripts/register_legacy.php"

letras = string.ascii_letters
maiu = string.ascii_uppercase
minu = string.ascii_lowercase
num = string.digits

aba = letras + maiu + minu + num
username = ""

for i in range(5):
    username += random.choice(aba)

while True:
    username += random.choice(aba)
    l2 = len(username)
    if l2 < 3 or l2 > 10:
        username = ""
        
    for i in range(5):
        username += random.choice(aba)

    data = {
    "username": username,
    "password": "123",
    "remember": False
    }
    
    time.sleep(0.1)
    a = httpx.post(url, data=data)
    print(a.json())
    print(username)
