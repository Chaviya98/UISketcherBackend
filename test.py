from flask import Flask
import spacy
from spacy.pipeline import EntityRuler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm")
ruler = EntityRuler(nlp)
patterns = [{"label": "UI", "pattern": "button"}, {"label": "UI", "pattern": "input"}]
ruler.add_patterns(patterns)
nlp.add_pipe(ruler)
all_stopwords = nlp.Defaults.stop_words

print("------Please Enter Data------")
inputData = input()
#TempData = "I want a button called submit."

# Preparing data for tokenizing
doc = nlp(" ".join(inputData.lower().split()))

# Tokenizing , stop words removing and unnecessary characters removing
tokens = [token.text for token in doc if not token.is_punct if not token.is_stop]

# Converting list of token into string
list_to_str = ' '.join(map(str, tokens))

# Preparing to entity recognition
doc2 = nlp(list_to_str)

# entity recognition
entity_recognition = [(ent.text, ent.label_) for ent in doc2.ents]

# json_format = json.dumps(entity_recognition)

print("------Extracted Information------")

if len(entity_recognition) == 0:
    print("No UI Element Detected")

else:
    if len(entity_recognition) < 2:
        # Preparing the response json
        response_type = {
        "data": {
            "element": ent.text for ent in doc2.ents
            }
         }
        print(response_type)
    else:
        print("Multiple UI Elements Detected")
