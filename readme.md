
# simple match making routine

Each row of the dataset represent a verctor if user preferences.
Each preference is expressed on a scale from 0 to 10.

The raking works by computing the cosine-similarity function
for each user against all others. Then we rank the results
and we match users that have the most similar preferences.

Constraints can be easily added by seading the "busy" set.

# example

     $./ranking.py 
     user6 <-> user1
     user4 <-> user3
     user5 <-> user2

# reference : 
http://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/
