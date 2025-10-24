from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This command tells Flask to find 'index.html' 
    # in the 'templates' folder and show it.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)