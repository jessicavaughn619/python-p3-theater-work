from sqlalchemy import (ForeignKey, Column, Integer, String, MetaData, PrimaryKeyConstraint)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = "auditions"
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Integer())

    role_id = Column(Integer(), ForeignKey("roles.id"))

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'Actor: {self.actor} ' \
        + f'Location: {self.location} ' \
        + f'Phone: {self.phone} ' \
        + f'Hired: {self.hired} ' \
        + f'Role ID: {self.role_id}'

    def call_back(self):
        self.hired=1

class Role(Base):
    __tablename__ = "roles"
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    character_name = Column(String())

    auditions = relationship("Audition", backref=backref("audition"))

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'Character Name: {self.character_name}'

    def lead(session):
        hired_actors = session.query(Role).filter_by(hired=1)
        if hired_actors:
            return hired_actors.first()
        return("No actor has been hired for this role.")

    def understudy(session):
        hired_actors = session.query(Role).filter_by(hired=1).limit(2)[1]
        if hired_actors:
            return hired_actors
        return("No actor has been hired for this role.")
    