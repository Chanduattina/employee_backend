from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://chandu:chandupass@localhost/emp_db",
    echo=True
)
Session = sessionmaker(autocommit=True, autoflush=True, bind=engine)
session = Session()