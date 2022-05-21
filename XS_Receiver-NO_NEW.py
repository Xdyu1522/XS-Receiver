import os
import threading
import math
import ssl

import bs4
import requests
import tqdm
from fake_useragent import UserAgent

ssl._create_default_https_context = ssl._create_unverified_context

class Download: 
    def __init__(self, url, root): 
        self.url = url
        self.ua = UserAgent()
        self.root = root

    def get_list(self): 
        self.ym_download = requests.get(url, headers={'User-Agent': str(self.ua.random)})
        self.ym_download.encoding = self.ym_download.apparent_encoding #!处理字符编码，否则可能出现乱码！
        ym_download_find = bs4.BeautifulSoup(self.ym_download.text, 'html.parser')
        self.title_of_book = ym_download_find.select('h1')[0].getText()
        list_find = ym_download_find.select('#list > dl > dd > a')
        self.cha_list = []
        for i in list_find: 
            href = i.get('href')
            self.cha_list.append((i.getText(), f'{self.root}{href}'))
        os.makedirs(self.title_of_book, exist_ok=True)
        os.chdir(f'./{self.title_of_book}')
        print('开始获取.')
        self.bar = tqdm.tqdm(total=len(self.cha_list))

    #TODO:函数`get_book`获取章节内容并写入文件
    def get_book(self, _from, to, Tname): 
        cha_id = 0
        for book in self.cha_list[_from:to-1]: 
            try: 
                get = requests.get(book[1], headers={'User-Agent': str(self.ua.random)})
                get.encoding = get.apparent_encoding
                find = bs4.BeautifulSoup(get.text, 'html.parser')
                find_text = find.select('#content')
                text = find_text[0].getText()
                text = text.replace('\xa0\xa0\xa0\xa0', '\n\n\u3000\u3000').replace('\xa0\xa0\xa0\xa0', '')
                name = book[0].replace('*', '').replace('?', '')

                with open(f'{Tname}.{cha_id}{name}.txt', 'w', encoding='utf-8') as f: 
                    f.write(f'\u3000\u3000{book[0]}')
                    f.write(text)
            except Exception: 
                tqdm.tqdm.write(f'{book[0]}获取失败.')
            finally: 
                cha_id += 1
                self.bar.update(1)
        
    

    #TODO:函数`run`增加多线程获取内容
    def main(self):   # sourcery skip: convert-to-enumerate, for-append-to-extend, list-comprehension, merge-list-appends-into-extend, merge-list-extend, move-assign-in-block, unwrap-iterable-construction
        self.get_list()
        num = len(self.cha_list)
        fen_pei = []
        piece = num / 8
        threads = []
        # if debug == True: self.thread_num = 3
        # elif len(self.cha_list) % 3 == 0: self.thread_num = 3
        # elif len(self.cha_list) % 2 == 0: self.thread_num = 2
        # else: self.thread_num = 1

        # if self.thread_num == 1: 
        #     self.get_book(0, len(self.cha_list))

        # elif self.thread_num == 2: 
        #     fen_pei = [(0, math.ceil(len(self.cha_list) / 2)), (math.ceil(len(self.cha_list) / 2 + 1), len(self.cha_list))]
        #     therads = []
        #     for i in fen_pei: 
        #         therads.append(threading.Thread(target=self.get_book, args=(i[0], i[1])))
        #     for t in therads: 
        #         t.setDaemon(True)
        #         t.start()
        #     t.join()
        
        # elif self.thread_num == 3: 
        #     fen_pei = [(0, math.ceil(len(self.cha_list) / 3)), (math.ceil(len(self.cha_list) / 3 + 1), len(self.cha_list))]
        fen_pei.append((0, math.ceil(piece)))
        fen_pei.append((math.floor(piece) + 1, math.ceil(piece * 2)))
        fen_pei.append((math.floor(piece * 2) + 1, math.ceil(piece * 3)))
        fen_pei.append((math.floor(piece * 3) + 1, math.ceil(piece * 4)))
        fen_pei.append((math.floor(piece * 4) + 1, math.ceil(piece * 5)))
        fen_pei.append((math.floor(piece * 5) + 1, math.ceil(piece * 6)))
        fen_pei.append((math.floor(piece * 6) + 1, math.ceil(piece * 7)))
        fen_pei.append((math.floor(piece * 7) + 1, math.ceil(piece * 8)))

        i = 0
        for th in fen_pei: 
            threadObj = threading.Thread(target=self.get_book, args=(th[0], th[1], f'T{i}'))
            threads.append(threadObj)
            threadObj.setName(f'T{i}')
            # threadObj.getName()
            threadObj.start()
            i += 1

        for t in threads: 
            t.join()

        self.bar.close()
        print('完成.')

if __name__ == '__main__': 
    print('仅支持不含"最新章节"的小说页面')
    print('欢迎来到小说接收器,请输入小说链接')
    url = input('请输入链接:')
    root = input('请输入根地址:')
    get =  Download(url=url, root=root)
    get.main()
    # get.bar.close()
