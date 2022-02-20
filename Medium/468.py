class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        """
        时间复杂度: O(1), 因为无论是 ipv4 还是 ipv6, 它的最大长度都是固定的, 即使我们使用了嵌套循环搜索也不影响
        空间复杂度: O(1), 没有任何额外申请的空间
        """
        def is_ipv4(ip: str) -> bool:
            ip = ip.split('.')
            # must be four parts
            if len(ip) != 4:
                return False
            for part in ip:
                # 0 <= xi <= 255
                if not part.isdigit() or int(part) < 0 or int(part) > 255:
                    return False
                # no leading zeros
                elif len(part) > 1 and part[0] == '0':
                    return False
            return True
        
        def is_ipv6(ip: str) -> bool:
            ip = ip.split(':')
            # must be 8 parts
            if len(ip) != 8:
                return False
            for part in ip:
                # 1 <= len(xi) <= 4
                if len(part) < 1 or len(part) > 4:
                    return False
                try:
                    # must be a hex string
                    int_num = int(part, 16)
                except:
                    return False
            return True

        if is_ipv4(queryIP):
            return 'IPv4'
        elif is_ipv6(queryIP):
            return 'IPv6'
        else:
            return 'Neither'