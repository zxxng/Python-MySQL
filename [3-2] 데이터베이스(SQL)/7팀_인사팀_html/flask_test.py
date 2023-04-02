from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello1"

@app.route('/about')
def about():
    return render_template("about.html")

def main():
    app.run(debug=True,port=80)

if __name__ == '__main__':
    main()