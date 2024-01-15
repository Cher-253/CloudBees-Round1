from concurrent import futures
import time
import grpc
import ticket_pb2
import ticket_pb2_grpc

class TrainServicer(ticket_pb2_grpc.TrainServiceServicer):
    def __init__(self):
        self.receipts = {}
        self.section_a = {}
        self.section_b = {}
        self.next_receipt_id = 1

    def PurchaseTicket(self, request, context):
        receipt_id = str(self.next_receipt_id)
        self.next_receipt_id += 1

        ticket_receipt = ticket_pb2.TicketReceipt(
            receipt_id=receipt_id,
            to=request.to,
            user=request.user,
            price_paid=20.0,
        )

        # Assign a seat based on section
        if len(self.section_a) <= len(self.section_b):
            ticket_receipt.seat = f"A{len(self.section_a) + 1}"
            self.section_a[request.user.email] = ticket_receipt.seat
        else:
            ticket_receipt.seat = f"B{len(self.section_b) + 1}"
            self.section_b[request.user.email] = ticket_receipt.seat

        self.receipts[receipt_id] = ticket_receipt
        return ticket_receipt

    def GetReceiptDetails(self, request, context):
        receipt_id = request.receipt_id
        return self.receipts.get(receipt_id, ticket_pb2.TicketReceipt())

    def ViewUsersBySection(self, request, context):
        section = request.section
        users_by_section = ticket_pb2.UsersBySectionResponse()

        if section.lower() == 'a':
            users_by_section.user_seat.extend(
                ticket_pb2.UserSeat(user_id=user_id, seat=seat)
                for user_id, seat in self.section_a.items()
            )
        elif section.lower() == 'b':
            users_by_section.user_seat.extend(
                ticket_pb2.UserSeat(user_id=user_id, seat=seat)
                for user_id, seat in self.section_b.items()
            )

        return users_by_section
    
    def RemoveUser(self, request, context):
        email = request.email.lower()
        success = False

        for receipt_id, receipt in list(self.receipts.items()):
            if receipt.user.email.lower() == email:
                success = True
                del self.receipts[receipt_id]
                break

        return ticket_pb2.RemoveUserResponse(success=success)

    
    def ModifyUserSeat(self, request, context):
        email = request.email.lower()
        new_seat = request.new_seat
        success = False

        # Modify seat in section A
        if email in self.section_a:
            old_seat = self.section_a[email]
            self.section_a[email] = new_seat
            success = True
        # Modify seat in section B
        elif email in self.section_b:
            old_seat = self.section_b[email]
            self.section_b[email] = new_seat
            success = True
        else:
            old_seat = None

        # Update seat in receipts
        if success and old_seat:
            for receipt in self.receipts.values():
                if receipt.user.email.lower() == email and receipt.seat == old_seat:
                    receipt.seat = new_seat
        return ticket_pb2.ModifySeatResponse(success=success)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ticket_pb2_grpc.add_TrainServiceServicer_to_server(TrainServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()