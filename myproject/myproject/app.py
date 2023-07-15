from myspider import scraper_function
from flask import Flask, request, render_template
import sys
# add the parent directory of SearchEngine to the sys.path
sys.path.append('..')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def search_patents():
    if request.method == 'POST':
        query = request.form['query']
        # call your web scraper function with the query
        results = scraper_function(query)
        return render_template('results.html', results=results)
    else:
        return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
