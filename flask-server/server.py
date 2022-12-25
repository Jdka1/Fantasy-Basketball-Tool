from flask import Flask

import parsing
import stats_scraper


scraper = stats_scraper.Scraper(parser=parsing.Parser())

app = Flask(__name__)


# Stats API Route
@app.route("/per_game_averages/<year>")
def per_game_averages(year):
    return scraper.player_stats_per_game(year)

# Test Route
@app.route("/test")
def test():
    return {"test?": "test."}


if __name__ == "__main__":
    app.run(debug=True)