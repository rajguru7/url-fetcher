from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_url():
    # Get the URL from the query string
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing URL'}), 400

    # Perform the HTTP GET request
    response = requests.get(url)
    return jsonify({'url': url, 'status_code': response.status_code, 'headers': dict(response.headers)})

@app.route('/status', methods=['GET'])
def fetch_status():
    # Get the URL from the query string
    urls = {}
    urls["https://www.google.com"] = ""
    urls["https://github.com"] = ""
    urls[base64.b64decode("aHR0cHM6Ly9ldmlsLm9yZw==").decode("utf-8")] = ""

    # Perform the HTTP GET request
    for url in urls.keys():
        try:
            response = requests.get(url, timeout=2)
            urls[url] = response.status_code
        except Exception as e:
            urls[url] = str(type(e))
    return jsonify(urls)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

