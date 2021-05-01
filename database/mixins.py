from sqlalchemy import Column, Integer, String


class UrlMixin:
    url = Column(String, unique=True, nullable=False)
