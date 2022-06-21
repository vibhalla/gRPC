# Client program to get the current time in specific timezone
import grpc
import time
import timer_pb2_grpc as pb2_grpc
import timer_pb2 as pb2
 
 
class TimerClient(object):
   """
   Client for gRPC functionality
   """
 
   def __init__(self):
       self.host = 'localhost'
       self.server_port = 50051
 
       # instantiate a channel
       self.channel = grpc.insecure_channel(
           '{}:{}'.format(self.host, self.server_port))
 
       # bind the client and the server
       self.stub = pb2_grpc.TimeServiceStub(self.channel)
 
   def getTime(self, TimeZone):
       """
       Client function to call the rpc giveTime
       """
       #print(f'{TimeZone}')
       TZ = pb2.TimeReq(TimeZone=TimeZone)
       #print(f'{TZ}')
       return self.stub.giveTime(TZ)
 
 
if __name__ == '__main__':
   client = TimerClient()
   result = client.getTime(TimeZone="ASIA/Kolkata")
   print(f'{result}')