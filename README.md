# AffinityAnswers-Task-IG-Comments-Profanity-Calc

Task:-

Imagine there is a file full of Instagram comments by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file.

Approach:-

I am using an in-built Python library profanity-check

To install it execute this command on terminal - pip3 install profanity-check

Prime reason to do so is that the conventional method used by many profanity checker libraries/programs involves a hard-coded list of bad words to detect and filter profanity, which is a glaring issue.

In terms of performance profanity-check is much faster than profanity-filter.
This is because profanity-check uses a 'Bag-of-Words' model to vectorize input strings before feeding them to a linear classifier. 
While the latter uses sophisticated methods to do so at the cost of performance.

However, this library is far from perfect. 
For example, it has a hard time picking up on less common variants of swear words 
like "f4ck you" or "you b1tch" because they don't appear often enough in the training corpus.
