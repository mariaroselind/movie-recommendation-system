import pandas as pd
from app import create_app, db
from app.models import Movie

def seed_database(csv_filepath):
    app = create_app()
    with app.app_context():
        # Create database tables if they don't exist yet
        db.create_all()
        
        # Check if movies are already in the database
        if Movie.query.first() is not None:
            print("Database is already populated.")
            return

        print("Populating database from CSV...")
        df = pd.read_csv(csv_filepath)
        df['overview'] = df['overview'].fillna('')
        
        for index, row in df.iterrows():
            new_movie = Movie(
                tmdb_id=row['id'],
                title=row['title'],
                description=row['overview']
            )
            db.session.add(new_movie)
        
        try:
            db.session.commit()
            print("Database successfully populated.")
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    seed_database('tmdb_5000_movies.csv')