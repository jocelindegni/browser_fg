from flask import Flask, request
from hashlib import blake2b
app = Flask(__name__)
# Database uri
app.config["MONGO_URI"] = "mongodb://localhost:27017/fg"

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/fingerprints', methods=['POST'])
def save_fingerprint():
    # Get fingerprint from data
    fingerprint = request.get_json(force=True)['fingerprint']
    # hash
    hash = blake2b(digest_size=10)
    hash.update(fingerprint.encode())
    hash_id = hash.hexdigest()
    # check if fg all right exist in database

    # else save in database
    return hash_id


@app.route('/fingerprints', methods=['GET'])
def get_all_fingerprints():
    return 'fingerprint'


if __name__ == '__main__':
    app.run()
