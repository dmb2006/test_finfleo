# Автоматизированные UI-тесты для страницы finfleo

## 📌 О проекте

Автоматизированные тесты для веб-интерфейса:
- Добавление Мерча в корзину и заполнение формы, с проврекой что форма заполнена
- Заполнение формы для обратной связи с проверкой, что форма отправлена
- Проверка через поисковую строку спецтехники которой нет в наличии с проверкой 

## 🛠 Технологический стек

<p> align="center">
  <img src="sources/icon/python-original.svg" width="50"> <img src="media/icons/pytest.png" width="50"> <img src="media/icons/selene.png" width="50"> <img src="media/icons/selenoid.png" width="50"> <img src="media/icons/jenkins.png" width="50"> <img   src="media/icons/allure_report.png" width="50"> <img src="media/icons/allure_testops.png" width="50"> <img src="media/icons/jira.png" width="50"> <img src="media/icons/tg.png" width="50">
</p>


- **Python 3.9+** - язык программирования
- **Selenium WebDriver** - автоматизация браузера
- **Selene** - удобная обертка над Selenium
- **Pytest** - фреймворк для тестирования
- **Allure** - генератор отчетов
- **Jenkins** - система непрерывной интеграции
- **Selenoid** - контейнеризованный запуск браузеров

## 📂 Структура проекта

## 🌐 CI/CD и Мониторинг


**Ссылка на сборку**:  

**Особенности пайплайна**:
- Автоматический запуск тестов в Selenoid
- Генерация Allure-отчёта
- Отправка уведомлений в Telegram

**Пример отчёта**:  
[https://jenkins.autotests.cloud/job/homework_forteen_ANikashova/4/allure/](https://jenkins.autotests.cloud/job/homework_forteen_ANikashova/4/allure/)

![img_2.png](img_2.png)

### <img src="https://telegram.org/img/t_logo.png" width="20"> Telegram Bot
**Бот для уведомлений**:  
[@homework_13_Nikashova_bot](https://t.me/homework_13_Nikashova_bot)
![img_1.png](img_1.png)
