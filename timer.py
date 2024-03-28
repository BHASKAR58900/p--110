import time
def countdown_timer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer)
        time.sleep(1)
        seconds-=1
seconds=input("enter seconds")
countdown_timer(int(seconds))