class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            max_element = heapq.heappop(gifts)
            heapq.heappush(gifts, math.floor(math.sqrt(max_element * -1)) * -1)
        sum = 0
        for i in gifts:
            sum += (i * -1)
        return sum