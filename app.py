from flask import Flask, render_template, request,url_for
import requests

app = Flask(__name__)
NEWS_API_KEY = '0c70c8cd8bc6417aa3cf459c33c2eca7'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def index():
    params = {
        'apiKey': NEWS_API_KEY,
        'category':'general',
        'country':'in',
        'pagesize':10
    }
    response = requests.get(url=NEWS_API_URL,params=params)
    news_data = response.json()
    articles = news_data['articles']

    return render_template('starts.html',category='general',articles=articles)
@app.route('/search',methods=['GET'])
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        params = {
            'apiKey': NEWS_API_KEY,
            'q': query,
            'language': 'en',
            'pageSize': 10  # Change as needed
        }
        response = requests.get(NEWS_API_URL, params=params)
        news_data = response.json()
        articles = news_data['articles']
        return render_template('search.html', query=query, articles=articles)
    else:
        return render_template("starts.html")  # Redirect to the home page if the query is empty
@app.route('/Home')
def Home():
    params = {
        'apiKey': NEWS_API_KEY,
        'category':'general',
        'country':'in',
        'pagesize':10
    }
    response = requests.get(url=NEWS_API_URL,params=params)
    news_data = response.json()
    articles = news_data['articles']

    return render_template('starts.html',category='general',articles=articles)
@app.route('/sports')
def sports():
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'in',
        'category': 'sports',
        'pageSize': 10  # Change as needed
    }
    response = requests.get(NEWS_API_URL, params=params)
    news_data = response.json()
    articles = news_data['articles']
    return render_template('category.html', category='Sports', articles=articles)

@app.route('/entertainment')
def entertainment():
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'in',
        'category': 'entertainment',
        'pageSize': 10  # Change as needed
    }
    response = requests.get(NEWS_API_URL, params=params)
    news_data = response.json()
    articles = news_data['articles']
    return render_template('category.html', category='Entertainment', articles=articles)

@app.route('/politics')
def politics():
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'in',
        'category': 'politics',
        'pageSize': 10  # Change as needed
    }
    response = requests.get(NEWS_API_URL, params=params)
    news_data = response.json()
    articles = news_data['articles']
    return render_template('category.html', category='Politics', articles=articles)
@app.route('/Health')
def health():
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'in',
        'category': 'Health',
        'pageSize': 10  # Change as needed
    }
    response = requests.get(NEWS_API_URL, params=params)
    news_data = response.json()
    articles = news_data['articles']
    return render_template('category.html', category='Health', articles=articles)
@app.route('/Technology')
def tech():
    params ={
        'apikey':NEWS_API_KEY,
        'country':'in',
        'category':'Technology',
        'pageSize':20
    }
    response = requests.get(NEWS_API_URL,params=params)
    news_data = response.json()
    articles = news_data['articles']
    return render_template('category.html',category='Technology',articles=articles)
@app.route('/Business')
def bus():
    params ={
        'apikey':NEWS_API_KEY,
        'country':'in',
        'category':'Business',
        'pageSize':20
    }
    response = requests.get(NEWS_API_URL,params=params)
    news_data = response.json()
    articles = news_data['articles']
    return render_template('category.html', category ="Business",articles=articles)
if __name__ == '__main__':
    app.run(debug=True)
