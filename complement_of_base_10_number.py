class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # gross brute force
        s = ""
        n = bin(n)
        for i in range(2, len(n)):
            if n[i] == '0':
                s += '1'
            else:
                s += '0'
        return int(s, 2)

if __name__ == "__main__":
    s = Solution()
    print(bin(5))
    print(bin(s.bitwiseComplement(5)))