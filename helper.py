import random
import names
import string

from datetime import date, timedelta, datetime


def random_date(
        start=date(1990, 1, 1),
        end=date(2005, 1, 1)
):
    """
        Generate date between start и end
        :param start: date(1990, 1, 1),
        :param end: date(2005, 1, 1)
        :return date

        @example
        random_date()
        Output: 2000-12-04
    """
    # Length of array
    count = 5

    # getting days between dates
    dates_bet = end - start
    total_days = dates_bet.days

    res = []
    for idx in range(count):
        random.seed(a=None)

        # getting random days
        random_day = random.randrange(total_days)

        # getting random dates
        res.append(start + timedelta(days=random_day))

    return res[random.randint(0, count - 1)].strftime("%d/%m/%Y")


def random_datetime(
        start=datetime.strptime('1/1/2019 1:30 PM', '%m/%d/%Y %I:%M %p'),
        end=datetime.strptime('1/1/2023 4:50 PM', '%m/%d/%Y %I:%M %p')
):
    """
    Generate datetime between start and end
    Output: 2008-12-04 01:50:17
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return (start + timedelta(seconds=random_second)).strftime("%d/%m/%Y")


def generate_messages(message_count, news_count):
    messages = []
    for i in range(1, message_count + 1):
        message = {
            "_id": i,
            "text": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
            "created_at": random_date(),
            "rating": random.randint(-5, 5),
            "news_id": random.randint(1, news_count + 1)
        }
        messages.append(message)

    return messages


def generate_users(count):
    users = []
    for i in range(count):
        user = {
            "name": names.get_full_name(),
            "birthdate": random_date(),
            "messages": generate_messages(int(count/100), count),
        }
        users.append(user);

    return users


def generate_news(count):
    news = []
    for i in range(1, count + 1):
        new_news = {
            "_id": i,
            "created_at": random_datetime(),
            "text": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
            "views_count": random.randint(0, 100000),
        }
        news.append(new_news)

    return news


def generate_data(count):
    return generate_users(count), generate_news(count)
