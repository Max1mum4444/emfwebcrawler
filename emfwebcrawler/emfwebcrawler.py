from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import logging
import pandas
import numpy as np
from werkzeug.urls import url_fix


class Analyzer:

    @staticmethod
    def get_links(url):
        url = url_fix(url)
        links = []
        request = requests.get(url)
        if request.status_code == 200:
            try:
                html_page = urlopen(url, timeout=60)
                if html_page.code == 200:
                    soup = BeautifulSoup(html_page, 'lxml')
                    for single_link in soup.findAll('a'):
                        link = single_link.get('href')
                        if link is None:
                            link = ''
                        if not isinstance(link, object):
                            link = ''
                        if (url in link) or (len(link) > 1 and link[0] == '/') or (link.startswith('index.php')):
                            if link.startswith('index.php'):
                                link = '/' + link
                            if link == url:
                                link = '/'
                            if link.startswith(url):
                                link = link[len(url):]
                            links.append(link)
            except Exception as e:
                logging.exception(e)
        return links

    def analyze(self, url, level):
        counter = 1
        depth = 0
        table = pandas.DataFrame([{'id': 1, 'level': 0, 'url': '/'}])
        index_from = 1
        matrix = np.array([[0, 0], [0, 0]])
        matrix_size = 1
        while (index_from <= table['id'].count()) and (depth < level):
            line = table[table['id'] == index_from]
            depth = line['level'].item() + 1
            href = line['url'].item()

            if href.startswith('/'):
                links = self.get_links(url + href)
            else:
                links = self.get_links(url + '/' + href)

            for page in links:
                have_id = table.where(table['url'] == page)['id']
                if have_id.count() < 1:
                    counter = counter + 1
                    table.loc[counter] = [counter, depth, page]
                    print('Added: ', page)
                    index_to = counter
                else:
                    index_to = (table[table['url'] == page]['id']).item()

                if index_to > matrix_size:
                    matrix = np.insert(matrix, index_to, 0, axis=1)
                    matrix = np.insert(matrix, index_to, 0, axis=0)
                    matrix_size = index_to

                matrix[index_from][index_to] = 1
                # print('Matrix - from: ', href, ', to: ', page, ', index_from: ', index_from, ', index_to: ', index_to,', value:', matrix[index_from][index_to])
            index_from += 1
        return table, matrix
