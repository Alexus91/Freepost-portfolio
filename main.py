from webapp import create_app

# Create the Flask application using the create_app function
app = create_app()

# Run the Flask application if this script is the main entry point
if __name__ == "__main__":
    app.run(debug=False)


