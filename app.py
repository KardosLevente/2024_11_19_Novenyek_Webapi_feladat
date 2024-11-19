from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

plants = [
    {"name": "Monstera", "type": "Szobanövény", "feature": "Nagyméretű levelek"},
    {"name": "Bambusz", "type": "Dísznövény", "feature": "Gyors növekedés"},
    {"name": "Kaktusz", "type": "Pozsgás", "feature": "Szárazságtűrő"}
]

@app.route('/', methods=["GET"])
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
# @app.route('/tabla', methods=["GET"])

