class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for nei in graph[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return completed == numCourses