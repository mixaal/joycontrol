#import requests
import http.client

class JoyApi(object):
   def __init__(self):
       self.base_uri = 'http://localhost:5000'

   def _post(self, path):
       try:
           conn = http.client.HTTPConnection("localhost", 5000)
           conn.request("POST", path)
       except Exception as e:
           print(str(e))

   def press_a(self):
       self._post('/press/a')

   def press_b(self):
       self._post('/press/b')

   def press_x(self):
       self._post('/press/x')

   def press_y(self):
       self._post('/press/y')


   def press_up(self):
       self._post('/press/up')

   def press_down(self):
       self._post('/press/down')

   def press_left(self):
       self._post('/press/left')

   def press_right(self):
       self._post('/press/right')
