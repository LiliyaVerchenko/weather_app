# Документация по проекту
Приложение weather_app, позволяющее получать актуальные данные о погоде с ресурса 
https://openweathermap.org/
---

### Установка зависимостей:

pip install -r requirements.txt

---

### Получение API_key c вышеуказанного ресурса:

1. Необходимо перейти по ссылке https://home.openweathermap.org/users/sign_up и 
пройти процедуру регистрации
2. Зайти в личный кабинет в раздел "My API keys" или 
пеерйти по ссылке https://home.openweathermap.org/api_keys. Ключ будет в поле key.
3. Внести ключ в переменные окружения в проекте с помощью команды  
export API_key='...'

---

### Запуск проекта:

python weather_app.py