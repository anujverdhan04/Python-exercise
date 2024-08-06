class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = collections.Counter(tasks)
        # Create a max-heap using negative counts since Python has a min-heap by default
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        while max_heap:
            i = 0
            temp = []
            while i <= n:
                time += 1
                if max_heap:
                    count = heapq.heappop(max_heap)
                    if count < -1:
                        temp.append(count + 1)
                if not max_heap and not temp:
                    break
                i += 1
            for item in temp:
                heapq.heappush(max_heap, item)
        
        return time  

            
        