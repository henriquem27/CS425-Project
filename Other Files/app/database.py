from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql:///?User=postgres&Password=123qw123&Database=postgres&Server=127.0.0.1&Port=5432")

