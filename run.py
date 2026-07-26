from app import create_app

# Create the application instance
app = create_app()

if __name__ == '__main__':
    # Run the server. Debug mode is on by default via our .env file.
    app.run(port=5000)