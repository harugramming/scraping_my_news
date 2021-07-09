from flask import Flask,render_template,request

# 各種インポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す
app = Flask(__name__)

DRIVER_PATH = 'chromedriver'
# DRIVER_PATH = '/Users/Kenta/Desktop/Selenium/chromedriver' # ローカル
# DRIVER_PATH = '/app/.chromedriver/bin/chromedriver'        # heroku


# title、URLを格納する配列を定義
titles = []
urls = []

# ブラウザの起動
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

##-------------- GIGAZIN satrt ---------------------##
# GIGAZINにアクセスする
url = 'https://gigazine.net/'
driver.get(url)

# ソースコードを取得
html = driver.page_source

# HTMLをパースする
soup = BeautifulSoup(html, 'html.parser') # または、'html.parser'

# CSSセレクタ
selector = '.content > section:nth-child(1) > .card > h2 > a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append(soup.select_one(selector).get('href'))

# CSSセレクタ
selector = '.content > section:nth-child(2) > .card > h2 > a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append(soup.select_one(selector).get('href'))

# CSSセレクタ
selector = '.content > section:nth-child(3) > .card > h2 > a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append(soup.select_one(selector).get('href'))


##-------------- GIGAZIN end ---------------------##
##-------------- ITmedia start ---------------------##
# ITmediaにアクセスする
url = 'https://www.itmedia.co.jp/'
driver.get(url)

# ソースコードを取得
html = driver.page_source

# HTMLをパースする
soup = BeautifulSoup(html, 'html.parser') # または、'html.parser'

# CSSセレクタ
selector = '.colBoxInner > .colBoxTab1 > .colBoxIndex:nth-child(1) > .colBoxTitle > h3 > a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append(soup.select_one(selector).get('href'))

# CSSセレクタ
selector = '.colBoxInner > .colBoxTab1 > .colBoxIndex:nth-child(2) > .colBoxTitle > h3 > a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append(soup.select_one(selector).get('href'))
# CSSセレクタ

selector = '.colBoxInner > .colBoxTab1 > .colBoxIndex:nth-child(3) > .colBoxTitle > h3 > a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append(soup.select_one(selector).get('href'))
##-------------- ITmedia end ---------------------##

##-------------- yahoo news it start ---------------------##
# yahoo news itにアクセスする
url = 'https://news.yahoo.co.jp/categories/it'
driver.get(url)

# ソースコードを取得
html = driver.page_source

# HTMLをパースする
soup = BeautifulSoup(html, 'html.parser') # または、'html.parser'

# CSSセレクタ
selector = '.sc-ckYZGd li:nth-child(1) a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append(soup.select_one(selector).get('href'))
# CSSセレクタ
selector = '.sc-ckYZGd li:nth-child(2) a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append(soup.select_one(selector).get('href'))
# CSSセレクタ
selector = '.sc-ckYZGd li:nth-child(3) a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append(soup.select_one(selector).get('href'))
##-------------- yahoo news it end ---------------------##
##-------------- ビリヤードデイズ start ---------------------##
# ビリヤードデイズにアクセスする
url = 'https://www.billiards-days.com/'
driver.get(url)

# ソースコードを取得
html = driver.page_source

# HTMLをパースする
soup = BeautifulSoup(html, 'html.parser') # または、'html.parser'

# CSSセレクタ
selector = '.blogselection > .j-blogarticle:nth-child(1) > h2 > a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append('https://www.billiards-days.com/' + soup.select_one(selector).get('href'))

# CSSセレクタ
selector = '.blogselection > .j-blogarticle:nth-child(2) > h2 > a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append('https://www.billiards-days.com/' + soup.select_one(selector).get('href'))

# CSSセレクタ
selector = '.blogselection > .j-blogarticle:nth-child(3) > h2 > a'
# タイトルを格納、テキスト
titles.append(soup.select_one(selector).get_text())
# URLを格納、属性値
urls.append('https://www.billiards-days.com/' + soup.select_one(selector).get('href'))

##-------------- ビリヤードデイズ end ---------------------##

# ブラウザを終了する(Command + Q と同じ)
driver.quit()



@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    okyo = ["色不異空","空不異色","色即是空","空即是色"]
    count = range(0, len(titles))
    return render_template("index.html",name=name,okyo=okyo, titles=titles, urls=urls ,count=list(count))

if __name__ == "__main__":
    app.run(debug=True)