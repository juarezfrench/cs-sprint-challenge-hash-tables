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
    cache = {}  # set up cache
    route = [None] * length #create route array

    for x in tickets:
        if x.source == "NONE":              #look for first ticket
            route[0] = x.destination        # Put of first destination in [0] 
        cache[x.source] = x.destination     # Put in cache

    for y in range(1, length):              # Loop over the length of array
        route[y] = cache[route[y - 1]]      # Look for source of ticket on itinerary to be previous destination

    return route   

  