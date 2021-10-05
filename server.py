import socket
from _thread import *
import sys
server = "0.0.0.0"
port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET tells us about host and port, SOCK_STREAM is the default
try:
  s.bind((server, port))
except socket.error as e:
  print(str(e))
s.listen(2)
print("waiting for connection, server started")
def threaded_client(con):
  con.send(str.encode("connected"))
  print("connected")
  reply = ""
  while True:
    try:
      data = con.recv(2048) #i thought 2048 was a game
      reply = data.decode("utf-8")
      if not data:
        print("disconnected")
        break
      else:
        print("receive:", reply)
        con.send(str.encode(reply))
    except:
      break
  print("lost connection")
  con.close()
while True:
  con, addr = s.accept()
  start_new_thread(threaded_client,(con,))
