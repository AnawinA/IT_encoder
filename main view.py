"""main view"""
import webview
from bs4 import BeautifulSoup


def main():
    """pywebview"""
    f = open('my web.html')
    fsimp = BeautifulSoup(f.read(), "html.parser").prettify()
    f.close()

    window = webview.create_window('Load HTML Example', html=fsimp)
    webview.start()

if __name__ == '__main__':
    main
