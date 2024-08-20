import os
import sys
import django
from mongoengine import connect
import configparser

# Підключення до MongoDB
config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'USER')
mongodb_pass = config.get('DB', 'PASS')
db_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)

# Налаштування Django
sys.path.append('C:/Python/Projects/pw_modul_10/quotes')  # або вкажіть інший шлях до вашого проекту
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')
django.setup()

# Імпорт моделей
from modelsMongoDB import Authors as MongoAuthors, Qoutes as MongoQoutes, Tag as MongoTag
from quotesapp.models import Authors as PgAuthors, Qoutes as PgQoutes, Tag as PgTag

def transfer_tags(mongo_tags):
    pg_tags = []
    for mongo_tag in mongo_tags:
        pg_tag, created = PgTag.objects.get_or_create(name=mongo_tag.name)
        pg_tags.append(pg_tag)
    return pg_tags

def transfer_authors():
    for mongo_author in MongoAuthors.objects:
        pg_author, created = PgAuthors.objects.get_or_create(
            fullname=mongo_author.fullname,
            born_date=mongo_author.born_date,
            born_location=mongo_author.born_location,
            description=mongo_author.description
        )
        transfer_quotes(pg_author, mongo_author)

def transfer_quotes(pg_author, mongo_author):
    for mongo_quote in MongoQoutes.objects(author=mongo_author):
        pg_quote = PgQoutes.objects.create(
            author=pg_author,
            quote=mongo_quote.quote,
        )
        # Додамо теги до цитати
        pg_tags = transfer_tags(mongo_quote.tags)
        pg_quote.tags.set(pg_tags)
        pg_quote.save()

if __name__ == "__main__":
    transfer_authors()