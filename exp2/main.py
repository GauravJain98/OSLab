data_set = [{
    'bt':32,
    'at':0
},{
    'bt':2,
    'at':0
},{
    'bt':12,
    'at':0
},{
    'bt':31,
    'at':1
},{
    'bt':1,
    'at':1
},{
    'bt':11,
    'at':1
}]

class Process:

    def __init__(self,burstTime,arrivalTime):
        self.burstTime = burstTime
        self.waitingTime = 0
        self.turnAroundTime = 0
        self.arrivalTime = arrivalTime

    def __cmp__(self,other):
        return cmp(self.burstTime,other.burstTime)

    def __lt__(self, other):
        return self.burstTime < self.burstTime

def display(processes):
    print("S.no ArrivalTime BurstTime WaitingTime TurnAroundTime")
    a = 0
    for process in processes:
        a = a + 1
        print("{}\t{}\t{}\t{}\t\t{}".format(a,process.arrivalTime,process.burstTime,process.waitingTime,process.turnAroundTime))

def avgWTTT(processes):
    avgwt = 0
    avgtt = 0
    for process in processes:
        avgtt = avgtt + process.turnAroundTime
        avgwt = avgwt + process.waitingTime
    print("Average TurnAroundTime: {}\nAverage Waitime: {}".format(avgtt/len(processes),avgwt/len(processes)))

if __name__ == "__main__":
    processes = []
    sortedProcess = []
    finalprocess = []
    waitTime = 0
    for data in data_set:
        processes.append(Process(data['bt'],data['at']))
    processes.sort(key= lambda x:x.arrivalTime)
    for i in range(110):
        processe = list(filter(lambda x: x if x.arrivalTime == i else None,processes))
        if len(processe) > 0:
            for proc in  processe:
                sortedProcess.append(proc)
            sortedProcess.sort(key= lambda x:x.burstTime)
        if len(sortedProcess) > 0:
            if waitTime == 0:
                process = sortedProcess[0]
                sortedProcess = sortedProcess[1:]
                waitTime = process.burstTime
                process.waitTime = i
                process.turnAroundTime = process.burstTime + i
                print("{} {} {}".format(process.burstTime,process.waitTime-process.arrivalTime,process.arrivalTime))
            if waitTime > 0:
                waitTime = waitTime - 1

    display(sortedProcess)
 