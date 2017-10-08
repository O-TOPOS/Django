from django.shortcuts import render
from django.http import HttpResponse
import psycopg2 as ps

class Database:

    def __init__(self):

        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = ps.connect(
                database='test',
                user='postgres',
                host='localhost',
                port=5432,
                password='admin')

            self.cursor = self.connection.cursor()

        except Exception as e:
            print('Cannot connect to the server!')

    def close(self):
        try:
            self.connection.close()
        except Exception as e:
            print('Cannot close the connection to the server!')


# Create your views here.
def index(request):
    db = Database()
    db.connect()
    db = Database()
    db.connect()
    sql = "SELECT ST_AsGeoJSON(geom) FROM hembrug.hembrug"
    db.cursor.execute(sql)
    data = db.cursor.fetchall()
    return render(request, 'index.html', {'data':data})