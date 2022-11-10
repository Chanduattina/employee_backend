from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://chandu:chandupass@localhost/emp_db",
    echo=True
)
Session = sessionmaker(bind=engine)
session = Session()
