## Installation du projet

pip install python-telegram-bot --upgrade


### Sources

https://github.com/python-telegram-bot/python-telegram-bot



### Installation SQLite

sudo apt-get install sqlite3

### Enrichissement de la BDD
sqlite3 monitorwebsite.db 

sqlite> BEGIN;
sqlite> CREATE TABLE constants(key TEXT PRIMARY,value TEXT);
sqlite> COMMIT;

sqlite> BEGIN;
sqlite> INSERT INTO constants(key,value) VALUES ('TELEGRAM_GROUP_ID','XXXXXXXX');
sqlite> INSERT INTO constants(key,value) VALUES ('TELEGRAM_GROUP_ID','XXXXXXXX');
sqlite> COMMIT;

