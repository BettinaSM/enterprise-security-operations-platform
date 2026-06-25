from sqlalchemy import (

    Column,
    Integer,
    String

)

from database.database import Base


class Asset(Base):

    __tablename__ = "assets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    hostname = Column(
        String
    )

    ip_address = Column(
        String
    )

    operating_system = Column(
        String
    )

    owner = Column(
        String
    )

    criticality = Column(
        String
    )
