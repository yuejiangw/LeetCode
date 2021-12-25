from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(' ')
        third = []
        if len(text) < 3:
            return third
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                third.append(text[i+2])
        return third
