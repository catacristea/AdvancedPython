import requests, hashlib, sys
'''
This program uses some requests to get data from pwnedpasswords.
It searsches your password and shows you if your password has been hacked.
I used hashlib, so your password will not be stored on the site. 
Your password will be changed in hexadecimal format and the first 5 chr will be compared
with those which we get from website.
'''

def request_api_data(querry_char):
    url = 'https://api.pwnedpasswords.com/range/' + querry_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again!')
    return res

def get_pass_leakes_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    '''Check pass if it exists in API response'''
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_pass_leakes_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was fount {count} times ... you should probably your password!')
        else:
            print(f'{password} was not found. All good!')
    return 'Process done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
