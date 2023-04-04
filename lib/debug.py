from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Audition, Role)

if __name__ == "__main__":

    engine = create_engine('sqlite:///theater_work.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    elsa = Role(
        character_name="Elsa"
    )
    # session.add(elsa)
    # session.commit()

    tape_one = Audition(
        actor="Joe Smith",
        location="Denver, CO",
        phone=1234567890,
        hired=1,
        role_id=1
    )
    # session.add(tape_one)
    # session.commit()

    tape_two = Audition(
        actor="Sally Jones",
        location="Denver, CO",
        phone=9876543210,
        hired=0,
        role_id=1
    )
    # session.add(tape_two)
    # session.commit()

    


    session.commit()
    session.close()

    import ipdb; ipdb.set_trace()