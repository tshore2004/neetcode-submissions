class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        left = 0
        right = len(self.timeMap[key])

        while left < right:
            mid = (left + right) // 2
            if self.timeMap[key][mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid
        if right == 0:
            return ""
        elif right > 0:
            return self.timeMap[key][right-1][0]
        # return self.timeMap[right]
