# Train Ticket Booking System

This project is a simple train ticket booking system with gRPC APIs. The system allows users to purchase tickets, view receipt details, view users and their allocated seats in specific sections, remove users from the train, and modify a user's seat.


Prerequisites  
* Python  
* gRPC 


```
pip3 install grpcio
pip3 install grpcio-tools
```

To create protobuf files, run the following command after moving into cloned directory:
```
python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/ticket.proto
```

To run the following program:

Open 2 shells:  
One one shell run  
```
python3 train_server.py
```

after the server starts running, on another shell run
```
python3 train_client.py
```

Now select the options for the APIs you want to test out and execute them.