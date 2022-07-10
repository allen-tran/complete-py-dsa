import collections
from typing import List


def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    res = []
    indegrees = {i: 0 for i in range(numCourses)}
    graph = {i: [] for i in range(numCourses)}
    for pre, crs in prerequisites:
        graph[pre].append(crs)
        indegrees[crs] += 1

    sources = collections.deque()
    for key in indegrees:
        if indegrees[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        res.append(vertex)
        for child in graph[vertex]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                sources.append(child)

    if len(res) != numCourses:
        return False
    return True
