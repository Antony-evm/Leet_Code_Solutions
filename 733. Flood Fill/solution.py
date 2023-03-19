# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque

        colored = deque()
        init_color = image[sr][sc]
        if init_color == color:
            return image
        colored.append((sr,sc))

        while colored:
            i = colored[0]
            image[i[0]][i[1]] = color
            colored.popleft()
            if i[0]-1>-1 and image[i[0]-1][i[1]]==init_color:
                colored.append((i[0]-1,i[1]))
            if i[0]+1<len(image) and image[i[0]+1][i[1]]==init_color:
                colored.append((i[0]+1,i[1]))
            if i[1]-1>-1 and image[i[0]][i[1]-1]==init_color:
                colored.append((i[0],i[1]-1))
            if i[1]+1<len(image[i[0]]) and image[i[0]][i[1]+1]==init_color:
                colored.append((i[0],i[1]+1))
        return image