import unittest
from testqueue import TestQueue
from linkedqueue import LinkedQueue

class TestListQueue(unittest.TestCase, TestQueue):

    def newQueue(self):
        return LinkedQueue()

if __name__ == '__main__':
    unittest.main()
