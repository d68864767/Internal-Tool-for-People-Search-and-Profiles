# app.py

from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
from config import DevelopmentConfig
import requests
import search
import data_ingestion

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

es = Elasticsearch(app.config['ELASTICSEARCH_URL'])
gpt_index = app.config['GPT_INDEX_URL']
data_warehouse = app.config['DATA_WAREHOUSE_URL']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = search.perform_search(es, gpt_index, query)
        return render_template('search_results.html', results=results)
    else:
        return render_template('search.html')

@app.route('/profile/<id>')
def profile(id):
    profile_data = data_ingestion.get_profile_data(data_warehouse, id)
    return render_template('profile.html', profile=profile_data)

if __name__ == '__main__':
    app.run(debug=True)
