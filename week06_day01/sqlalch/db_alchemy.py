from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalch.User import Base, User

DB_ENGINE_NAME = 'sqlite:///test_db_py.sqlite3'

if __name__ == '__main__':
    engine = create_engine(DB_ENGINE_NAME, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = User(name='Kamil_usr1')
    session.add(new_user)
    session.commit()
