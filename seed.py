import pandas as pd
from app import create_app, db
from app.models import Movie

def seed_database(csv_filepath):
    app = create_app()
    with app.app_context():
        # Read the CSV file
        df = pd.read_csv(csv_filepath)
        
        # Fill any blank movie overviews with an empty string to prevent errors
        df['overview'] = df['overview'].fillna('')
        
        # Iterate through the rows and add to the database session
        for index, row in df.iterrows():
            new_movie = Movie(
                tmdb_id=row['id'],           # Maps CSV 'id' to Model 'tmdb_id'
                title=row['title'],          # Maps CSV 'title' to Model 'title'
                description=row['overview']  # Maps CSV 'overview' to Model 'description'
            )
            db.session.add(new_movie)
        
        # Commit the changes to MySQL
        try:
            db.session.commit()
            print("Database successfully populated.")
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    seed_database('tmdb_5000_movies.csv')