
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
  <img src="sources/icon/allure_testops.png" width="50" alt="Allure TestOps"> 
  <img src="sources/icon/jira.png" width="50" alt="Jira"> 
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

## 🌐 CI/CD и Мониторинг


**Ссылка на сборку**:  
[jenkins](https://jenkins.autotests.cloud/job/store_finfleo/)

**Особенности пайплайна**:
- Автоматический запуск тестов в Selenoid
- Генерация Allure-отчёта
- Отправка уведомлений в Telegram


**Пример отчёта**:  
[(https://jenkins.autotests.cloud/job/store_finfleo/4/allure/)](https://jenkins.autotests.cloud/job/store_finfleo/4/allure/)

<div align="center">
  
  <img src="sources/screenshots/allure_res1.png" width="300"> 
  
</div>

### <img src="https://telegram.org/img/t_logo.png" width="20"> Telegram Bot


<div align="center">
  
  <img src="sources/video/submit.mp4" width="300"> 
  <img src="sources/video/search_bar.mp4" width="300"> 
  <img src="sources/video/added_merge_in_basket.mp4" width="300"> 
  
</div>
-------

**Отбика прогонов с уведомлением в ТГ**:  
[Отбивка прогонов автотестов](https://t.me/+2XQAhYNunURkN2Uy)
<div align="center">
  
  <img src="sources/screenshots/allure_res2.png" width="300">
  
</div>
