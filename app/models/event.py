from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from datetime import datetime

class Base(DeclarativeBase):
    """
         Classe base para todos os modelos do SQLAlchemy.
    """
    pass

class Event(Base):
    """
    Modelo que representa um evento no sistema.

    Attributes:
        id (int): Identificador único do evento (chave primária).
        name (str): Nome do evento (máximo de 30 caracteres).
        description (str): Descrição do evento (máximo de 90 caracteres).
        date (datetime): Data e hora do evento (valor padrão: data/hora atual em UTC).
    """
    __tablename__ = "events" 
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=30), index = True)
    description: Mapped[str] = mapped_column(String(length=90), nullable=True)
    date : Mapped[datetime] = mapped_column(default=datetime.utcnow)