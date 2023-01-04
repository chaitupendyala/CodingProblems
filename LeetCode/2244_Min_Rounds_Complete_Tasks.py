'''
Intution to solve the problem is:
1. First we check the frequencies of all the tasks present
2. Now we need to do the following:
    i. If any of them has a frequency of 1 then the tasks can never be complated. So return -1
    ii. If frequency of any task is multiple of 3 when 2 is subtracted from it then we can do it in
            (frequency-2) // 3 + 1 #Since this is greedy approach, we first do as many as possible with 3 at once (frequency -2)
            and then only two tasks are left which can be done together therefore the + 1
    iii. If frequency of any task is multiple of 3 when 4 is subtracted from it then we can remove and do the other 4 in 2 - 2 task cycles
         It can never happen that the left over tasks will be more than 4 because if there are 5 they can be done as (3+2), 6(3+3)
    iv. Number of tasks are divisible by 3 so we do all of then that way, so frequency // 3
    v. Number of tasks are only divisible by 4 so we do all of them only 2 at a time
'''
from collections import Counter
class Solution:
    def minimumRounds(self, tasks) -> int:
        frequency = Counter(tasks)
        result = 0
        for freq in frequency.values():
            if freq == -1:
                return -1
            elif (freq-2) % 3 == 0:
                result += (freq-2)//3 + 1
            elif (freq-4) % 3 == 0:
                result += (freq-4)//3 + 2
            elif freq % 3 == 0:
                result += freq // 3
            else:
                result += freq // 2
        return result