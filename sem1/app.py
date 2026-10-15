from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/visitor/<name>')
def hello_visitor(name):
    return render_template('visitor.html', visitor=name)

@app.route('/static')
def static_page():
    return render_template('static_index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)
