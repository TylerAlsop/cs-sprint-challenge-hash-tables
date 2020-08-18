#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    route = {}
    head = None

    for ticket_item in tickets:
        if tickets[ticket_item[0]] == "NONE":
            head = tickets[ticket_item]

    print(head)
    current_ticket = head


    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]


expected = ["PDX", "DCA", "NONE"]
reconstruct_trip(tickets, 3)
