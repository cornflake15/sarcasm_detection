import os
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy


app = Flask(__name__)

model = None

@app.route('/', methods=['POST', 'GET'])
def index():
    errors = []
    content = []
    result = None
    if request.method == 'POST':
        try:
            content.append(request.form['sentence-area'])
        except:
            errors.append(
                'Unable to get sentence. Please make sure it is valid and try again.'
            )
            return render_template('index.html', errors=errors)

        if content:
            # padded_content = padding(content)
            # print(padded_content)
            # print(type(padded_content))
            # result = model.predict(padded_content)
            # result = str(result[0][0])
            print(result)
            # result = [content]
            print(type(content))
            print(type(content[0]))
            # print(type(result))
    return render_template('index.html', results=content)

def padding(input_sentence):
    vocab_size = 1000
    max_length = 16
    trunc_type = 'post'
    padding_type =' post'
    oov_tok = '<OOV>'
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    sequences = tokenizer.texts_to_sequences(input_sentence)
    print(sequences)
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    print(padded)
    return padded

if __name__ == '__main__':
    MODEL_PATH = 'model/model_3_sarcasm.h5'
    model = load_model(MODEL_PATH)
    # import serving package
    from waitress import serve
	# serve on port 8080
    serve(app, host='localhost', port=8080)