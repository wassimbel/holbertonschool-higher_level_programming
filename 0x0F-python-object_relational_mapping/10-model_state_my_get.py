#!/usr/bin/python3
""" module that lists all state objects from a database """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).filter(State.name == sys.argv[4]).first()
    if not first:
        print("Not found")
    else:
        print(first.id)
    session.close()
