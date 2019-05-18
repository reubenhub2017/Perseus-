import sys
sys.path.insert(0, 'ext/imports/')
import dependecies
from main import Controller



def start():
    test = Controller("this runs")
    test.run()
    test.runvisuals()


if __name__ == '__main__':
    start()
