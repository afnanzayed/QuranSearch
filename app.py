from flask import Flask, request, jsonify
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Search path
@app.route('/search', methods=['GET'])
def search_verse():
    query = request.args.get('query')  # Keyword
    if not query:
        return jsonify({'error': 'Query is required'}), 400

    # Request data from API
    url = f"https://api.alquran.cloud/v1/search/{query}/all/en"
    response = requests.get(url)
    # print("Response from API:", response.status_code, response.json())  # طباعة الرد


    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from API'}), 500

    # Extract only important data
    results = []
    data = response.json()
    for match in data.get('data', {}).get('matches', []):
        results.append({
            'surah': match['surah']['englishName'],
            'revelationType' : match['surah']['revelationType'],
            'ayah': match['numberInSurah'],
            'text': match['text']
        })
    print("Results being sent to frontend:", results)
    return jsonify({'results': results})

    # Extract all data
    # data = response.json()
    # return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
