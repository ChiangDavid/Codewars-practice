# A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

# E.g.

# map1 = "abcdefghijklmnopqrstuvwxyz";
# map2 = "etaoinshrdlucmfwypvbgkjqxz";
   
# cipher = Cipher(map1, map2);
# cipher.encode("abc") # => "eta"
# cipher.encode("xyz") # => "qxz"
# cipher.encode("aeiou") # => "eirfg"
   
# cipher.decode("eta") # => "abc"
# cipher.decode("qxz") # => "xyz"
# cipher.decode("eirfg") # => "aeiou"
# If a character provided is not in the opposing alphabet, simply leave it as be.

class Cipher(object):
    #使用字典下去做
    def __init__(self, map1, map2):
        self.encoder = dict(zip(map1, map2))
        self.decoder = dict(zip(map2, map1))
    
    def encode(self, s):
        return "".join([self.encoder.get(i, i) for i in s])
    
    def decode(self, s):
        return "".join([self.decoder.get(i, i) for i in s])
