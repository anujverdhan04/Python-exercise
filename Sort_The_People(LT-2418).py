class Solution(object):
    def sortPeople(self, names, heights):
        n = len(names)
        if len(names) != len(heights):
            return "Lengths of names and heights are not the same"
        heights_sorted = sorted(heights, reverse=True)  
        sorted_names = [""] * n
        for i in range(n):
            height_index = heights.index(heights_sorted[i])  
            sorted_names[i] = names[height_index] 
        return sorted_names       
        