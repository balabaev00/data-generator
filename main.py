from helper import generate_data
from mongo import Mongo


def main():
    mongo = Mongo()
    db_users = mongo.db['users']
    db_news = mongo.db['news']

    print('Generate data')
    users, news = generate_data(500)

    print('Insert data to users collection')
    db_users.insert_many(users)

    print('Insert data to news collection')
    db_news.insert_many(news)

    print('Import data is done')


if __name__ == '__main__':
    main()
