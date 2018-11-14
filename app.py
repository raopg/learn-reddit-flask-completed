from flask import Flask, render_template
import json
import reddit


app = Flask(__name__)

@app.route('/')
def index():
    my_reddit_instance = reddit.create_reddit_instance()
    my_ten_hot_list = reddit.ten_top_titles(my_reddit_instance, 'UCI')
    print(my_ten_hot_list)
    return render_template('index.html',posts = my_ten_hot_list,subreddit = 'UCI')

if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment