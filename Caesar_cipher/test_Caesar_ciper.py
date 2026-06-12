import unittest
from Caesar_ciper import caesar_encrypt_by_word_length


class TestCaesarByWordLength(unittest.TestCase):

    def test_single_short_word(self):
        self.assertEqual(caesar_encrypt_by_word_length("a"), "b")

    def test_the_end_alphabet(self):
        self.assertEqual(caesar_encrypt_by_word_length("yz"), "ab")

    def test_two_word(self):
        self.assertEqual(caesar_encrypt_by_word_length("Hello world!"), "Mjqqt btwqi!")

    def test_punctuation_marks(self):
        self.assertEqual(caesar_encrypt_by_word_length("./ '!"), "./ '!")

    def test_empty_line(self):
        self.assertEqual(caesar_encrypt_by_word_length(""), "")

    def test_long_line(self):
        self.assertEqual(
            caesar_encrypt_by_word_length(
                "Today is a beautiful sunny day, the perfect time for a walk in the park and a small picnic!"
            ),
            "Ytifd ku b knjdcrodu xzssd gdb, wkh wlymlja xmqi iru b aepo kp wkh tevo dqg b xrfqq voitoi!",
        )


if __name__ == "__main__":
    unittest.main()
