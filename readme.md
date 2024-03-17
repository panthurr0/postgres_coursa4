# Парсер вакансий HeadHunter'а
Выводит информацию о вакансиях HH по запросу пользователя, используя SQL-запросы
## **Структура проекта:**

### **src:**

* [DB_setup.py](src/db_setup.py) - класс для создания бд и таблиц + заполнение таблиц
* [DBManager.py](src/db_manager.py) - класс с SQL-запросами
* [hhapi.py](src/hh_api.py) - класс для вывода вакансий и работодателей из HH
* [sql_config.py](src/sql_config.py) - конфиг для подключения к SQL
* [utils.py](src/vacancy.py) - функции для работы с пользователем


### root:

* [config](config.py)
* [main](main.py):
* [sql_setup()](main.py) - создает БД(удаляет старую при необходимости)
* [main()](main.py) - взаимодействие с пользователем
* [database.ini](database.ini) - заглушка, написать свои данные

