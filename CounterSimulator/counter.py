import threading, time

def counter(sec):
    i=0
    while i<sec:
        print(i)
        i+=1
        time.sleep(0.01)


#counter(50)

cnt=0
def counter_thread(freq):
    global cnt
    while True:
        cnt +=1
        print(f"{cnt}")
        time.sleep(1/freq)



if __name__ == "__main__":
    #mit deamon=true wird der Thread mit dem Hauptprogramm beendet.
    cnt_thr=threading.Thread(target=counter_thread, args=(100,),daemon=True)
    print("starte thread")
    cnt_thr.start()
    print("schlafe")
    time.sleep(5)
    #join wartet, bis das Thread beendet wird.
    #cnt_thr.join()
    print("fertig")
