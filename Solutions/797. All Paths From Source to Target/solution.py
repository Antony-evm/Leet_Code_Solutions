# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = deque(graph[0])
        paths = deque()
        graph[-1] = []
        res = []

        while stack:
            paths.append([stack.popleft()])
            ele = paths.pop()
            t = deque([ele])
            while t:
                ele = t.popleft()
                if graph[ele[-1]]:
                    for new_node in graph[ele[-1]]:
                        t.append(ele + [new_node])
                else:
                    if ele[-1] == len(graph) - 1:
                        res.append([0] + ele)

        return res
