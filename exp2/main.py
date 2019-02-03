class Process:
    def __init__(self,burstTime):
        self.burstTime = burstTime
        self.waitingTime = 0
        self.turnAroundTime = 0

def evaluate(processes):
    time = 0
    for i in range(len(processes)):
        if i != 0:
            processes[i].waitingTime = time
        processes[i].turnAroundTime = processes[i].waitingTime + processes[i].burstTime
        time = time+processes[i].burstTime

def display(processes):
    print("S.no  BurstTime WaitingTime TurnAroundTime")
    a = 0
    for process in processes:
        a = a + 1
        print("{}\t{}\t{}\t\t{}".format(a,process.burstTime,process.waitingTime,process.turnAroundTime))

def avgWTTT(processes):
    avgwt = 0
    avgtt = 0
    for process in processes:
        avgtt = avgtt + process.turnAroundTime
        avgwt = avgwt + process.waitingTime
    print("Average TurnAroundTime: {}\nAverage Waitime: {}".format(avgtt/len(processes),avgwt/len(processes)))

if __name__ == "__main__":
    print("Enter number of processes: ")
    number = int(input())
    processes = []
    print("Enter burstTime:")
    for i in range(number):
        processes.append(Process(int(input())))
    evaluate(processes)
    display(processes)
    avgWTTT(processes)