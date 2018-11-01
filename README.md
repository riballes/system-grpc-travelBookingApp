# system-grpc-travelBookingApp

## INTRO
gRPC is an open source remote procedure call (RPC) system initially developed at Google. It uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts. It generates cross-platform client and server bindings for many languages.

## IMPLEMENTATION
Create the client and server programs for the vacation trip application
<ul>
  <li>The server program will provide functions to add/remove/modify things such as a hotel room, an airline booking and a rental car. In this week's assignment, the server program will only print message(s) when the functions are called. The client program will use RPC to call the server functions and display the results.</li>
  <li>The Server will provide several simple functions such as: 
    <ol type="a">
      <li>Get a list of hotels, airlines, cars</li>
      <li>Reserve a hotel or airline or car by providing the Name(s), start-date, end-date</li>
      <li>Display current reservations</li>
      <li>Cancel a hotel or airline or car reservation and so on...</li>
    </ol>
  </li>
  <li>The Client program will call each of the functions in a sequence. For example, 
    <ol type="a">
      <li>Get list of hotels.</li>
      <li>Reserve a hotel room</li>
      <li>Display list of reservations</li>
      <li>delete a reservation</li>
      <li>Display list of reservations.</li>
    </ol>
  </li>
</ul>

<b>The application of the client and server programs will show:</b>
<ul>
  <li>The client calling the remote procedure</li>
  <li>The remote procedure being called</li>
  <li>The client displaying the remote procedure's return value</li>
  <li>Output of the 'netstat' comand that shows the server listening on the port number</li>
 </ul>


