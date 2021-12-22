class Solution:
    def numberToWords(self, num: int) -> str:
        low = [
            '', 'One', 'Two', 'Three', 'Four',
            'Five', 'Six', 'Seven', 'Eight', 'Nine'
        ]
        mid = [
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
            'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
        high = [
            '', '', 'Twenty', 'Thirty', 'Forty',
            'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]

        def build_number(num):
            a = num % 10    # 个位
            num = num // 10
            b = num % 10    # 十位
            num = num // 10
            c = num         # 百位
            res = ''
            if c != 0:
                res += low[c] + " Hundred "
            if b == 1:
                res += mid[a]
            elif b == 0:
                res += low[a]
            else:
                res += high[b] + ' ' + low[a]
            return res.strip() + " "

        if num == 0:
            return "Zero"

        part1 = num % 1000  # 个位
        num = num // 1000
        part2 = num % 1000  # 十位
        num = num // 1000
        part3 = num % 1000  # 百位
        num = num // 1000
        part4 = num         # 千位

        res = ''
        if part4 != 0:
            res += build_number(part4) + 'Billion '
        if part3 != 0:
            res += build_number(part3) + 'Million '
        if part2 != 0:
            res += build_number(part2) + 'Thousand '
        if part1 != 0:
            res += build_number(part1)
        return res.strip()
