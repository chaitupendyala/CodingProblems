class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        def flood_fill(image, sr, sc, fromColor, toColor):
            if (sr,sc) in visited:
                return
            if sr == len(image) or sc == len(image[1]) or sr < 0 or sc < 0:
                return
            visited.add((sr,sc))
            if image[sr][sc] == fromColor:
                image[sr][sc] = toColor
                flood_fill(image, sr+1, sc, fromColor, toColor)
                flood_fill(image, sr, sc+1, fromColor, toColor)
                flood_fill(image, sr-1, sc, fromColor, toColor)
                flood_fill(image, sr, sc-1, fromColor, toColor)
        if color == image[sr][sc]:
            return image
        flood_fill(image, sr, sc, image[sr][sc], color)
        return image