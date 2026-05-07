class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strings:
            key = tuple(((ord(s[i + 1]) - ord(s[i])) % 26 for i in range(len(s) - 1)))
            groups[key].append(s)

        return list(groups.values())