import string
import secrets

def contains_uppercase(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ''
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

if __name__ == '__main__':
    new_password: str = generate_password(length=10, symbols=True, uppercase=True)
    print(new_password)