import requests
from bs4 import BeautifulSoup

# Variables
domains = './domains.txt'
save_domains = open(domains, mode='a', encoding='utf-8')

# otras fuentes
f1 = './20170118.txt'


def others(word_list=None):
    with open(f1, mode='r', encoding='utf-8') as arch:
        for linea in arch:
            if linea not in word_list:
                word = linea.replace('\n', '').lower().split('.')[-2:]
                words = '.'.join(word)
                word_list.append(words)
            break
    return word_list


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "lxml")

    for post_text in soup.findAll('td'):
        content = post_text.string
        try:
            word = content.lower().split('.')[-2:]
            words = '.'.join(word)
            if words not in word_list:
                word_list.append(words)
        except:
            pass

    word_list = others(word_list)

    for each_word in word_list:
        save_domains.writelines(' - "' + each_word + '"\n')

    save_domains.close()


start('https://organicweb.com.au/18884/email-marketing/mailchimp-sending-domains')