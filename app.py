from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    word_count = None
    char_count = None
    word_freq = {}

    if request.method == 'POST':
        text = request.form['text']
        
        words = [word.strip().lower() for word in text.split() if word.strip()]
        
        word_count = len(words)
        char_count = len(text)

        # Count frequency
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

    return render_template(
        'index.html',
        word_count=word_count,
        char_count=char_count,
        word_freq=word_freq
    )

if __name__ == '__main__':
    app.run(debug=True)