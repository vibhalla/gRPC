# gRPC Server that returns the current time in the requested time zone

import grpc
from concurrent import futures
import time
import timer_pb2_grpc as pb2_grpc
import timer_pb2 as pb2
from datetime import datetime
import pytz 

class TimeService(pb2_grpc.TimeServiceServicer):

   def __init__(self, *args, **kwargs):
       pass

   def giveTime(self, request, context):
        
        TZ = request.TimeZone
        TimeZone = pytz.timezone(TZ)
        utc_time = datetime.now(tz=pytz.utc)
        result = f'Hello the current time in the timezone  "{TimeZone}" is "{utc_time.astimezone(TimeZone).isoformat()}"'
        result = {'Result' : result}
        #print(f'{result}')
        return pb2.TimeResp(**result)



def serve():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   pb2_grpc.add_TimeServiceServicer_to_server(TimeService(), server)
   server.add_insecure_port('[::]:50051')
   server.start()
   server.wait_for_termination()


if __name__ == '__main__':
   serve()
