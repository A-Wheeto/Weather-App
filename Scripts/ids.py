from itsdangerous import json
from flask_sqlalchemy import SQLAlchemy

import json

with open('city.list.json', 'r', encoding="utf8") as f:
    data = f.read()

obj = json.loads(data)

for i in obj:
    print(i['id'], i['name'])

db = SQLAlchemy
