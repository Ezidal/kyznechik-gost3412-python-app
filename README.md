# Графическое приложение на Python для шифрования

Этот проект представляет собой графическое приложение (GUI) для шифрования и дешифрования данных с использованием блочного шифра «Кузнечик» (ГОСТ Р 34.12-2015). Приложение позволяет пользователям вводить ключи и данные, а затем получает зашифрованный результат.

## Структура проекта

```
python-gui-encryption-app
├── src
│   ├── main.py          # Точка входа в приложение
│   ├── gost.py          # Реализация блочного шифра ГОСТ
│   ├── mainRandom.py    # Генерация случайных ключей и шифрование
│   ├── mainStdIn.py     # Ввод ключей и блоков через консоль
│   ├── gui.py           # Реализация графического интерфейса
│   └── assets           # Дополнительные ресурсы (изображения, иконки и т.д.)
├── requirements.txt     # Зависимости проекта
└── README.md            # Документация проекта
```

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/Ezidal/kyznechik-gost3412-python-app.git
   cd python-gui-encryption-app
   ```

2. Установите необходимые зависимости:
   ```
   pip install -r requirements.txt
   ```

## Использование

1. Запустите приложение:
   ```
   python src/main.py
   ```

2. Откроется графический интерфейс, где можно ввести ключи шифрования и данные.

3. Введите ключи и данные в соответствующие поля и нажмите кнопку шифрования, чтобы получить результат.

4. Также можно использовать консольный режим, запустив:
   ```
   python src/mainStdIn.py
   ```

## Возможности

- Ввод ключей и данных через удобный графический интерфейс.
- Шифрование и дешифрование с использованием блочного шифра ГОСТ.
- Генерация случайных ключей для шифрования.
- Ввод через консоль для продвинутых пользователей.



# Python GUI Encryption Application

This project is a graphical user interface (GUI) application for encrypting and decrypting data using the Kuznechik (GOST R 34.12-2015) block cipher. The application allows users to input keys and data, and it provides encrypted outputs.

## Project Structure

```
python-gui-encryption-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── gost.py          # Implementation of the GOST block cipher
│   ├── mainRandom.py     # Random key generation and encryption
│   ├── mainStdIn.py      # Console input for keys and blocks
│   ├── gui.py           # GUI implementation
│   └── assets           # Additional resources (images, icons, etc.)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-gui-encryption-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. The GUI will open, allowing you to input your encryption keys and data.

3. Enter the keys and data in the provided fields and click the encrypt button to see the encrypted output.

4. You can also use the console input method by running:
   ```
   python src/mainStdIn.py
   ```

## Features

- Input keys and data through a user-friendly GUI.
- Encrypt and decrypt data using the GOST block cipher.
- Generate random keys for encryption.
- Console-based input for advanced users.