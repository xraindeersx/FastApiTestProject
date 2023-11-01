# FastAPI Проект
Этот проект представляет собой API, созданный с использованием FastAPI, который предоставляет функциональность для управления элементами (item) и пользователями (user). Проект включает базовую аутентификацию HTTP для безопасности.

# Зависимости
Проект требует установки следующих зависимостей, которые могут быть установлены с использованием pip:

# Вы можете установить их, выполнив следующую команду:
**pip install -r requirements.txt**
Запуск приложения
Запуск с использованием Docker
Вы также можете запустить приложение с использованием Docker. Убедитесь, что у вас установлен Docker на вашем компьютере. Для этого выполните следующие шаги:

# Создайте Docker-образ:
**docker build -t my-fastapi-app .**
Где my-fastapi-app - это имя вашего Docker-образа.

# Запустите Docker-контейнер:
**docker run -p 8080:8080 my-fastapi-app**
Ваше FastAPI приложение будет доступно по адресу *http://127.0.0.1:8080* внутри контейнера, и порт 8080 будет проксирован на вашу локальную машину.


# Для запуска приложения без Docker выполните следующие шаги:
Запустите приложение с использованием Uvicorn:
**uvicorn main:app --host 0.0.0.0 --port 8080 --reload**
Приложение будет доступно по адресу http://127.0.0.1:8000. Вы можете использовать инструменты, такие как curl, Postman или веб-браузер для взаимодействия с API.

# Маршруты
Управление элементами (item)
1. POST /: Создание элемента. Для доступа к этому маршруту требуется базовая аутентификация HTTP.
2. GET /all_items: Получение всех элементов. Для доступа к этому маршруту также требуется базовая аутентификация HTTP.
3. PUT /{id}: Обновление элемента по его идентификатору. Требует аутентификации.
4. DELETE /{id}: Удаление элемента. Требуется аутентификация.
# Управление пользователями (user)
1. POST /: Создание пользователя.
2. GET /{id}: Получение информации о пользователе. Требуется аутентификация.
3. PUT /{id}: Обновление информации о пользователе. Требуется аутентификация.
4. DELETE /{id}: Удаление пользователя. Требуется аутентификация.
# Дополнительные маршруты
1. GET /count: Получение информации о пользователе и его элементах. Требуется аутентификация.
# Авторы
Aleh Shved
