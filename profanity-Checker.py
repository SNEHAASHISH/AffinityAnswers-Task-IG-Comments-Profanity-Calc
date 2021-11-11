
from profanity_check import predict, predict_prob

# predict() takes an array and returns a 1 for each string if it is offensive, else 0.
# predict_prob() takes an array and returns the probability each string is offensive

with open('instagramComments.txt', 'r') as igComments:
    for line in igComments:
        flag_arr = predict([line])
        flag = flag_arr[0]
        if flag == 0:
            print('Line has no offensive language')
        else:
            val_profanity_arr = predict_prob([line])
            val_profanity = val_profanity_arr[0]
            print('The line has offensive language and degree of profanity is ' + val_profanity)
