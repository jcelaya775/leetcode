class Solution:
    # o(n + m) time
    # O(1) space
    def numberOfBeams(self, bank: list[str]) -> int:
        prev, count, res = None, 0, 0

        for cells in bank:
            for cell in cells:
                if cell == '1':
                    count += 1

            if not prev:
                prev = count
                count = 0
            if count == 0:
                continue
            else:
                res += prev * count
                prev = count
                count = 0

        return res