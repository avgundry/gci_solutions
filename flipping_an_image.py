from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Hm. Well...can you directly convert a binary array to binary?
        n = len(image[0])
        for row in image:
            for i in range(n // 2):
                print(f"flipping and inverting indices {i}, {n - i - 1}")
                row[i], row[n - i - 1] = int(not row[n - i - 1]), int(not row[i])
            if n % 2 == 1:
                row[n // 2 ] = int(not row[n // 2])

        return image



if __name__ == "__main__":
    s = Solution()
    print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))