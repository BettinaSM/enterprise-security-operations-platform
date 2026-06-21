from sqlalchemy import (

    Column,
    Integer,
    String,
    DateTime

)

from datetime import datetime

from database.database import Base


class AuditEvent(Base):

    __tablename__ = "audit_events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    username = Column(
        String
    )

    action = Column(
        String
    )

    source = Column(
        String
    )
