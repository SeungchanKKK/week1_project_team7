from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.8wjkf.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta



@app.route('/')
def home():
    return render_template('index.html')

@app.route("/item", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    sel_receive = request.form['sel_give']


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']





    doc = {
        'title':title,
        'image':image,
        'sel':sel_receive
    }

    db.item.insert_one(doc)

    return jsonify({'msg':'게시 완료'})

@app.route("/item", methods=["GET"])
def movie_get():
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

