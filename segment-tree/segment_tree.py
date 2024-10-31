class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)
        self.tree = [0 for _ in range(4* self.length + 1)]
        self.build_tree(0,0,  self.length - 1)
    
    
    def build_tree(self, curr_index, start, end):
        if start == end:
            self.tree[curr_index] = self.arr[start]
        else:
            middle_index = (start + end) // 2
            #  Move to The Left
            
            self.build_tree((curr_index * 2) + 1, start, middle_index)
            self.build_tree((curr_index*2) + 2, middle_index + 1, end)
            
            self.tree[curr_index] = self.tree[(curr_index * 2) + 2] + self.tree[(curr_index * 2) + 1]
            
    def query(self, left, right):
        return self._query(0, 0, self.length - 1, left, right)   
        
    def _query(self,curr_index,  start, end, left, right):
        #  If The Asked Range Is Not Bounded By Our Left And Right Bounde Of The Tree
        if right < start or left > end:
            #  Return Nutral Value
            return 0
        elif start >= left and right >= end:
            return self.tree[curr_index]
        else:
            middle_index = (start + end) // 2
            #  Check The Left Part
            left_value = self._query((curr_index * 2) + 1,start, middle_index, left, right)
            #  Check The right Part
            right_value = self._query((curr_index*2) + 2, middle_index + 1, end, left, right)
            
            
            return left_value + right_value
        
    def _update(self, curr_index, start, end, index, value):
        if start == end:
            self.tree[curr_index] += value
        else:
            middle_index = (start + end) // 2
            if start <= index <= end:
                self._update( (curr_index * 2) +  1, start, middle_index, index, value)
            else:
                self._update((curr_index* 2) + 2, middle_index + 1, end, index, value )
            
            self.tree[curr_index] = self.tree[(curr_index * 2) + 1] +  self.tree[(curr_index * 2) + 2]
    def update(self, index, value):
        return self._update(0, 0, self.length - 1, index, value)
        
    
    
arr = [1, 2, 3, 4, 5, 6]
seg_tree = SegmentTree(arr)

       
            