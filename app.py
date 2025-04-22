from flask import Flask, render_template
import random

app = Flask(__name__)

colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Black", "White"]


@app.route('/random-colors')
def random_colors():

    random_selected_colors = random.sample(colors, 3)
    return render_template('colors.html', colors=random_selected_colors)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

