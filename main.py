import hashlib
import itertools

def hash_password(password, algorithm='md5'):
    hash_func = hashlib.new(algorithm)
    hash_func.update(password.encode('utf-8'))
    return hash_func.hexdigest()

def brute_force_crack(hashed_password, max_length=4, algorithm='md5'):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempt_password = ''.join(attempt)
            if hash_password(attempt_password, algorithm) == hashed_password:
                print(f"Password found: {attempt_password}")
                return
    print("Password not found")

if __name__ == "__main__":
    target_hash = input("Enter hashed password: ")
    max_len = int(input("Enter max length of password to attempt: "))
    brute_force_crack(target_hash, max_length=max_len)
