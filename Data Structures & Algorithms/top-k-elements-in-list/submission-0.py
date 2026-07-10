class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count_dict = {}
            for num in nums:
                if num in count_dict:
                    count_dict[num] += 1
                else:
                    count_dict[num] = 1
            sorted_dict = sorted(count_dict, key = count_dict.get)
            return sorted_dict[-k:]

        