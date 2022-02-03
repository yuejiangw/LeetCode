class UndergroundSystem:

    def __init__(self):
        self.start_station = dict()
        self.table = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start_station[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time = self.start_station[id][1]
        # start station, end statino
        path = (self.start_station[id][0], stationName)
        record = self.table.get(path, (0, 0))
        self.table[path] = (record[0] + t - start_time,
                            record[1] + 1)  # total time, total amount

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        idx = (startStation, endStation)
        time, amount = self.table[idx]
        return time / amount


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
