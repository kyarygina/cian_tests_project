# Проект по тестированию сервиса для продажи недвижимости "ЦИАН"
> <a target="_blank" href="https://cian.ru/">cian.ru</a>

![main page screenshot](/files/cian.ru.png)

----

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Запуск web/UI автотестов в Selenoid

### Список проверок, реализованных в web/UI автотестах

- [x] Проверка фильтров на вкладке 'Купить'
- [x] Проверка фильтров на вкладке 'Cнять'
- [x] Проверка фильтров на вкладке 'Посуточно'
- [x] Проверка фильтров на вкладке 'Ипотека'
- [x] Проверка диалогового окна на вкладке 'Подбор риелтора'

----

### Используемый стэк

<img title="Python" src="/files/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="/files/icons/pytest-original.svg" height="40" width="40"/> <img title="Allure Report" src="/files/icons/Allure_Report.png" height="40" width="40"/> <img title="GitHub" src="/files/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="/files/icons/selenoid.png" height="40" width="40"/> <img title="Selenium" src="/files/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="/files/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="/files/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="/files/icons/tg.png" height="40" width="40"/> <img title="Jenkins" src="/files/icons/jenkins-original.svg" height="40" width="40"/>

----

### Локальный запуск автотестов

#### Для запуска web/UI автотестов выполнить в cli:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

#### Получение отчёта:
```bash
allure serve tests/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_python_20_14_kyarygina/">Ссылка</a>

#### Параметры сборки
> [!NOTE]
> Параметры сборки не обязательны
```python
ENVIRONMENT = ['STAGE', 'PREPROD', 'PROD'] # Окружение
COMMENT = 'some comment' # Комментарий, в котором можно указать аккаунт в tg для уведомления об отчете
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_python_20_14_kyarygina/">проект</a>
2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать любое окружение
4. В поле "COMMENT" ввести комментарий
5. Нажать "Build"

![jenkins project main page](/files/jenkins_project.png)

----

### Allure отчет
#### <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_python_20_14_kyarygina/16/allure/">Общие результаты</a>
![allure_report_overview](/files/allure_report_overview.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_python_20_14_kyarygina/16/allure/#suites">Результаты прохождения теста</a>

![allure_reports_suites](/files/allure_report_suites.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_python_20_14_kyarygina/16/allure/#suites">Приложенные к кейсу логи, видео, скриншоты</a>


![allure_reports_attach](/files/allure_report_attach.png)

----

### Оповещения в Telegram
![telegram_allert](/files/telegram_allert.png)

----

### Видео прохождения web/UI автотеста
![autotest_gif](/files/autotest.gif)
