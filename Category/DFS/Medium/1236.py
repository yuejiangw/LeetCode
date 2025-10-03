# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = []
        visited = set()
        parts = startUrl.split('/')
        src = f'http://{parts[2]}'
        
        def dfs(start):
            nonlocal src
            if start in visited:
                return
            res.append(start)
            visited.add(start)
            urls = htmlParser.getUrls(start)
            if not urls or len(urls) == 0:
                return
            for url in urls:
                if url.startswith(src):
                    dfs(url)
        
        dfs(startUrl)
        return res
        