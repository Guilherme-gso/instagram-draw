import random
from crawler import Crawler
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/draw', methods=['POST'])
def draw():
  post_url = request.json['post_url']
  crawler = Crawler()
  comments = crawler.get_comments(post_url)
  r = random.randint(0, len(comments))
  chosen_comment = comments[r]
  return jsonify(chosen_comment)

if __name__ == '__main__':
  app.run(debug=True)





