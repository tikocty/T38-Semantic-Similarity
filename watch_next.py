# import the package and model to run the NLP
import spacy
nlp = spacy.load('en_core_web_md')

# open the film of the film description and close it after reading the lines
file = open('movies.txt', 'r+')
lines = file.readlines()
file.close()

# declare the empty list, match rate and film details for later use
nlp_list = []
match_rate = 0
film_details = ""

# passing every line in the txt file to the NLP model for analysis,
# and write the line in the nlp_list which declare in the previous step
for line in lines:
    nlp_line = nlp(line)
    nlp_list.append(nlp_line)

# declare the hulk details and pass it to the NLP mmodel
planet_hulk = """
Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.
"""
nlp_planet_hulk = nlp(planet_hulk)

# compare the similarity of hulk and others film by the for loop, and store the highest similarity film details
for nlp_line in nlp_list:
    if nlp_line.similarity(nlp_planet_hulk) > match_rate:
        match_rate = nlp_line.similarity(nlp_planet_hulk)
        film_details = nlp_line

# print out the recommendation
print(f"""
Recommendation for you: 
{film_details} 
match rate: {match_rate}
""")


