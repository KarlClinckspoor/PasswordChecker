# PasswordChecker

This is a simple script to send a request to the api from haveibeenpwned.com and check if a password has been leaked before. Inspired by a [computerphile video](https://www.youtube.com/watch?v=hhUb5iknVJs&t=401s)

## Usage

`python password.py <password1> <password2> ...`

Example:

```
$ python password.py Password1 Password1234
For password Password1 there are 111658 leaks
        Sleeping for 1 seconds...
For password Password1234 there are 3621 leaks
        Sleeping for 1 seconds...
```

## Requirements

Any installation of python probably has these, but just in case:

1. `hashlib`
2. `requests`
3. `sys`
