import grpc
from concurrent import futures
import time

# import the generated classes
import hotel_app_pb2
import hotel_app_pb2_grpc


# import the original

# create a class to define the server functions, derived from
# hotel_app_pb2_grpc.HotelApplicationServicer
class HotelApplication(hotel_app_pb2_grpc.HotelApplicationServicer):

    # The Services are exposed in here
    def HotelList(self, request, context):
        return hotel_app_pb2.SysMessage(message='You have selected %s: All our Hotels Are Availalbe\n'%request.value)

    def HotelReserv(self, request, context):
        return hotel_app_pb2.SysMessage(message='You have selected %s: Thans for using our service to Reserve your Hotel\n'%request.value)

    def HotelDisplay(self, request, context):
        return hotel_app_pb2.SysMessage(message='You have selected %s: Display your Hotel Reservation. Enjoy your trip\n'%request.value)

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_HotelApplicationServicer_to_server`
# to add the defined class to the server
hotel_app_pb2_grpc.add_HotelApplicationServicer_to_server(HotelApplication(), server)

# listen on port 50051
print('Hotel Server Running.')
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)