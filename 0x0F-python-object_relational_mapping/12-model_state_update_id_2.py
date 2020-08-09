#!/usr/bin/python3
"""Explanation
"""


if __name__ == '__main__':
    from model_state import Base, State
    from sys import argv as par
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    args = 'mysql+mysqldb://{}:{}'.format(par[1], par[2])
    args += '@localhost:3306/{}'.format(par[3])
    eng = create_engine(args, pool_pre_ping=True)
    Base.metadata.create_all(eng)

    ses = sessionmaker(bind=eng)
    Sess = ses()
    state = State(name="Louisiana")
    Sess.add(state)
    state = Sess.query(State).get(2)
    state.name = "New Mexico"
    Sess.commit()
    Sess.close()
    