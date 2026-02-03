# JWT Basics — схема взаимодействия

## Описание проекта

Учебный проект, демонстрирующий работу JWT (JSON Web Token) аутентификации на Python.

В проекте реализованы три основных процесса:
- **Регистрация** — хеширование пароля алгоритмом argon2 и сохранение в базу данных
- **Логин** — проверка пароля и выдача JWT токена
- **Защищённый запрос** — валидация токена и предоставление доступа к данным

Используемые технологии: Python, PyJWT, argon2-cffi.

---

## Файлы и их роли

| Файл | Роль |
|---|---|
| `password_utils.py` | Хеширование и проверка паролей (argon2) |
| `jwt_utils.py` | Создание и проверка JWT токенов |
| `jwt_basics` | Главный сценарий — связывает все вместе |

## Что делает каждый файл

### password_utils.py
- `hash_password(password)` — принимает пароль, возвращает хеш (argon2)
- `verify_password(password, hashed_password)` — сравнивает пароль с хешем, возвращает `True` / `False`

### jwt_utils.py
- `create_token(data, expires_delta)` — принимает словарь с данными, добавляет время истечения, возвращает JWT строку
- `verify_token(token)` — декодирует токен, возвращает payload или `None` если токен невалидный/истек

### jwt_basics (главный файл)
- `simulate_registration(username, password)` — вызывает `hash_password`, возвращает `{username, hashed_password}`
- `simulate_login(username, password, stored_hash)` — вызывает `verify_password`, если ок — вызывает `create_token`, возвращает токен
- `simulate_protected_request(token)` — вызывает `verify_token` ( где уже пропписан ключ шифрования и метод шифрования ), если ок — доступ разрешен

## Схема вызовов

```
jwt_basics
│
├── simulate_registration("nikita", "123")
│   └── password_utils.hash_password("123")          -> хеш
│
├── simulate_login("nikita", "123", хеш)
│   ├── password_utils.verify_password("123", хеш)   -> True/False
│   └── jwt_utils.create_token({username, user_id})   -> токен
│
└── simulate_protected_request(токен)
    └── jwt_utils.verify_token(токен)                 -> payload или None
```

## Полный флоу (что происходит при запуске)

```
1. РЕГИСТРАЦИЯ
   "123" --> hash_password --> "$argon2id$..." (хеш сохраняется)

2. ЛОГИН
   "123" + хеш --> verify_password --> True
                --> create_token({username: "nikita", user_id: 1}) --> "eyJ..."

3. ЗАЩИЩЕННЫЙ ЗАПРОС
   "eyJ..." --> verify_token --> {username: "nikita", user_id: 1, exp: ...}
            --> Доступ разрешен
```
