from flask import Flask
import spacy
nlp = spacy.load("en_core_web_sm")
app = Flask(__name__)


x = "Embracing and analyzing self failures (of however multitude )is a virtue of nobelmen"

doc = nlp(x)

@app.route('/')
def hello():
    tokens = (token.text for token in doc)
    print(tokens)
    return "Hello Worls"
if __name__ == '__main__' :
    app.run()