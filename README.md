# gb_flask
## Flask project

### Установка
- *Клонируйте проект с гит*
```shell 
git clone git@github.com:HappySeien/gb_flask.git
```
- *перейдите в папку с проектом*
```shell 
cd gb_flask/ 
```
- *Разверните виртуальное окружение python*
```shell 
python3 -m venv env
```
- *Активируйте окружение*
```shell 
source env/bin/activate
```
- *Установите зависимости*
```
pip install -r requirements.txt
```
- *Инициализируйте бд с тестовыми данными*
```shell 
flask db upgrade
flask custom create-users
flask custom create-admin
flask custom create-tags
``` 
- *Запустите проект*
```shell 
python3 wsgi.py
```
