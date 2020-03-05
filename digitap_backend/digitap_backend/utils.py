import random
import string

def generate_st():
    """Generate a random string  """
    strng = string.ascii_lowercase + string.digits
    return ''.join(random.choice(strng) for i in range(7))
