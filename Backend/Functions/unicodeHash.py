from hashlib import sha256

def unicodeHash(s : str) -> str :
        return ' '.join(map(str, map(int, sha256(s.encode()).digest())))
