import threading
import tweetvideo
import queue

def queue_func(name, number, filepath1, filepath2,consumer_key, consumer_secret,access_key, access_secret):
    q = queue.Queue()
    q.put(tweetvideo.googlevision(name, number, filepath1, filepath2,consumer_key, consumer_secret,access_key, access_secret))
    q.put(tweetvideo.Image2Video(name, filepath1))
    while not queue.Empty():
        q.get()

def pipelining(names:list, numbers:list, filepath1:list, filepath2:list,consumer_key, consumer_secret,access_key, access_secret):
    """
    x = 0
    thread_list = []
    for i in range(len(names)):
        t1 = threading.Thread(target = tweetvideo.googlevision, name = 't1{}'.format(i), args = (names[i],numbers[i],filepath1[i],filepath2[i]))
        t1.start()
        thread_list.append(t1)
        
    for t in thread_list:
        t.join()
        tweetvideo.Image2Video(names[x],filepath1[x])
        x += 1
    """
    for i in range(len(names)):
        
        t1 = threading.Thread(target = queue_func, name = 't1{}'.format(i), args = (names[i],numbers[i],filepath1[i],filepath2[i],consumer_key, consumer_secret,access_key, access_secret))
        t1.start()



    