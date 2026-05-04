class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Left pointer on the current item

        # Check elements to the right and get the max

        # Change the item at the current marker to the max

        # Move the cursor to the right and repeat

        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans

                

