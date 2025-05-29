def containsNearbyDuplicate(nums, k: int) -> bool:
        map = {}
        for idx, num in enumerate(nums):
            if (num not in map):
                map[num] = idx
            elif (idx - map[num] <= k):
                return True
            else:
                 map[num] = idx
        return False 