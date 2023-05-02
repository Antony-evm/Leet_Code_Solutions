# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = {}
        stack = deque()
        for i in range(len(isConnected)):
            if not visited.get(i):
                visited[i] = True
                stack.append(i)
                while stack:
                    curr = stack.popleft()
                    connections = [
                        idx
                        for idx, val in enumerate(isConnected[curr])
                        if val == 1 and visited.get(idx, False) == False
                    ]
                    for conn in connections:
                        stack.append(conn)
                        visited[conn] = True
                provinces += 1
        return provinces
