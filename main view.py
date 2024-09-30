"""main view"""
import webview
from bs4 import BeautifulSoup
import time

def load_website(window: webview.Window):
    """load website"""
    pass

def main():
    """pywebview"""
    window = webview.create_window('Load HTML Example', "./it-encode-web.html")
    webview.start(load_website, window)

if __name__ == '__main__':
    main()
