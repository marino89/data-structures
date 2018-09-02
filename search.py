from typing import Optional


def binary_search(ordered_list: list, term: int) -> int:
    index_of_first_element = 0
    index_of_last_element = len(ordered_list) - 1

    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element) // 2
        mid_point_term = ordered_list[mid_point]
        if mid_point_term == term:
            return mid_point

        if term > mid_point_term:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1

    return None


def nearest_mid(input_list: list, lower_bound_index: int, upper_bound_index: int, 
                search_value: int) -> Optional[int]:
    num = upper_bound_index - lower_bound_index
    den = input_list[upper_bound_index] - input_list[lower_bound_index]
    return lower_bound_index + (num / den) * (search_value - input_list[lower_bound_index])
