# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        island = deque()
        islands = []
        areas = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                area = 0

                if [i,j] in areas:
                    continue
                else:
                    areas.append([i,j])

                if grid[i][j]==1:
                    island.append([i,j])
                    while island:
                        temp_grid = island[0]
                        area+=1
                        island.popleft()
                        if temp_grid[0]-1>-1 and [temp_grid[0]-1,temp_grid[1]] not in areas:
                            if grid[temp_grid[0]-1][temp_grid[1]]==1:
                                island.append([temp_grid[0]-1,temp_grid[1]])
                            areas.append([temp_grid[0]-1,temp_grid[1]])

                        if temp_grid[0]+1<len(grid) and [temp_grid[0]+1,temp_grid[1]] not in areas:
                            if grid[temp_grid[0]+1][temp_grid[1]]==1:
                                island.append([temp_grid[0]+1,temp_grid[1]])
                            areas.append([temp_grid[0]+1,temp_grid[1]])
                        if temp_grid[1]-1>-1  and [temp_grid[0],temp_grid[1]-1] not in areas:
                            if grid[temp_grid[0]][temp_grid[1]-1]==1:
                                island.append([temp_grid[0],temp_grid[1]-1])
                            areas.append([temp_grid[0],temp_grid[1]-1])
                        if temp_grid[1]+1<len(grid[i]) and [temp_grid[0],temp_grid[1]+1] not in areas:
                            if grid[temp_grid[0]][temp_grid[1]+1]==1:
                                island.append([temp_grid[0],temp_grid[1]+1])
                            areas.append([temp_grid[0],temp_grid[1]+1])
                    islands.append(area)
                    

        islands.sort()
        return islands[-1] if len(islands)>0 else 0



