from sqlalchemy import (

    Column,
    Integer,
    String,
    Boolean

)

from database.database import Base


class Identity(Base):

    __tablename__ = "identities"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String
    )

    source = Column(
        String
    )

    privileged = Column(
        Boolean,
        default=False
    )

    dormant = Column(
        Boolean,
        default=False
    )

    mfa_enabled = Column(
        Boolean,
        default=False
    )
