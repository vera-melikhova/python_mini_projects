import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."


def ask_yes_no(question):
    while True:
        answer = input(question + " (д/н): ")
        if answer.lower() in ["д", "да", "y", "yes"]:
            return True
        elif answer.lower() in ["н", "нет", "n", "no"]:
            return False
        else:
            print("Пожалуйста, ответьте 'д' или 'н'")


def generate_password(length, chars):
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password


if __name__ == "__main__":
    print("Сколько паролей сгенерировать?")
    num = int(input())
    print("Укажите длину пароля?")
    length = int(input())
    digit = ask_yes_no("Включать ли цифры 0123456789?; д = да, н = нет")
    upper = ask_yes_no(
        "Включать прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; д = да, н = нет"
    )
    lower = ask_yes_no(
        "Включать строчные буквы abcdefghijklmnopqrstuvwxyz?; д = да, н = нет"
    )
    symbols = ask_yes_no("Включать ли символы !#$%&*+-=?@^_?; д = да, н = нет")
    similar_symbols = ask_yes_no(
        "Исключать ли неоднозначные символы il1Lo0O?; д = да, н = нет"
    )

    chars = ""

    if digit:
        chars += digits
    if upper:
        chars += uppercase_letters
    if lower:
        chars += lowercase_letters
    if symbols:
        chars += punctuation
    if similar_symbols:
        for bad_char in "il1Lo0O":
            chars = chars.replace(bad_char, "")
    if not chars:
        print("Ошибка: не выбрано ни одной категории символов!")
        exit()

    print("Сгенерированные пароли:")
    for i in range(num):
        password = generate_password(length, chars)
        print(password)
