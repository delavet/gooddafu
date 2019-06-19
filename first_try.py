import requests
from bs4 import BeautifulSoup

host = 'https://www.haodf.com'


def get_hospital_list_from_page(page):
    soup = BeautifulSoup(page,'html5lib')
    list_html = soup.find('div', class_='m_ctt_green')


def get_chaoyang_page():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Upgrade-Insecure-Requests':'1',
        'Referer':'https://www.haodf.com/yiyuan/beijing/haidian/list.htm',
        'Host':'www.haodf.com',
        } #为了突破反爬措施加的headers
    r = requests.get('https://www.haodf.com/yiyuan/beijing/chaoyang/list.htm',headers=headers) #获取到朝阳区的医院列表
    chaoyang = open('chaoyang.html', 'w', encoding='utf-8')
    try:
        page_text = r.text.encode('gbk').decode('gbk')
        chaoyang.write(page_text)   #把页面存下来看一看……
    finally:
        chaoyang.close()
    return page_text


def main():
    chaoyang_page = get_chaoyang_page()

if __name__ == "__main__":
    

