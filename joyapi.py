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

   def lstick_vert(self, value):
       self._post('/stick/l/v?value='+str(value))

   def lstick_horiz(self, value):
       self._post('/stick/l/h?value='+str(value))

   def rstick_vert(self, value):
       self._post('/stick/r/v?value='+str(value))

   def rstick_horiz(self, value):
       self._post('/stick/r/h?value='+str(value))

   def rstick_left(self):
       self._post('/stick/r/left')

   def rstick_right(self):
       self._post('/stick/r/right')

   def rstick_up(self):
       self._post('/stick/r/up')

   def rstick_down(self):
       self._post('/stick/r/down')

   def rstick_center(self):
       self._post('/stick/r/center')

   def lstick_left(self):
       self._post('/stick/l/left')

   def lstick_right(self):
       self._post('/stick/l/right')

   def lstick_up(self):
       self._post('/stick/l/up')

   def lstick_down(self):
       self._post('/stick/l/down')

   def lstick_center(self):
       self._post('/stick/l/center')

   def release_a(self):
       self._post('/release/a')

   def release_b(self):
       self._post('/release/b')

   def release_x(self):
       self._post('/release/x')

   def release_y(self):
       self._post('/release/y')

   def release_up(self):
       self._post('/release/up')

   def release_down(self):
       self._post('/release/down')

   def release_left(self):
       self._post('/release/left')

   def release_right(self):
       self._post('/release/right')

   def release_zr(self):
       self._post('/release/zr')

   def release_zl(self):
       self._post('/release/zl')

   def release_r(self):
       self._post('/release/r')

   def release_l(self):
       self._post('/release/l')



   def hold_a(self):
       self._post('/hold/a')

   def hold_b(self):
       self._post('/hold/b')

   def hold_x(self):
       self._post('/hold/x')

   def hold_y(self):
       self._post('/hold/y')

   def hold_up(self):
       self._post('/hold/up')

   def hold_down(self):
       self._post('/hold/down')

   def hold_left(self):
       self._post('/hold/left')

   def hold_right(self):
       self._post('/hold/right')

   def hold_zr(self):
       self._post('/hold/zr')

   def hold_zl(self):
       self._post('/hold/zl')

   def hold_r(self):
       self._post('/hold/r')

   def hold_l(self):
       self._post('/hold/l')

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

   def press_home(self):
       self._post('/press/home')

   def press_capture(self):
       self._post('/press/capture')


   def press_plus(self):
       self._post('/press/plus')

   def press_minus(self):
       self._post('/press/minus')
