import socket, time, re

def connect_to_server(ip, port, retry = 10):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        print (e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port, retry)       
    
    return s

def get_source(s, ip, page):
    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += ip
    get += CRLF
    get += CRLF

    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    print (response)
    return response
  
def get_all_links(response, list_links, cnt):
    beg = 0
    while True:
        beg_str = response.find('href="', beg)   
        if beg_str == -1:
            return list_links  
        end_str = response.find('"', beg_str + 6)      
        link = response[beg_str+6:end_str]
        if link not in list_links:
            if link.find("html") != -1:
                listLinks.insert(cnt, link)
                cnt+=1
        beg = end_str + 1

ip = 'www.optimazadar.hr'
port = 80
page = '1280/djelatnost1280.html'
s = connect_to_server(ip, port)
print (s)
response = get_source(s, ip, page)
listLinks = []
cnt = 0
get_all_links(response, listLinks,cnt)
end_page = page.find("/")

for link in listLinks:
    page = page[0:end_page+1] + link
    s = connect_to_server(ip, port)
    response = get_source(s,ip,page)
    get_all_links(response, listLinks, cnt)
    cnt +=1
    if(cnt == 50): break

print(listLinks)