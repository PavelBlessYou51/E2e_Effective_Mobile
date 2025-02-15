# Краткое описание

Проект содержит E2E-тест, воспроизводящий сценарий покупки товара на сайте [SauceDemo](https://www.saucedemo.com/). Тест
использует Selenium с Python для автоматизации тестирования.

# Структура проекта

- main_project_dir
    - locators
        - \_\_init__.py
        - locators.py - содержит локаторы
    - pages
        - \_\_init__.py
        - base_page.py - содержит общие методы для работы с сайтом 
        - main_page.py - содержит методы для работы с определенным функционалом сайта
    - tests
      - \_\_init__.py
      - conftest.py - содержит тестовые фикстуры
      - end_to_end.py - содержит E2E-тест
    - \_\_init__.py
- .gitignore - список файлов и директорий не отслеживаемых Git
- README.md - настоящий файл
- requirements.txt - файл с зависимостями

# Инструкция по запуску тестов

1. Откройте IDEA и клонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале
    ```
    git clone https://github.com/PavelBlessYou51/E2e_Effective_Mobile.git
    ```

2. Убедитесь, что на Вашем компьютере установлен Python. В командной строке/терминале выполните команду
    ```
    python -v
    ```  
    Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/), выбрав подходящую версию для Вашей операционной системы, и пройдите шаг сначала.  В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". Иначе, у Вас не будет корректно отображаться версия Python.


3. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду
   ```
   cd /здесь укажите путь до директории с проектом
   ```

4. Убедитесь, что у Вас активировано виртуальное окружение. Если среда активирована, ваша командная строка будет выглядеть так:
   ```
   (venv) root@purplegate:/var/test (для Linux)
   (.venv) PS C:\path\to\project> (для Windows)
   ```
   4.1. Если среда не активирована, выполните в командной строке:
   
   ```
   source venv/bin/activate (для Linux)
   venv\Scripts\activate.bat (для Windows)
   ```

5. Установите необходимые зависимости из файла `requirements.txt`, выполнив команду  
   ```
   pip install -r requirements.txt (для Windows)
   pip3 install -r requirements.txt (для Linux)
   ```

6. Запустите тесты, выполнив команду  
   ```
   python -m pytest
   ```