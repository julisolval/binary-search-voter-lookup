costa_rican_residents = ["Montoya Alvarado Juan", "Montoya Benavides Claudia", "Montoya Castillo Carlos", "Montoya Durán Laura", 
                         "Montoya Espinoza Ariel", "Montoya Flores Natalia", "Montoya Guillén Luis", "Montoya Hernández Ana",
                         "Montoya Iglesias Fabricio", "Montoya Jiménez Luz", "Montoya León David", "Montoya Montoya Boris"]

def binary_search(voter_list, target_voter):
    start, end = 0, len(voter_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if  target_voter == voter_list[mid]:
            return mid
        elif target_voter > voter_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None


binary_search_result = binary_search(costa_rican_residents, "Montoya Montoya Boris")
#binary_search_result = binary_search(costa_rican_residents, "Montoya Flores Susan")

if binary_search_result is not None:
    print(f"Voter number: {binary_search_result}")
else:
    print("Voter not found in the list.")


