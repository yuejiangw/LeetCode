class Solution:
    def partitionLabels(self, S: str):
        if not S or len(S) == 0:
            return None
        # N = len(S)
        result = []
        for i in range(len(S)):
            