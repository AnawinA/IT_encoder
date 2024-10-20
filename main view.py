"""main view"""
import webview
from bs4 import BeautifulSoup
import time

def main():
    """pywebview"""
    window = webview.create_window('Load HTML Example', "./index.html")
    webview.start()

if __name__ == '__main__':
    main()
