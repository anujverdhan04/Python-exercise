class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        # Get the k most common elements
        most_common = freq.most_common(k)
        
        # Extract just the elements from the most common pairs
        top_k_elements = [element for element, count in most_common]
        
        return top_k_elements
           





       
        