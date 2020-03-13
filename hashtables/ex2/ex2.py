#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length
    ticketList=[]
    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)
    ticketList.append(hash_table_retrieve(ht, "NONE"))
    ticketList.append(hash_table_retrieve(ht, hash_table_retrieve(ht, "NONE")))
    lastDest = ticketList[1]
    while len(ticketList) < length - 1:
        nextDest = hash_table_retrieve(ht, lastDest)
        ticketList.append(nextDest)
        lastDest = nextDest
 
    return ticketList