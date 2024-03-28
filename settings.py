from dotenv import load_dotenv

load_dotenv()
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_URI = 'localhost:5432'
DB_PASSWORD = ''

AUTH0_DOMAIN = 'kavyasrik.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'casting'