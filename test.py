from tester import Tester
from setting import *


def schedule_tester(TESTER_CYCLE):
    tester = Tester()
    while True:
        tester.run()


if __name__ == "__main__":
    schedule_tester(TESTER_CYCLE)
