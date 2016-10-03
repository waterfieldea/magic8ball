# magic8ball

###dependencies
```
pip install -r requirements.txt
```

### to start
```
python manage.py runserver
```

### usage
```
curl -G "http://localhost:8000/api/answer/" --data-urlencode "question=how old are you?"

# or just visit
http://localhost:8000/api/answer?question=how old are you?"
```
