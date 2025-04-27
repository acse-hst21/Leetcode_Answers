class Solution:
    def flip(self, image: List[List[int]]) -> List[List[int]]:
        new_image = []
        for row in image:
            new_image.append(row[::-1])
        return new_image
    def invert(self, image: List[List[int]]) -> List[List[int]]:
        new_image = []
        for row in image:
            new_image.append([1 - num for num in row])
        return new_image
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = self.flip(image)
        inverted = self.invert(flipped)
        return inverted
