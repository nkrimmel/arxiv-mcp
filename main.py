from flask import Flask, request, jsonify
import requests
from PyPDF2 import PdfReader
import io
import os

app = Flask(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"

@app.route('/search', methods=['GET'])
def search_papers():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    params = {
        'search_query': query,
        'start': 0,
        'max_results': 10
    }
    response = requests.get(ARXIV_API_URL, params=params)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data from Arxiv API"}), 500

    return response.text, 200

@app.route('/read_pdf', methods=['GET'])
def read_pdf():
    pdf_path = request.args.get('pdf_path')
    if not pdf_path:
        return jsonify({"error": "PDF path is required"}), 400

    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            text = "\n".join(page.extract_text() for page in pdf_reader.pages)
        return jsonify({"content": text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download_pdf', methods=['GET'])
def download_pdf():
    pdf_url = request.args.get('pdf_url')
    if not pdf_url:
        return jsonify({"error": "PDF URL is required"}), 400

    try:
        response = requests.get(pdf_url)
        if response.status_code != 200:
            return jsonify({"error": "Failed to download PDF"}), 500

        filename = pdf_url.split('/')[-1]
        filepath = os.path.join("downloads", filename)
        os.makedirs("downloads", exist_ok=True)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        return jsonify({"message": "PDF downloaded successfully", "file_path": filepath}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)