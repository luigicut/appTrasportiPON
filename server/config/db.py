from mongoengine import connect
MONGO_DBNAME = process.env.MONGO_ATLAS_NAME
MONGO_HOST = process.env.MONGO_ATLAS_CONNECTION
# MONGO_PORT = 27017


def initialize_db():
    connect(MONGO_DBAME, host=MONGO_HOST)