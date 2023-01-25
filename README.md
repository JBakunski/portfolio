To upload data to database run below commands:
```shell
python manage.py migrate
python manage.py upload_data
```
Or
```shell
python manage.py migrate
python manage.py loaddata posts/fixtures/author.json
python manage.py loaddata posts/fixtures/post.json
```

To run project use:`python manage.py runserver`
All necessary packages you can install using requirements.txt file.
