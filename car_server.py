import grpc
from concurrent import futures
import time

# import the generated classes
import car_app_pb2
import car_app_pb2_grpc


# import the original

# create a class to define the server functions, derived from
# hotel_app_pb2_grpc.HotelApplicationServicer
class CarApplication(car_app_pb2_grpc.CarApplicationServicer):

    # The Services are exposed in here
    def CarList(self, request, context):
        return car_app_pb2.SysMessage(message='You have selected %s: All our Car Are Availalbe\n'%request.value)

    def CarReserv(self, request, context):
        return car_app_pb2.SysMessage(message='You have selected %s: Thans for using our service to Reserve your Car\n'%request.value)

    def CarDisplay(self, request, context):
        return car_app_pb2.SysMessage(message='You have selected %s: Display your Car Reservation. Enjoy your trip\n'%request.value)

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_HotelApplicationServicer_to_server`
# to add the defined class to the server
car_app_pb2_grpc.add_CarApplicationServicer_to_server(CarApplication(), server)

# listen on port 50051
print('Car Server Running.')
print('Starting server. Listening on port 50053.')
server.add_insecure_port('[::]:50053')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)