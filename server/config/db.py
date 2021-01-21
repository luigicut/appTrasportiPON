from mongoengine import connect
import os
MONGO_DBNAME = os.environ.get('MONGO_ATLAS_NAME') 
MONGO_HOST = os.environ.get('MONGO_ATLAS_CONNECTION')
# MONGO_PORT = 27017


def initialize_db():
    connect(MONGO_DBAME, host=MONGO_HOST)