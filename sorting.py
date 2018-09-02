def insertion_sort(unsorted_list: list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]
        print('insert value:', insert_value)

        count = 0
        while search_index > 0 and unsorted_list[search_index - 1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index - 1]
            search_index -= 1
            count += 1
        
        print('[while loop] {} iterations'.format(count))
        unsorted_list[search_index] = insert_value
        print('[Iteration #{}]: {}\n'.format(index + 1, unsorted_list))
   
    return unsorted_list


def partition(unsorted_array, first_index, last_index):
    pivot = unsorted_array[first_index]  # value of the pivot
    pivot_index = first_index
    index_of_last_element = last_index

    less_than_pivot_index = index_of_last_element  # where we begin the search for the element < pivot
    greater_than_pivot_index = first_index + 1  

    while True:
        while unsorted_array[greater_than_pivot_index] < pivot \
            and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1

        while unsorted_array[less_than_pivot_index] < pivot \
            and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1

        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break

        

my_list = [5, 1, 100, 2, 10]
insertion_sort(my_list)

array = [43, 3, 20, 89, 4, 77]