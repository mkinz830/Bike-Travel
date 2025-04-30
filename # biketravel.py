# Check if it is possible to travel on a bike for a trip of 1000km. Consider following inputs in order
# N - Maximum fuel capacity
# M - Mileage of the bike (in KM)
# D - Distance between each fuel station (in KM)
# Find the minimum number of refueling required(including the initial fueling) to reach the destination.
# If the rider can reach the destination, print 'Yes' along with number of refuels required. If not 
# respond 'No'.
# Input format: Input string will contain comma separated values for maximum fuel capacity. Mileage of the
# bike and distance between each fuel station in same order.
# Output format: A space separated string in case of success, i.e. "Yes" along with number of refuels or "No".
# (Output is case-sensitive)

def check_trip(fuel_capacity, mileage, fuel_stations):
    total_distance_per_tank = fuel_capacity * mileage
    if total_distance_per_tank >= 1000:
        return 'Yes 1'
    elif total_distance_per_tank >= fuel_stations:
        return 'Yes ' + str(1000//total_distance_per_tank+1)
    else:
        return 'No'

print(check_trip(13,28,400))