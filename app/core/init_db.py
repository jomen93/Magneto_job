from app.core.database import Base, engine
from app.models import dna_sequence

def initialize_database():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully !")

# from root python -m app.core.init_db
# enter the dabase from terminal
# docker exec -it magneto_db mysql -u root -p
