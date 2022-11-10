from os import system
from client import client
from quotes.retrieve_quotes import final_tweet

try:
    tweet = final_tweet
    print(tweet)

    if (len(tweet) <= 280):
        user_approval = input('\n¿Désea tuítear la frase anterior? (Y):')
        if (user_approval.lower() == 'y'):
            print('\nEl tuít se ha aprovado')
            response = client.create_tweet(
                text=final_tweet
            )
        else:
            print('\nEl tuít se ha cancelado')
    else:
        print('\nThe tweet is too long')
except:
    print("An exception occurred")


