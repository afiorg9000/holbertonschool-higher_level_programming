#!/usr/bin/python3

#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).first()

    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))

    session.close()
