import grpc

# import the generated classes
import hotel_app_pb2
import hotel_app_pb2_grpc
import airline_app_pb2
import airline_app_pb2_grpc
import car_app_pb2
import car_app_pb2_grpc


def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "A. Hotel Options"
    print "B. Airline Options"
    print "C. Car Options"
    print "D. Exit"
    print 67 * "-"

def print_hotelmenu():       ## Your menu design here
    print 30 * "-" , "HOTEL" , 30 * "-"
    print "A. Hotel List"
    print "B. Hotel Reserve"
    print "C. Hotel Display Reservation"
    print "D. Exit"
    print 67 * "-"

def print_airlinemenu():       ## Your menu design here
    print 30 * "-" , "AIRLINE" , 30 * "-"
    print "A. Airline List"
    print "B. Airline Reserve"
    print "C. Airline Display Reservation"
    print "D. Exit"
    print 67 * "-"

def print_carmenu():       ## Your menu design here
    print 30 * "-" , "CAR" , 30 * "-"
    print "A. Car List"
    print "B. Car Reserve"
    print "C. Car Display Reservation"
    print "D. Exit"
    print 67 * "-"

loop=True       
 
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = str.upper(raw_input("Enter your choice [A-D]: "))
    
    if choice=='A':     
        print "Hotel Options Selected"
        print_hotelmenu()
        # open a gRPC channel
        channel0 = grpc.insecure_channel('localhost:50051')
        # create a stub (client)
        stub = hotel_app_pb2_grpc.HotelApplicationStub(channel0)
        subchoice = str.upper(raw_input("Enter your choice [A-D]: "))
        if subchoice=='A':
            response = stub.HotelList(hotel_app_pb2.Selection(value=subchoice))
        elif subchoice=='B':
            response = stub.HotelReserv(hotel_app_pb2.Selection(value=subchoice))
        elif subchoice=='C':
        	response = stub.HotelDisplay(hotel_app_pb2.Selection(value=subchoice))
        elif subchoice=='D':
            print "Returning to Main Menu"
            break
        else:
            raw_input("Wrong option selection. Enter any key to try again..")
            break
        print(response.message)
    elif choice=='B':
        print "Airline Options Selected"
        print_airlinemenu()
        # open a gRPC channel
        channel1 = grpc.insecure_channel('localhost:50052')
        # create a stub (client)
        stub = airline_app_pb2_grpc.AirlineApplicationStub(channel1)
        subchoice = str.upper(raw_input("Enter your choice [A-D]: "))
        if subchoice=='A':
            response = stub.AirlineList(airline_app_pb2.Selection(value=subchoice))
        elif subchoice=='B':
            response = stub.AirlineReserv(airline_app_pb2.Selection(value=subchoice))
        elif subchoice=='C':
        	response = stub.AirlineDisplay(airline_app_pb2.Selection(value=subchoice))
        elif subchoice=='D':
            print "Returning to Main Menu"
            break
        else:
            raw_input("Wrong option selection. Enter any key to try again..")
            break
        print(response.message)
    elif choice=='C':
        print "Car Options Selected"
        print_carmenu()
        # open a gRPC channel
        channel2 = grpc.insecure_channel('localhost:50053')
        # create a stub (client)
        stub = car_app_pb2_grpc.CarApplicationStub(channel2)
        subchoice = str.upper(raw_input("Enter your choice [A-D]: "))
        if subchoice=='A':
            response = stub.CarList(car_app_pb2.Selection(value=subchoice))
        elif subchoice=='B':
            response = stub.CarReserv(car_app_pb2.Selection(value=subchoice))
        elif subchoice=='C':
        	response = stub.CarDisplay(car_app_pb2.Selection(value=subchoice))
        elif subchoice=='D':
            print "Returning to Main Menu"
            break
        else:
            raw_input("Wrong option selection. Enter any key to try again..")
            break
        print(response.message)
    elif choice=='D':
        print "Exit Selected....Thank you, bye!!"
        loop=False #Exit the Menu
        exit()
    else:
        # Any other input will not included will print and error
        raw_input("Wrong option selection. Enter any key to try again..")

