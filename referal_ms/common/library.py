import hashlib
from hashids import Hashids

from django.conf import settings


def encode(value):
    """
    Function to  hash hid the int value.

    Input Params:
        value(int): int value
    Returns:
        hashed string.
    """
    hasher = Hashids(
        min_length=settings.HASHID_MIN_LENGTH,
        salt=settings.HASHID_SALT)
    try:
        value = int(value)
        return hasher.encode(value)
    except:
        return None


def decode(value):
    """
    Function to  decode hash hid value.

    Input Params:
        value(str): str value
    Returns:
        int value.
    """
    hasher = Hashids(
        min_length=settings.HASHID_MIN_LENGTH,
        salt=settings.HASHID_SALT)
    try:
        return hasher.decode(value)[0]
    except:
        return None


def generate_referral_code(usr_id):
    """function to convert id in referral code"""
    id_bytes = str(usr_id).encode('utf-8')
    hashed_id = hashlib.sha256(id_bytes).hexdigest()
    referral_code = hashed_id[:6]

    return referral_code
