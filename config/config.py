import os

HOST = "127.0.0.1"
PRODUCTION_PORT = 80
DEBUG_PORT = 8080

# DEBUG = os.path.isfile('config/.debug')
DEBUG = True

if DEBUG:
    PORT = DEBUG_PORT
else:
    PORT = PRODUCTION_PORT
if os.getenv('PORT'):
    PORT = int(os.getenv('PORT'))
