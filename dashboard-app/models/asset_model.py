from sqlalchemy import *

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Asset(Base):

    __tablename__ = "assets"

    id = Column(
        Integer,
        primary_key=True
    )

    hostname = Column(String)

    ip = Column(String)

    os = Column(String)

    owner = Column(String)

    criticality = Column(String)
