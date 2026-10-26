from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data.get(key, [])
        i = bisect_right(arr, (timestamp, chr(0x10FFFF))) - 1
        return arr[i][1] if i >= 0 else ""