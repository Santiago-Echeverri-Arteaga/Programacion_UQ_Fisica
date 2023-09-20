def weeks_elapsed(day1, day2):
    """ (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    2
    """
    # Calculate the absolute difference between the two days
    day_difference = abs(day1 - day2)
    
    # Calculate the number of full weeks by dividing the day difference by 7
    full_weeks = day_difference // 7
    
    return full_weeks
#########################################
#########################################
#########################################
# alkaline_earth_metals = [
#     [4, 9.012],
#     [12, 24.305],
#     [20, 40.078],
#     [38, 87.62],
#     [56, 137.327],
#     [88, 226]
# ]
# for element in alkaline_earth_metals:
#     atomic_number, atomic_weight = element
#     print(f"Atomic Number: {atomic_number}, Atomic Weight: {atomic_weight}")
# number_and_weight = []

# for element in alkaline_earth_metals:
#     number_and_weight.extend(element)

# print(number_and_weight)
#########################################
#########################################
#########################################
rat_1_weight = 100  # Initial weight of rat 1
rat_1_rate = 0.04  # Rate of weight increase for rat 1 (4% per week)
target_increase = 0.25  # Target weight increase (25%)

weeks = 0  # Initialize the weeks counter

while rat_1_weight < (1 + target_increase) * 100:
    rat_1_weight += rat_1_weight * rat_1_rate  # Increase weight of rat 1
    weeks += 1

print(f"It will take {weeks} weeks for rat 1 to be 25% heavier.")

#####
initial_weight = 100  # Initial weight for both rats
rat_1_rate = 0.06  # Rate of weight increase for rat 1 (6% per week)
rat_2_rate = 0.04  # Rate of weight increase for rat 2 (4% per week)
target_increase = 0.10  # Target weight increase (10%)

rat_1_weight = initial_weight
rat_2_weight = initial_weight
weeks = 0  # Initialize the weeks counter

while rat_1_weight < (1 + target_increase) * rat_2_weight:
    rat_1_weight += rat_1_weight * rat_1_rate  # Increase weight of rat 1
    rat_2_weight += rat_2_weight * rat_2_rate  # Increase weight of rat 2
    weeks += 1

print(f"It will take {weeks} weeks for rat 1 to be 10% heavier than rat 2.")
# ###############

