import threading, time, random

data_pool = []
results =[]
lock = threading.Lock()

def data_producer(worker_id):
    """Erzeugt Daten"""
    for i in range(3):
        with lock:  #Synchronisiere Zugriff
            new_data = f"Daten-{worker_id}-{i}"
            data_pool.append( new_data)
            print(f"🟢 PRODUCER {worker_id} erzeugt: {new_data}")
    time.sleep(random.uniform(0.1, 0.5))


dc_test = threading.Thread(target=data_producer, args=(1))
dc_test.start()