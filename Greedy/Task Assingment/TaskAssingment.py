# O(nlog(n)) time | O(n) space - where n is the number of tasks

def taskAssignment(k, tasks):
    pairedTasks = []

    taskDurationsToIndices = getTaskDurationsToIndices(tasks)
    sortedTasks = sorted(tasks)

    for idx in range(k):

        task1Duration = sortedTasks[idx]

        indicesWithTask1Duration = taskDurationsToIndices[task1Duration]

        task1Index = indicesWithTask1Duration.pop()

        task2SortedIndex = len(tasks) - 1 - idx

        task2Duration = sortedTasks[task2SortedIndex]

        indicesWithTask2Duration = taskDurationsToIndices[task2Duration]

        task2Index = indicesWithTask2Duration.pop()

        pairedTasks.append([task1Index, task2Index])

    return pairedTasks

def getTaskDurationsToIndices(tasks):

    taskDurationsToIndices = {}

    for idx, taskDuration in enumerate(tasks):

        if taskDuration in taskDurationsToIndices:

            taskDurationsToIndices[taskDuration].append(idx)

        else:

            taskDurationsToIndices[taskDuration] = [idx]

    return taskDurationsToIndices

'''
my solution

def taskAssignment(k, tasks):

    # Write your code here.

    res=[]

    sortedtask=[]

    for idx, num in enumerate(tasks):

        sortedtask.append((num,idx))

    sortedtask.sort(key=lambda x:x[0])
    l=0

    r=len(tasks)-1

    while l<r:

        res.append([sortedtask[l][1],sortedtask[r][1]])

        l+=1
        r-=1

    return res
'''