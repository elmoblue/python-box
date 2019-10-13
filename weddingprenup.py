import psycopg2
from  psycopg2 import Error

class  weddingPrenup:
    def __init__(self):
        self.minutes = ''

    def setDuration(self, args):
        self.minutes = args