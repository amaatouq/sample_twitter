__author__ = 'amaatouq'

from tweepy import StreamListener
import json, time, sys

class MyStreamListener(StreamListener):
    def __init__(self, api=None, fprefix='sample'):
        self.api = api
        self.counter = 0
        self.fprefix = fprefix
        self.output = open(fprefix + '.'
                           + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
        self.delout = open('delete.txt', 'a')

    def on_data(self, data):
        print 'got data '
        if 'in_reply_to_status' in data:
            print 'got reply'
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            print 'got limit ', json.loads(data)['limit']
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print warning['message']
            return False

    def on_status(self, status):
        print 'got status'
        self.output.write(status + "\n")

        # self.counter += 1

        # if self.counter >= 50000:
        #     print 'got 20000, I will write them to the file :)'
        #     self.output.close()
        #     self.output = open(self.fprefix + '.'
        #                        + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
        #     self.counter = 0

        return

    def on_delete(self, status_id, user_id):
        self.delout.write(str(status_id) + "\n")
        return

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        print 'got an error ', status_code
        # return False
        return

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        print 'Timedout sleeping for 60 seconds'
        time.sleep(60)
        return
