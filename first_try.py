import requests
from bs4 import BeautifulSoup

host = 'https://www.haodf.com'


def get_hospital_list_from_page(page):
    soup = BeautifulSoup(page,'html5lib')
    border = soup.find('div', class_='m_ctt_green')
    hospital_ul = border.contents[1]
    ret = []
    for li in hospital_ul.children:
        if li.name == "li":
            a = li.find('a')
            href = host + a['href']
            name = a.text.strip()
            o = {}
            o['href'] = href
            o['name'] = name
            ret.append(o)
    return ret


def get_hospital_page(hospital_info):
    addr = hospital_info['href']
    name = hospital_info['name']
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Upgrade-Insecure-Requests':'1',
        'Referer':'https://www.haodf.com/yiyuan/beijing/list.htm',
        'Host':'www.haodf.com',
        } #为了突破反爬措施加的headers
    r = requests.get(addr, headers=headers)
    page_text = r.text.encode('gbk').decode('gbk')
    return page_text


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
    hospital_list = get_hospital_list_from_page(chaoyang_page)
    #for hospital_info in hospital_list: #我调好后会用循环进行大规模爬取

    hospital_try = hospital_list[0] #第一次try一下不爬所有医院。。。
    hospital_page_text = get_hospital_page(hospital_try)
    hospital_file = open('hospital1.html', 'w', encoding='utf-8')
    try:
        hospital_file.write(hospital_page_text)
    finally:
        hospital_file.close()
    


if __name__ == "__main__":
    main()
