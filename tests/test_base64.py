import random
import string

from encoder.base64 import base64_encode, base64_decode

character_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=')

def random_string(string_length=100):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def test_encode_characters():
    string = random_string()
    encoded = base64_encode(string)
    good = True
    for c in encoded:
        if c not in character_set:
            good = False
    assert good

def test_encode_ending_equal():
    string = random_string()
    encoded = base64_encode(string)
    substr = encoded[:-2]
    assert '=' not in substr

def test_encode_simple():
    assert base64_encode("omar aflak") == "b21hciBhZmxhaw=="

def test_encode_length():
    string = random_string()
    assert len(base64_encode(string)) > len(string)

def test_encode_decode():
    string = random_string(1000)
    encoded = base64_encode(string)
    decoded = base64_decode(encoded)
    assert string == decoded
