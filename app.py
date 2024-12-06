from . import create_app

# Create an application instance
app = create_app()

# Only run the app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Use debug=False in production