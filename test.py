import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from bs4 import BeautifulSoup


class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()


url = 'https://wanwang.aliyun.com/domain/searchresult/?keyword=zhongzi&suffix=.me'
r = Render(url)
html = r.frame.toHtml()
bsj = BeautifulSoup(html,'lxml')
info = bsj.find_all("li",{"data-domain":"zhongzi.me"})[0]
com = info.find("a",{"action":"addCart"})
if com:
    print("可以注册")
else:
    print("已被注册")



