import spacy
from spacy.pipeline import EntityRuler
nlp = spacy.load("en_core_web_sm")
ruler = EntityRuler(nlp)
patterns = [{"label": "UI", "pattern": "button"}]
ruler.add_patterns(patterns)
nlp.add_pipe(ruler)
all_stopwords = nlp.Defaults.stop_words

text = "I want a was Button !  with a TITLE called submit because."

#  "nlp" Object is used to create documents with linguistic annotations.
#  join() along with string split() functions are used to remove all the duplicate whitespaces and newline characters.
doc = nlp(" ".join(text.lower().split()))

tokens = [token.text for token in doc if not token.is_punct if not token.is_stop]

print(tokens)
# # Create list of word tokens after removing stopwords
# text_without_stopwords = [word for word in tokens if not word in all_stopwords]
#
# print(text_without_stopwords)
listToStr = ' '.join(map(str, tokens))
doc2 = nlp(listToStr)
print([(ent.text, ent.label_) for ent in doc2.ents])
