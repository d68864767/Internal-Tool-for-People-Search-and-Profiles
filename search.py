# search.py

from elasticsearch import Elasticsearch
import requests

def perform_search(es, gpt_index, query):
    # Perform a search using Elasticsearch
    es_search_result = es.search(
        index=gpt_index,
        body={
            "query": {
                "match": {
                    "content": query
                }
            }
        }
    )

    # Extract the hits from the search result
    es_hits = es_search_result['hits']['hits']

    # Perform a search using GPT-3
    gpt_search_result = requests.post(
        gpt_index,
        headers={"Content-Type": "application/json"},
        json={
            "prompt": query,
            "max_tokens": 60
        }
    ).json()

    # Combine the results from Elasticsearch and GPT-3
    combined_results = es_hits + gpt_search_result['choices']

    # Sort the combined results by score
    sorted_results = sorted(combined_results, key=lambda x: x['_score'], reverse=True)

    return sorted_results
