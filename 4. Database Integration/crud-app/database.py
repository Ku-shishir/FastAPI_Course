from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

"""sqlite → Database type
./ → Current project directory
test.db → SQLite database file"""


"""What is check_same_thread=False?
SQLite normally restricts a database connection to the thread that created it.
FastAPI can handle requests using different threads, so:"""


"""Request
   ↓
SessionLocal()
   ↓
Database Session
   ↓
Query / Insert / Update / Delete
   ↓
db.close()"""


"""Why autoflush=False?
It prevents SQLAlchemy from automatically sending pending changes to the database before certain operations."""