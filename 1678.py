# 真是操了，这么简单的题想那么复杂
class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o").replace("(al)", "al")
        return command
