## Clone Repository
```sh
git clone https://github.com/novaandini/arkanesia.git
```
## Download Library
```sh
pip install -r requirements.txt
```
atau
```sh
py -m pip install -r requirements.txt
```
## Setting Database
Buat file .env kemudian tambahkan:
```sh
DATABASE_URL="mysql+pymysql://username:password@localhost/db_name"
```
## Run Project
```sh
flask run --port=5001
```
atau
```sh
py -m flask run --port=5001
```
