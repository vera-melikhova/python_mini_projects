from generator import generate_password

DIGITS = "0123456789"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_."


def test_password_length():
    chars = LOWERCASE + UPPERCASE
    length = 10
    password = generate_password(length, chars)
    assert len(password) == length


def test_password_uses_allowed_chars():
    chars = DIGITS + LOWERCASE
    password = generate_password(20, chars)
    for char in password:
        assert char in chars


def test_exclude_similar_symbol():
    chars = DIGITS + LOWERCASE + UPPERCASE + PUNCTUATION
    bad_chars = "il1Lo0O"
    for bad_char in bad_chars:
        if bad_char in chars:
            chars = chars.replace(bad_char, "")
    password = generate_password(50, chars)
    for bad_char in bad_chars:
        assert bad_char not in password


def test_only_digits():
    chars = DIGITS
    password = generate_password(10, chars)
    assert password.isdigit()


def test_includes_punctuation():
    chars = PUNCTUATION
    password = generate_password(20, chars)
    for char in password:
        assert char in PUNCTUATION


def test_randomness():
    chars = DIGITS + LOWERCASE + UPPERCASE + PUNCTUATION
    passwords = set()
    for _ in range(100):
        password = generate_password(10, chars)
        passwords.add(password)
    assert len(passwords) > 90


def test_very_long_password():
    chars = DIGITS + LOWERCASE + UPPERCASE + PUNCTUATION
    length = 1000
    password = generate_password(length, chars)
    assert len(password) == length


def test_single_char_password():
    chars = DIGITS
    length = 1
    password = generate_password(length, chars)
    assert len(password) == 1
    assert password[0] in chars


def test_different_lengths():
    chars = LOWERCASE
    for length in [1, 5, 10, 20, 50, 100]:
        password = generate_password(length, chars)
        assert len(password) == length
