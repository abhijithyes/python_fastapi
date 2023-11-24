from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from neo.db.models.base import Base


class User(Base):
    """
    Represents a user in the system.

    :param id: The unique identifier for the user.
    :param username: The username of the user (unique).
    :param hashed_password: The hashed password of the user.
    :param documents: A list of documents owned by the user.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)  # Store the hashed password

    # Define the one-to-many relationship with Document
    documents = relationship("Document", back_populates="owner")



class Document(Base):
    """
    Represents a document in the system.

    :param id: The unique identifier for the document.
    :param title: The title of the document.
    :param content: The content of the document.
    :param owner_id: The ID of the user who owns the document.
    :param owner: The user who owns the document.
    """

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

    # Define the many-to-one relationship with User
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="documents")
