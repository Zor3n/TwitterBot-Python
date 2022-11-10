import json
from random import seed, randint

with open('quotes/quotes.json', 'rb') as f:
    try:
        data = json.load(f)
        num_authors = len(data)
        
        rand_author_num = randint(0, num_authors - 2)
        author_object = data[rand_author_num]

        num_quotes = len(author_object['phr'])
        rand_quote_num = randint(0, num_quotes - 1)
        quote = author_object['phr'][rand_quote_num]
        author = author_object['author']

        final_quote = f"\"{quote}\".\n\n"
        final_tweet = f'{final_quote}'+u'\u202B'+author

    except Exception as e:
        print(f'Error: Some error has occurred. D: Continuing... ({e})')