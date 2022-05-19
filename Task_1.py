import time

class TrafficLight:
    __color: list = ('red', 'yellow', 'green')

    def running(self):
        while True:
            for i in range(len(TrafficLight.__color)):
                if i == 0:
                    print(f'{TrafficLight.__color[i]} 4 сек')
                    time.sleep(4)
                elif i == 1:
                    print(f'{TrafficLight.__color[i]} 2 сек')
                    time.sleep(2)
                elif i == 2:
                    print(f'{TrafficLight.__color[i]} 3 сек')
                    time.sleep(3)

if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
