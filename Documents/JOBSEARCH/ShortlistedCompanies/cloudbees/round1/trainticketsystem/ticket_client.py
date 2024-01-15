import ticket_pb2_grpc
import ticket_pb2
import time
import grpc

def get_receipt_details(stub, receipt_id):
    print("\n\nFetching Receipt Details")
    details_request = ticket_pb2.ReceiptDetailsRequest(receipt_id=receipt_id)
    receipt_details = stub.GetReceiptDetails(details_request)
    print("Receipt Details Response:")
    print(receipt_details)

def get_ticket_details():
    from_location = input("Enter From Location: ")
    to_location = input("Enter To Location: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email Address: ")
    price_paid = float(input("Enter Price Paid (Please enter only numerical values): "))

    user = ticket_pb2.User(first_name=first_name, last_name=last_name, email=email)
    receipt_request = ticket_pb2.TicketRequest(fromTRQ=from_location, to=to_location, user=user, price_paid=price_paid)

    return receipt_request

def purchase_ticket(stub):
    print("\n\nPurchasing ticket")
    ticket_request = get_ticket_details()
    ticket_receipt = stub.PurchaseTicket(ticket_request)
    print("Purchase Ticket Response:")
    print(ticket_receipt)

def view_users_by_section(stub, section):
    print("\n\nView Users by Section:")
    section_request = ticket_pb2.SectionRequest(section=section)
    users_by_section = stub.ViewUsersBySection(section_request)
    print(f"Users in Section {section.upper()} Response:")
    for user_seat in users_by_section.user_seat:
        print(f"User: {user_seat.user_id}, Seat: {user_seat.seat}")

def remove_user(stub, email):
    print("\n\nRemove users by Email:")
    remove_request = ticket_pb2.RemoveUserRequest(email=email)
    remove_response = stub.RemoveUser(remove_request)
    print(f"Remove User Response: Success={remove_response.success}")

def modify_user_seat(stub, email, new_seat):
    print("\n\nModify Users by Email:")
    modify_request = ticket_pb2.ModifySeatRequest(email=email, new_seat=new_seat)
    modify_response = stub.ModifyUserSeat(modify_request)
    print(f"Modify User Seat Response: Success={modify_response.success}")

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ticket_pb2_grpc.TrainServiceStub(channel)
        print("1. Purchase Ticket")
        print("2. Get Receipt Details")
        print("3. View Users By Section")
        print("4. Remove User from Train")
        print("5. Modify User's Seat")
        api_call = input("Which API would you like to call: ")

        if api_call == "1":
            purchase_ticket(stub)
        elif api_call == "2":
            receipt_id = input("Enter Receipt ID: ")
            get_receipt_details(stub, receipt_id)
        elif api_call == "3":
            section = input("Enter Section (A or B): ")
            view_users_by_section(stub, section)
        elif api_call == "4":
            email = input("Enter email to Remove: ")
            remove_user(stub, email)
        elif api_call == "5":
            email = input("Enter email of user whose seat to Modify: ")
            new_seat = input("Enter New Seat: ")
            modify_user_seat(stub, email, new_seat)

if __name__ == "__main__":
    run()