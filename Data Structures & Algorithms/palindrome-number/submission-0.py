class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        input = str(x)
        i, j = 0, len(input) - 1

        while i <= j:
            if input[i] != input[j]:
                return False
            i += 1
            j -= 1
        
        return True
