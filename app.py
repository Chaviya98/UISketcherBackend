from flask import Flask, request
import spacy
from spacy.pipeline import EntityRuler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm")
ruler = EntityRuler(nlp)
patterns = [{"label": "UI", "pattern": "button"}, {"label": "UI", "pattern": "textinput"},
            {"label": "UI", "pattern": "card"}, {"label": "UI", "pattern": "imageview"},
            {"label": "UI", "pattern": "header"}, {"label": "UI", "pattern": "textview"}]
ruler.add_patterns(patterns)
nlp.add_pipe(ruler)
all_stopwords = nlp.Defaults.stop_words


@app.route('/extract/data', methods=['GET', 'POST'])
def extract_data():

        # Preparing data for tokenizing
        doc = nlp(" ".join(request.data.decode('UTF-8').lower().split()))

        # Tokenizing , stop words removing and unnecessary characters removing
        tokens = [token.text for token in doc if not token.is_punct if not token.is_stop]

        # Converting list of token into string
        list_to_str = ' '.join(map(str, tokens))

        # Preparing to entity recognition
        doc2 = nlp(list_to_str)

        # entity recognition
        entity_recognition = [(ent.text, ent.label_) for ent in doc2.ents]

        # json_format = json.dumps(entity_recognition)

        if len(entity_recognition) == 0:
            print("No UI elements detected")

        else:
            if len(entity_recognition) < 2:
                # Preparing the response json
                response_type = {
                    "data": {
                        "element": ent.text for ent in doc2.ents
                    }
                }
                return response_type
            else:
                print("Multiple UI Element Detected")


if __name__ == '__main__':
    app.run()

