from flask import Flask, render_template, abort, redirect, url_for, request

app = Flask(__name__)

cards = [{"question": "What is your name?", "answer": "My name is Sachin"},
{"question": "Where do you study?", "answer": "I study at herald"}]

@app.route("/")
@app.route("/hello", methods = ['GET'])
def hello():
  return render_template('welcome.html', cards = cards)


@app.route("/cards/<int:index>")
def get_cards(index):
  try:
    return render_template('card.html', card = cards[index], index = index, total_cards = len(cards))
  except:
    abort(404)


@app.route("/delete-card/<int:index>", methods=['POST', 'GET'])
def delete_card(index):
  if (request.method == 'POST'):
    del cards[index]
    return redirect(url_for('hello'))
  else:
    return render_template('delete-card.html', index = index)