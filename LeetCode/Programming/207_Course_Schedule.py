'''
207. Course Schedule
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where 
prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''
class Solution:
    '''
    We need to use the concept of Topological Sort here.
    '''
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            degree[prerequisite[0]] += 1
        
        nodes_with_zero_degree = [i for i in range(numCourses) if degree[i] == 0]

        for node in nodes_with_zero_degree:
            for adjacent in graph[node]:
                degree[adjacent] -= 1
                if degree[adjacent] == 0:
                    nodes_with_zero_degree.append(adjacent)
        
        return len(nodes_with_zero_degree) == numCourses

            

print("numCourses = 2, prerequisites = [[1,0]]:", Solution().canFinish(numCourses = 2, prerequisites = [[1,0]]))
print("numCourses = 2, prerequisites = [[1,0],[0,1]]:", Solution().canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
print("numCourses = 3, prerequisites = [[1,0],[0,2],[2,1]]:", Solution().canFinish(numCourses = 3, prerequisites = [[1,0],[0,2],[2,1]]))