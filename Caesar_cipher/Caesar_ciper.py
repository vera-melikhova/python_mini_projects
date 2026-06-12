def caesar_encrypt_by_word_length(text):
    new_text = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for word in text.split():
        shift = 0
        for char in word:
            if char.isalpha():
                shift += 1

        new_word = ""
        for char in word:
            if char.isalpha():
                index = alphabet.index(char.lower())
                new_index = (shift + index) % 26
                new_char = alphabet[new_index]
                if char.isupper():
                    new_char = new_char.upper()
                new_word += new_char
            else:
                new_word += char
        new_text.append(new_word)

    return " ".join(new_text)
