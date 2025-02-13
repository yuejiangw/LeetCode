class Solution:
    def isNumber(self, s: str) -> bool:
        # T: O(n), S: O(1)
        seen_digit = seen_e = seen_dot = False
        
        for idx, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ['e', 'E']:
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            elif c in ['+', '-']:
                if idx > 0 and s[idx - 1] != 'e' and s[idx - 1] != 'E':
                    return False
            elif c == '.':
                if seen_e or seen_dot:
                    return False
                seen_dot = True
            else:
                return False
            
        return seen_digit