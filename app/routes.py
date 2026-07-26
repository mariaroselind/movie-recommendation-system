from flask import Blueprint, render_template, request, jsonify
from app.models import Movie
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

main = Blueprint('main', __name__)

# Cache variables so the math only runs once
app_data = {'df': None, 'cosine_sim': None}

def init_recommender():
    if app_data['df'] is None:
        movies = Movie.query.all()
        # Load data into a Pandas DataFrame
        df = pd.DataFrame([(m.title, m.description) for m in movies], columns=['title', 'description'])
        df['description'] = df['description'].fillna('')
        
        # Calculate text similarity
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(df['description'])
        app_data['cosine_sim'] = cosine_similarity(tfidf_matrix, tfidf_matrix)
        app_data['df'] = df

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/recommend', methods=['POST'])
def recommend():
    init_recommender()
    title = request.json.get('title')
    df = app_data['df']
    cosine_sim = app_data['cosine_sim']
    
    try:
        # Find the movie index (case-insensitive)
        idx = df.index[df['title'].str.lower() == title.lower()].tolist()[0]
    except IndexError:
        return jsonify([]) # Return empty if the movie isn't in the database

    # Get top 5 most similar movies
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    
    # Format and return the results
    result = df.iloc[movie_indices][['title', 'description']].to_dict('records')
    return jsonify(result)