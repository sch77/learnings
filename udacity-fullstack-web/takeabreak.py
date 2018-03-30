import time
import webbrowser

print "start the time accounting"
interval_seconds = 10
sleep_seconds = 10

start_time = time.time();
while True:
    current_time = time.time()
    cur_time_elapsed = current_time - start_time
    print cur_time_elapsed
    print "difference"
    print cur_time_elapsed-interval_seconds
    if cur_time_elapsed-interval_seconds >= 0:
        print "take a break!!!"
        webbrowser.open('http://youtube.com')
        time.sleep(sleep_seconds)
        start_time = time.time()
        continue


