import sys
import requests
import hashlib

passwords = sys.argv[1:]
if not passwords:
    raise("Please supply at least one password")

for password in passwords:
    #password = password.encode()
    sha1 = hashlib.sha1(password.encode()).hexdigest()
    to_send = sha1[:5]
    url = f'https://api.pwnedpasswords.com/range/{to_send}'
    
    possibilities = requests.get(url).text.split('\r\n')
    for possibility in possibilities:
        if sha1[5:].upper() in possibility:
            print('For password', password, 
                    'there are', possibility.split(':')[1], 'leaks')
            break
    else:
        print(f'Your password, {password}, is safe! Nothing found')

     
