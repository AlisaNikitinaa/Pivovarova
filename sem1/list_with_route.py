from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/vowels', methods=['GET', 'POST'])
def count_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_word = 'Burmalda'
    found = []
    for letter in new_word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)
    print(found)
    return render_template('dynamic_page.html', word=new_word, found=found)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
