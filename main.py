import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()

        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Чтобы программа возвращала словарь
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def translate_to_russian(text):
    try:
        translator = Translator()
        translation = translator.translate(text, src='en', dest='ru')
        return translation.text
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        if not word_dict:
            continue

        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение на русский язык
        word_russian = translate_to_russian(word)
        word_definition_russian = translate_to_russian(word_definition)

        # Начинаем игру
        print(f"Значение слова - {word_definition_russian}")
        user = input("Что это за слово? ")
        if user.lower() == word_russian.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word_russian}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()