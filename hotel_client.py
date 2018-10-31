import grpc

# import the generated classes
import hotel_app_pb2
import hotel_app_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = hotel_app_pb2_grpc.HotelApplicationStub(channel)

#make the call
response = stub.HotelList(hotel_app_pb2.Selection(value='A'))

#Listo
print(response.message)