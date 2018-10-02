# *- coding: utf-8 -*
import time
import random
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, Sequence
from sqlalchemy.dialects import postgresql

HOW_MANY = 1000

# import logging
# logging.basicConfig()
# logger = logging.getLogger('sqlalchemy.engine')
# logger.setLevel(logging.INFO)

Base = declarative_base()


class Talk(Base):
    __tablename__ = "talks"

    id = Column(Integer, Sequence("talks_id_seq"), primary_key=True)
    topic = Column(String)
    when = Column(DateTime)
    tags = Column(postgresql.ARRAY(String))
    duration = Column(Float)


def _random_topic():
    return random.choice(
        (
            "No talks added yet",
            "I'm working on a branch of django-mongokit that I "
            "thought you'd like to know about.",
            "I want to learn Gaelic.",
            "I'm well, thank you.",
            " (Kaw uhn KEU-ra shin KAW-la root uh CHOO-nik mee uhn-royer?)",
            "Chah beh shin KEU-ra, sheh shin moe CHYEH-luh uh vah EEN-tchuh!",
            "STUH LUH-oom BRISS-kaht-chun goo MAWR",
            "Suas Leis a' Ghàidhlig! Up with Gaelic!",
            "Tha mi ag iarraidh briosgaid!",
        )
    )


def _random_when():
    return datetime.datetime(
        random.randint(2000, 2010),
        random.randint(1, 12),
        random.randint(1, 28),
        0,
        0,
        0,
    )


def _random_tags():
    tags = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]
    random.shuffle(tags)
    return tags[: random.randint(0, 3)]


def _random_duration():
    return round(random.random() * 10, 1)


def run():
    engine = create_engine(
        "postgresql://peterbe:test123@localhost/fastestdb", echo=False
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Talk).delete()

    t0 = time.time()
    # CREATE ALL
    talks = []
    for i in range(HOW_MANY):
        talk = Talk(
            topic=_random_topic(),
            when=_random_when(),
            duration=_random_duration(),
            tags=_random_tags(),
        )
        session.add(talk)
        talks.append(talk)

    session.commit()

    t1 = time.time()
    # EDIT ALL

    for talk in talks:
        talk.topic += "extra"
        talk.duration += 1.0
        talk.when += datetime.timedelta(days=1)
        talk.tags.append("extra")
        session.merge(talk)

    session.commit()
    t2 = time.time()

    # DELETE EACH
    for talk in talks:
        session.delete(talk)
    session.commit()
    t3 = time.time()

    print("insert", t1 - t0)
    print("edit", t2 - t1)
    print("delete", t3 - t2)
    print("TOTAL", t3 - t0)


if __name__ == "__main__":
    run()
