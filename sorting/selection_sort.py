class SelectionSort:
    def __init__(self, arr):
        self.arr = self.selection_sort(arr)
    def swap(self, index1, index2, arr):
        arr[index1], arr[index2] = arr[index2], arr[index1]
    def selection_sort(self, arr):
        length = len(arr)
        for curr_index in range(length - 1):
            smallest_element_index = curr_index
            for index in range(curr_index + 1, length):
                if arr[index] < arr[smallest_element_index]:
                    smallest_element_index = index
            self.swap(smallest_element_index, curr_index,arr)
        return arr
    


arr = [32, 2,300,  4, 9, 3, 5, 1]

selection_sort = SelectionSort(arr)

print(selection_sort.arr)