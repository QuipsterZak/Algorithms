from itertools import permutations

cities_coords = {
    'A':(0,0),
    'B':(2,4),
    'C':(5,2),
    'D':(7,8),
    'E':(1,6),
}
#using a long dictionary will make the program run forever
cities_coords_forever = {
    'A': (0, 0),
    'B': (2, 4),
    'C': (5, 2),
    'D': (7, 8),
    'E': (1, 6),
    'F': (3, 1),
    'G': (8, 5),
    'H': (6, 3),
    'I': (9, 2),
    'J': (2, 7),
    'K': (4, 5),
    'L': (7, 1),
    'M': (3, 8),
    'N': (1, 2),
    'O': (5, 6),
    'P': (8, 4),
    'Q': (4, 2),
    'R': (6, 7),
    'S': (2, 1),
    'T': (9, 7),
    'U': (5, 9),
    'V': (0, 5),
    'W': (3, 6),
    'X': (7, 4),
    'Y': (1, 4),
    'Z': (4, 7)
}


#Calculate distance based on Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities_coords[city1]
    x2, y2 = cities_coords[city2]
    return ((x1 - x2) **2 + (y1 - y2) ** 2) ** 0.5
    #Example: ((0 - 2) ** 2 + (0 - 4) ** 2) ** 0.5(sqrt) = 4.47 unit of distance

#Find shortest TSP with bruteforce
def tsp_bruteforce(cities): # takes a dictionary as arg
    all_cities = list(cities_coords.keys()) # create a list of the cities
    shortest_tour = None
    shortest_distance = float('inf') # value so large to ensure any tour found to be shorter

    for tour in permutations(all_cities): # loop through all possible permuations
        # for each tour, we calc total distance, tour[i] and tour[i+1] represent 2 consecutive cities
        tour_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        tour_distance += calculate_distance(tour[-1], tour[0])

        if tour_distance < shortest_distance:
            shortest_distance = tour_distance
            shortest_tour = tour

    return shortest_tour, shortest_distance

shortest_tour, shortest_distance = tsp_bruteforce(cities_coords)

print("shortest TSP Tour", shortest_tour)
print("Shortest Distance: ", shortest_distance)
