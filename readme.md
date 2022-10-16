## TDD python project

### Install
1. ```pip install -r requirements.txt```
2. Run Server ```python manage.py createsuperuser```
3. Install ChromeDrive


### StepByStep
1. ```pip freeze > requirements.txt```
2. Download [Chromedriver](https://chromedriver.chromium.org/downloads) for Browser version
   - unzip
   - Add to Path
   - Test ```chromedriver --version``` -> ChromeDriver 106.0.5249.61
3. ```pip install Django```
   - ```python -m django --version```` -> 4.1.2
4. Create Django project:
   - ```django-admin startproject superlists```
   - created folder *superlists*
5. run server
   - ```cd .\superlists\```
   - ```python manage.py migrate```
   - ```python manage.py runserver```
6. Django Admin
   - ```python manage.py createsuperuser``` 
   - vvuri / qa@test.test
   - Open ```http://127.0.0.1:8000/admin```
7. Git
   - ```git init```
   - ```git add .```
   - ```git commit -m```
   - ```git remote add origin git@github.com:vvuri/py_tdd```
   - ```git push -u origin main```
