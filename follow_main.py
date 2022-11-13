#1,000 users per request
#1,000 actions per day
#400 follow actions per day

from client import client, my_bot_id

def u_following():
    try:
        response = client.get_users_following(id=my_bot_id, user_auth=True)
        users = response.data #array with User objs [<User id=? name=? username=? >]
        errors = response.errors
        results = response.meta['result_count']
        
        if len(errors) > 0:
            print(errors)

        print(f'Total following users {results}')

        # follow action
        result = client.follow_user(target_user_id=3034916907, user_auth=True)
        result_response = result.data['following']
        result_errors = result.errors
        if len(result_errors) > 0:
            print('Some errors were found:')
            print(result_errors)

        if result_response == True:
            print('Following action succeded')
        # end follow action

        if results > 0:
            ''' In this case, I am using the only account that the bot follows '''
            user_to_id = users[0].id #3034916907
            # unfollow action
            # result = client.unfollow_user(target_user_id=user_to_id, user_auth=True)
            # result_response = result.data['following']
            # result_errors = result.errors
            # if len(result_errors) > 0:
            #     print('Some errors were found:')
            #     print(result_errors)

            # if result_response == False:
            #     print('Unfollowing action succeded')
            # end unfollow action
        
    except Exception as e:
        print(f"An exception occurred {e}")

def l_following():
    try:
        response = client.get_owned_lists(id=my_bot_id, user_auth=True)
        print(response)
    except Exception as e:
        print(f"An exception occurred {e}")

if __name__ == '__main__':
    l_following()