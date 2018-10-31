import grpc
from concurrent import futures
import time

# import the generated classes
import airline_app_pb2
import airline_app_pb2_grpc


# import the original

# create a class to define the server functions, derived from
# hotel_app_pb2_grpc.HotelApplicationServicer
class AirlineApplication(airline_app_pb2_grpc.AirlineApplicationServicer):

    # The Services are exposed in here
    def AirlineList(self, request, context):
        return airline_app_pb2.SysMessage(message='You have selected %s: All our Flights Are Availalbe\n'%request.value)

    def AirlineReserv(self, request, context):
        return airline_app_pb2.SysMessage(message='You have selected %s: Thans for using our service to Reserve your Flight\n'%request.value)

    def AirlineDisplay(self, request, context):
        return airline_app_pb2.SysMessage(message='You have selected %s: Display your Flight Reservation. Enjoy your trip\n'%request.value)

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_HotelApplicationServicer_to_server`
# to add the defined class to the server
airline_app_pb2_grpc.add_AirlineApplicationServicer_to_server(AirlineApplication(), server)

# listen on port 50051
print('Airline Server Running.')
print('Starting server. Listening on port 50052.')
server.add_insecure_port('[::]:50052')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)