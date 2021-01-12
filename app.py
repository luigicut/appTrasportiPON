from flask import Flask, request, jsonify
from server.config.db import initialize_db
# from server.features.entry.population import populate_all

# setup server
appTrasporti = Flask(__name__)
# initialize_db()

if __name__ == '__main__':
    appTrasporti.run(debug=True)


