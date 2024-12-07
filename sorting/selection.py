'''
Steps for Selection Sort:

Example array: arr = [32, 2, 4, 9, 3, 5, 1]

1. Start with the first element, `i = 0` (value = 32). Search for the minimum element in the unsorted portion of the array, which starts from `i + 1`.  
   - Compare values at indices `1, 2, 3, 4, 5, 6`.  
   - The smallest value is at index `6` (value = 1).  
   - Swap the values at indices `0` and `6`.  
   Result: arr = [1, 2, 4, 9, 3, 5, 32].

2. Move to the next element, `i = 1` (value = 2). Search for the minimum value in the remaining unsorted portion (`i + 1` onward).  
   - Compare values at indices `2, 3, 4, 5, 6`.  
   - The smallest value is already at `i = 1`. No swap is needed.  
   Result: arr = [1, 2, 4, 9, 3, 5, 32].

3. Proceed to `i = 2` (value = 4). Search for the minimum value in the unsorted portion.  
   - Compare values at indices `3, 4, 5, 6`.  
   - The smallest value is at index `4` (value = 3).  
   - Swap the values at indices `2` and `4`.  
   Result: arr = [1, 2, 3, 9, 4, 5, 32].

4. Next, `i = 3` (value = 9). Search for the minimum in the remaining elements.  
   - Compare values at indices `4, 5, 6`.  
   - The smallest value is at index `4` (value = 4).  
   - Swap the values at indices `3` and `4`.  
   Result: arr = [1, 2, 3, 4, 9, 5, 32].

5. For `i = 4` (value = 9), search for the minimum in the remaining elements.  
   - Compare values at indices `5, 6`.  
   - The smallest value is at index `5` (value = 5).  
   - Swap the values at indices `4` and `5`.  
   Result: arr = [1, 2, 3, 4, 5, 9, 32].

6. Finally, `i = 5` (value = 9). Search for the minimum in the remaining element at `i = 6`.  
   - The value at index `6` (value = 32) is larger than the current value. No swap is needed.  
   Result: arr = [1, 2, 3, 4, 5, 9, 32].

After completing the steps, the array is fully sorted.



'''

def swap(index1, index2, arr):
    arr[index1], arr[index2] = arr[index2], arr[index1]
def selection_sort(arr):
    length = len(arr)
    for curr_index in range(length - 1):
        smallest_element_index = curr_index
        for index in range(curr_index + 1, length):
            if arr[index] < arr[smallest_element_index]:
                smallest_element_index = index
        swap(smallest_element_index, curr_index,arr)
    return arr


if __name__=='__main__':
    arr = [32, 2, 4, 9, 3, 5, 1]
    print("'arr' Before Selection Sort Applied : ", arr)
    selection_sort(arr)
    print("'arr' After Selection Sort Applied : ", arr)

 
            
        
    









