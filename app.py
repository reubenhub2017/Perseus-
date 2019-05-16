import sys
sys.path.insert(0, 'src/MVC/controller/')
from main import Controller

def start():
    test = Controller("this runs")
    test.run()

if __name__ == '__main__':
    start()
