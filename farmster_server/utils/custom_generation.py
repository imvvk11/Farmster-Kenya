from random import SystemRandom

UNICODE_ASCII_INT_SET = '0123456789'
UNICODE_ASCII_CHAR_SET = 'abcdefghijklmnopqrstuvwxyz'


def generate_token_custom(length=6, chars=UNICODE_ASCII_INT_SET):
    """Generates a non-guessable OAuth token

    OAuth (1 and 2) does not specify the format of tokens except that they
    should be strings of random characters. Tokens should not be guessable
    and entropy when generating the random characters is important. Which is
    why SystemRandom is used instead of the default random.choice method.
    """
    rand = SystemRandom()
    return ''.join(rand.choice(chars) for x in range(length))

