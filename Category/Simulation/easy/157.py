"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)

        题目难点：
        1. read4 每次固定读 4 个字符，但可能已经读完了所有字符，因此要判断其返回值
        2. 可能在将 buf4 中的字符复制到 buf 的过程中就已经达到了返回条件，需要加以判断
        """
        buf4 = [""] * 4
        res = 0
        while res < n:
            x = read4(buf4)
            if x == 0:
                break
            for i in range(x):
                buf[res] = buf4[i]
                res += 1
                if res >= n:
                    break
        return res
