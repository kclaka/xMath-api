from flask import Flask
from flask_cors import CORS
from routes.router import register_routes


app = Flask(__name__)

# Enable CORS
CORS(app)  # Allow all origins by default

register_routes(app)



# Only run the app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Use debug=False in production