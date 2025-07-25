
# Автоматизированные UI-тесты для страницы finfleo

## 📌 О проекте

Автоматизированные тесты для веб-интерфейса:
- Добавление Мерча в корзину и заполнение формы, с проврекой что форма заполнена
- Заполнение формы для обратной связи с проверкой, что форма отправлена
- Проверка через поисковую строку спецтехники которой нет в наличии с проверкой 

## 🛠 Технологический стек

<div align="center">
  
  <img src="sources/icon/python-original.svg" width="50" alt="Python"> 
  <img src="sources/icon/pytest.png" width="50" alt="Pytest"> 
  <img src="sources/icon/selene.png" width="50" alt="Selene"> 
  <img src="sources/icon/selenoid.png" width="50" alt="Selenoid"> 
  <img src="sources/icon/jenkins.png" width="50" alt="Jenkins"> 
  <img src="sources/icon/allure_report.png" width="50" alt="Allure Report"> 
  <img src="sources/icon/tg.png" width="50" alt="Telegram">
  
</div>

  - **Python 3.9+** - язык программирования
  - **Selenium WebDriver** - автоматизация браузера
  - **Selene** - удобная обертка над Selenium
  - **Pytest** - фреймворк для тестирования
  - **Allure** - генератор отчетов
  - **Jenkins** - система непрерывной интеграции
  - **Selenoid** - контейнеризованный запуск браузеров

## 📂 Структура проекта

```
.
├── .venv
├── model
│   ├── data
│   │   └── users.py
├── finfleo_page
│   ├── added_bascet_merge.py
│   ├── main_page_submit.py
│   └── search_bar.py
├── sources
│   ├── icon
│   │   ├── allure_report.png
│   │   ├── allure_testops.png
│   │   ├── pytest.png
│   │   ├── python-original.svg
│   │   ├── selene.png
│   │   ├── selenoid.png
│   │   └── tg.png
├── tests
│   ├── allure_results
│   ├── test_added_in_basket_merch.py
│   ├── test_main_page_submit.py
│   └── test_search_bar.py
├── utils
│   └── attach.py
├── .env
├── .gitignore
├── allure-notifications-4.9.0.jar
├── confest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## :rocket: Для запуска из терминала необходимо выполнить команду
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests
```

## 🌐 CI/CD и Мониторинг

<div align="center">
  
  <img src="sources/gif/added_merge.gif" width="300"> 
  <img src="sources/gif/search_bar.gif" width="300"> 
  <img src="sources/gif/submit.gif" width="300"> 
  
</div>

**Ссылка на сборку**:  
[jenkins](https://jenkins.autotests.cloud/job/store_finfleo/)

**Особенности пайплайна**:
- Автоматический запуск тестов в Selenoid
- Генерация Allure-отчёта
- Отправка уведомлений в Telegram



**Пример отчёта**:  
[(https://jenkins.autotests.cloud/job/store_finfleo/4/allure/)](https://jenkins.autotests.cloud/job/store_finfleo/4/allure/)


<img src="sources/screenshots/info.png" width="300"> 
<img src="sources/screenshots/allure_info.png" width="300"> 

  

-------

### <img src="https://telegram.org/img/t_logo.png" width="20"> Telegram Bot
**Отбика прогонов с уведомлением в ТГ**:  
[Отбивка прогонов автотестов](https://t.me/+2XQAhYNunURkN2Uy)
<div align="center">
  
  <img src="sources/screenshots/finfleo_done.png" width="300">
  
</div>
