from flask import Flask
from flask_restful import Resource, Api
import tweetvideo_threading
import tweet_keys

consumer_key = tweet_keys.consumer_key
consumer_secret = tweet_keys.consumer_secret
access_key = tweet_keys.access_key
access_secret = tweet_keys.access_secret

app = Flask(__name__)
api = Api(app)
"""
names, numbers, filepath1, filepath2 = []
consumer_key, consumer_secret,access_key, access_secret = ''
class twtvid(Resource):
    def put(self, names, numbers, filepath1, filepath2,consumer_key, consumer_secret,access_key, access_secret):
        tweetvideo_threading.pipelining(names, numbers, filepath1, filepath2,consumer_key, consumer_secret,access_key, access_secret)

api.add_resource(twtvid,'/')
@app.route('/', methods=['GET'])
def tweets2vid(self, names, numbers, filepath1, filepath2,consumer_key, consumer_secret,access_key, access_secret):
    tweetvideo_threading.pipelining(names, numbers, filepath1, filepath2,consumer_key, consumer_secret,access_key, access_secret)
    return 'check the desinated folder for video'
if __name__ == "__main__":
    app.run(debug = True)
"""

@app.route('/', methods=['GET'])
def tweets2vid(names, numbers, filepath1, filepath2,consumer_key, consumer_secret,access_key, access_secret):
    tweetvideo_threading.pipelining(names, numbers, filepath1, filepath2,consumer_key, consumer_secret,access_key, access_secret)
    return "work done"
if __name__ == "__main__":
    names = ['@DoseOfBeautiful','@realDonaldTrump','@LeagueOfLegends']
    filepath1 = ['C:/Users/Vanquish/Desktop/pyve/VisionApi/downloadimage1/',
        'C:/Users/Vanquish/Desktop/pyve/VisionApi/downloadimage2/',
        'C:/Users/Vanquish/Desktop/pyve/VisionApi/downloadimage3/']
    filepath2 = [r'C:\Users\Vanquish\Desktop\pyve\VisionApi\downloadimage1',
        r'C:\Users\Vanquish\Desktop\pyve\VisionApi\downloadimage2',
        r'C:\Users\Vanquish\Desktop\pyve\VisionApi\downloadimage3']
    numbers = [30,40,10]
    app.run(debug = True)