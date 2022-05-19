class Solution:
    def is_integer(self, s: str) -> bool:
        if s == '' or s == '+' or s == '-':
            return False
        has_sbl = False
        for idx, char in enumerate(s):
            if char == '+' or char == '-':
                if has_sbl or idx != 0:
                    return False
                has_sbl = True
            elif not char.isdigit():
                return False
        return True

    def is_float(self, s: str) -> bool:
        if s == '' or s == '+' or s == '-':
            return False
        s = s.split('.')
        if len(s) != 2 or s == ['', '']:
            return False
        return (s[0] == '' or s[0] == '+' or s[0] == '-' or self.is_integer(s[0])) \
                and (s[1] == '' or (self.is_integer(s[1]) and s[1][0].isdigit()))

    def isNumber(self, s: str) -> bool:
        s = s.strip().lower()
        if s == '-.':
            return False
        s = s.split('e')
        if len(s) == 1:
            return self.is_integer(s[0]) or self.is_float(s[0])
        elif len(s) == 2:
            return (self.is_integer(s[0]) or self.is_float(s[0])) and self.is_integer(s[1])
        return False
        