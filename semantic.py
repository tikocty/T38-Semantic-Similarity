#-----SIMILARITY WITH SPACY

import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


#-----WORKING WITH VECTORS
tokens = nlp('cat apple monkey banana ')
for token1 in tokens: 
     for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))


#-----WORKING WITH SENTENCES
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)

"""
Note:
The simliarities bewteen these three words descending order,
Cat/Monkey, is the highest because both of them are animals
Monkey/Banana, is the second highest because banana is one of the monkey favourite food, at least in the cartoon
Cat/Banana is the lowest, because apple is not the main food of cat
"""