class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        od = ""
        while dominoes != od:
            od = dominoes
            dominoes = dominoes.replace("R.L", "T")
            dominoes = dominoes.replace(".L", "LL")
            dominoes = dominoes.replace("R.", "RR")
            dominoes = dominoes.replace("T", "R.L")
        return dominoes