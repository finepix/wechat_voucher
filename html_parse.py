from bs4 import BeautifulSoup


def get_html_from_file(fn):
    '''
           从文件中读取html，用于测试
        :param fn:
        :return:
    '''
    with open(fn, 'r', encoding='UTF-8') as f:
        return f.read()


def get_result_from_html(html_text):
    '''
            解析网页获取结果
        :param html_text:
        :return:
    '''
    soup = BeautifulSoup(html_text)
    rs = soup.select('.card-wrap')
    for r in rs:
        print(r.get_text().replace(' ', ''))                                      # 未抢到
    others = soup.select('.friends-list > ul').pop().select('li')
    for li in others:

        name = li.select('.main .name').pop().get_text()
        date = li.select('.main .date').pop().get_text()
        right = li.select('.right').pop().get_text()

        right = right.replace(' ', '').replace('\n', '')                         # 去掉空格以及换行符
        # print('|' + name.ljust(15) + '|' + date.ljust(15) + '|' + right.ljust(8) + '|')           # 代码洁癖
        print('{0:<20}\t{1:{3}<12}\t{2:^6}'.format(name, date, right, chr(12288)))


if __name__ == '__main__':
    filename = 'voucher.html'
    html = get_html_from_file(filename)
    get_result_from_html(html)






