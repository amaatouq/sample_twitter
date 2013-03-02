__author__ = 'amaatouq'

import numpy as np
from Streaming import Streaming
# # my credentials for Twitter with amaatouq@gmail.com
# credential= {'consumer_key': '4Yd3iUGaFHltlezXYBJhFA',
#  'consumer_secret': 'oKeNDcOIWRfmpsWqgKntU1XCl0abZ1objWWiCGCo',
#  'access_token': '243804207-dXlUBW293YNz806LG3RcLfc5eXRWEkNQgPIVDTGY',
#  'access_token_secret': 'JcvyrAVgVwzpl6BXdNwRsOCUrhUt0M0hgLA3tGEVa1c'}


# # my credentials for Twitter with amaatouq@yahoo.com
# credential= {'consumer_key': 'cE3QBbAAouLyzSKnWa2eQ',
#  'consumer_secret': 'XRRcY3hdtk5cdtvwXAvn32gnS0h369phmghsejOrlvk',
#  'access_token': '1218854118-CRX9NrbnBjkqZCXkBXe7z0rl1jSGw94FEHmdOJB',
#  'access_token_secret': '2Pp2vNz8qnbTuwNE5nQljDDCDw4TWPWxRSBEi8xIC4'}




# my credentials for Twitter with amaatouq1@hotmail.com
credential= {'consumer_key': 'Gmv1OijQeEL6PLFxVJn0Hg',
 'consumer_secret': 's7VueE6tk4yIGnyz5qDGm8HfyPEUPbjviff6JK2g0',
 'access_token': '1233436285-8FmEdCSbuSzqJxDjgOT9O35OTcdtUvDv0YW73OJ',
 'access_token_secret': 'Fhg8rev0i7lYQwD9t2LyN0CQ3O1l8wDegenw9IxwlVU'}


# connecting to the stream
streaming = Streaming(credential)

# Riyadh "location=[46.56,24.50,47.00,24.85]""

# Start listening with the filters


def listen_to_location(location):
	streaming.listen(location=location)

def listen_to_users(list_of_users):
	streaming.listen(follow=list_of_users)

#listen_to_location(location=[46.56,24.50,47.00,24.85])

#getting spam from spam accounts
# spam = np.loadtxt('Helpers/spammers_id.csv',dtype='i16').tolist()
# print 'started listening'


# listen_to_users(spam)


#streaming.listen(location=[-180,-90,180,90],track='%20')


sampling = streaming.sample()