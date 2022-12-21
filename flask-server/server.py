from flask import Flask

app = Flask(__name__)


#Players API Rout
@app.route("/data")
def data():
    return {'players': {
        'player1': {
            'stat1': 1,
            'stat2': 2,
            'stat3': 3
        },
        'player2': {
            'stat1': 1,
            'stat2': 2,
            'stat3': 3
        },
    }}


if __name__ == "__main__":
    app.run(debug=True)