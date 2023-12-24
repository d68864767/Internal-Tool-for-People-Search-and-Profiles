# views.py

from flask import Blueprint, render_template, request, redirect, url_for
from models import Profile
from search import perform_search
from data_ingestion import get_profile_data

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = perform_search(query)
        return render_template('search_results.html', results=results)
    else:
        return redirect(url_for('home'))

@views.route('/profile/<id>')
def profile(id):
    profile_data = get_profile_data(id)
    if profile_data:
        return render_template('profile.html', profile=profile_data)
    else:
        return "Profile not found", 404
