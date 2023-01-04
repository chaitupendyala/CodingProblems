class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        OPT = [None] * len(tasks)
        def minRounds(tasks, index):
            if index == len(tasks):
                return 0
            elif index > len(tasks) or index == len(tasks) - 1 or tasks[index] != tasks[index+1]:
                return -1
            elif OPT[index] != None:
                return OPT[index]
            elif index + 2 <= len(tasks) - 1 and tasks[index] == tasks[index+1] != tasks[index+2]:
                count = minRounds(tasks, index+2)
                if count == -1:
                    return -1
                OPT[index] = 1 + count
                return 1 + count
            elif index + 3 <= len(tasks) - 1 and tasks[index] == tasks[index+1] == tasks[index+2] and tasks[index] != tasks[index+3]:
                count = minRounds(tasks, index+3)
                if count == -1:
                    return -1
                OPT[index] = 1 + count
                return 1 + count
            else:
                count1 = minRounds(tasks, index+2)
                count2 = minRounds(tasks, index+3)
                if count1 == -1 and count2 != -1:
                    OPT[index] = 1 + count2
                    return 1 + count2
                elif count2 == -1 and count1 != -1:
                    OPT[index] = 1 + count1
                    return 1 + count1
                elif count1 == -1 and count2 == -1:
                    OPT[index] = -1
                    return -1
                else:
                    OPT[index] = 1 + min(count1, count2)
                    return 1 + min(count1, count2)
            
        tasks.sort()
        return minRounds(tasks, 0)