# CineMatch: Movie Recommendation System

A web-based movie recommendation application built with Python and Flask. The system processes a dataset of thousands of movies to provide accurate recommendations based on user queries, utilizing a lightweight SQLite database for rapid data retrieval and deployment.

## Live Demo
The application is deployed and live on Render: 
[https://movie-recommendation-system-72nn.onrender.com](https://movie-recommendation-system-72nn.onrender.com)

## System Architecture

*   **Backend Framework:** Python, Flask
*   **Database:** SQLite (managed via Flask-SQLAlchemy)
*   **Data Processing:** Pandas (for parsing and seeding TMDB dataset)
*   **Deployment Server:** Gunicorn
*   **Hosting Platform:** Render

## Features

*   **Automated Database Seeding:** Initializes and populates the SQLite database automatically on startup using the TMDB 5000 movies dataset.
*   **Recommendation Engine:** Queries and retrieves movie data based on user input.
*   **Web Interface:** Clean, responsive frontend for user interaction.

## Local Installation and Setup

To run this project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-directory>
