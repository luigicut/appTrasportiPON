from mongoengine import connect
MONGO_DBNAME = 'appTrasporti'
MONGO_HOST = 'mongodb://localhost:27017/appTrasporti'
MONGO_PORT = 27017


def initialize_db():
    connect(MONGO_DBAME, host=MONGO_HOST, port=MONGO_PORT)