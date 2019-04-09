import requests
import time
import threading
lock = threading.Lock()


datas = list()

def thread_1():            #take the data from the website
    global datas
    while True:
        response = requests.get('http://api.open-notify.org/iss-now.json')
        data = response.json()
        longitude = data['iss_position']['longitude']
        latitude = data['iss_position']['latitude']
        timestamp = data['timestamp']
        with lock:
            datas.append((float(longitude), float(latitude), float(timestamp)))

        # print("longitude : " , longitude)
        # print("latitude : ", latitude)
        # print("time stamp: ", timestamp)

        time.sleep(1)

differences = list()
def thread_dif():                           #Do the operations (calculate differences and appending it to list)
    global differences
    current = 1
    while True:
        with lock:
            if len(datas) > current + 5:
                # print(datas[current])
                differences.append((
                    (datas[current][0] - datas[current-1][0]),
                    (datas[current][1] - datas[current-1][1])
                ))

                current += 1

        #print(datas)
                print(differences[-1])


t = threading.Thread(target=thread_1, name = "thread_1")
t2 = threading.Thread(target=thread_dif, name = "thread_diff")
t.start()
t2.start()


