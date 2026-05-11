class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        s = ""

        # Use a pointer i to traverse the array
        i = 0
        while i < n:
            # Append the character to s
            s += chars[i]

            # Find the extent of the consecutive identical character using the second pointer j
            j = i + 1
            while j < n and chars[i] == chars[j]:
                j += 1

            # If the count j - i is greater than 1, append the count as a string to s
            if j - i > 1:
                s += str(j - i)
            # Shift i to j
            i = j
        
        # Copy the compressed string s back to the chars array and return its length
        i = 0
        while i < len(s):
            chars[i] = s[i]
            i += 1
        return i