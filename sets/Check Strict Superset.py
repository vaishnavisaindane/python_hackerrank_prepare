a = set(map(int, input().split()))  # Read the main set 'a'
n = int(input())  # Number of other sets to compare

is_superset = True  # Assume 'a' is a superset initially

for i in range(n):
    set1 = set(map(int, input().split()))  # Read each set to compare with 'a'
    if not a.issuperset(set1):  # Check if 'a' is NOT a superset of 'set1'
        is_superset = False  # If 'a' is not a superset of any set, set to False
        break  # No need to check further if one comparison fails

print(is_superset)  # Print the final result
