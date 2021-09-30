import requests
from bs4 import BeautifulSoup as bs
import re

def Scrape(url,header):
    Articles = []
    r = requests.get(url,headers=header)
    if r.status_code == 200 :
        soup = bs(r.content, 'lxml')

        sections = soup.find_all('section')
        Base_Link = url
        Date_posted = []
        COMMENTS = []
        Claps = []

        # ------------------------------
        # Followers
        # ------------------------------
        try:
          Followers = soup.find('a',string = re.compile(r'Followers')).text
        except : Followers = 0

        # ------------------------------
        # Comments
        # ------------------------------
        for n in soup.find_all('button'):
          try:
            n.div.div.svg
            try:
              Comments = int(n.div.div.p.text)
            except:
              Comments = 0
            COMMENTS.append(Comments)
          except:
            pass

        # ------------------------------
        # Claps
        # ------------------------------
        # for claps in soup.find_all('p'):
        #   try:
        #     Claps.append(claps.button.text)
        #   except: pass

        # ------------------------------
        # Date Posted
        # ------------------------------
        for i in soup.find_all('span'):
          try:
            if i.a.p == "None" or i.a.p is None:
              pass
            else:
              Date_posted.append(i.a.p.text)
          except:
            pass
        # ------------------------------
        # Reading Time
        # ------------------------------
        read = soup.find_all('span', string=re.compile(r'min read'))
        # ------------------------------
        # Images, Descriptions, Title, Link
        # ------------------------------
        k = 0

        # print('[*] Followers : {}'.format(Followers))

        for i in sections :
          try:
            try:
              Image       = i.find('img')['src']
            except :
              Image       = None
            Link        = url + i.find('h1').find_next()['href']
            Title       = i.h1.text
            Description = i.text.replace(Title,'')

            # print('[*] Title : {}\n[*] Image : {}\n[*] Description : {}'.format(Title,Image,Description))
            # print('[*] Reading Time : {}'.format(read[k].text))
            # print('[*] Date Posted  : {}'.format(Date_posted[k]))
            # print('[*] Link         : {}'.format(Link))
            # # print('[*] Claps        : {}'.format(Claps[k]))
            # print('[*] Comments     : {}'.format( COMMENTS[k]))

            Articles.append({
                'Title'         : Title,
                'Image'         : Image,
                'Reading'       : read[k].text,
                'Posted'        : Date_posted[k],
                'Description'   : Description,
                'Comment'      : COMMENTS[k],
                'Link'          : Link

            })

            k+=1
            # print('--------------------------------')
          except:
            pass
    else:
        pass
    if len(Articles) < 1:

        Articles.append({
            'Title'         : '',
            'Image'         : None,
            'Reading'       : '',
            'Posted'        : '',
            'Description'   : '',
            'Comment'       : '',
            'Link'          : 'Link'

        })
    return Articles
