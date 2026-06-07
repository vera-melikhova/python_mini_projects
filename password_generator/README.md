# Генератор паролей

Программа на Python для генерации случайных паролей с настраиваемыми параметрами:
- Выбор длины пароля
- Включение/исключение цифр, букв, символов
- Исключение неоднозначных символов (il1Lo0O)
- Генерация нескольких паролей за раз

## Установка

```bash
git clone https://github.com/vera-melikhova/password_generator.git
cd password_generator
```

## Запуск

```bash
python generator.py
```

## Тестирование

```bash
pip install pytest
pytest test_password_generator.py -v
```

## Требования

- Python 3.6+
- pytest (для тестов)