# coding:utf-8
import json
import urllib, urllib2, base64
import sys

#--------------
# do_ocr
#--------------
def do_ocr(f1,ak,sk):
    try:
    #if 1:
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + ak + '&client_secret=' + sk
        request = urllib2.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib2.urlopen(request)
        content = response.read()

        if content:
            content_js = json.loads(content)
            if content_js.has_key('access_token'):
                access_token = content_js['access_token']
                #print(content)    
                #url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token=' + access_token
                #url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/receipt?access_token=' + access_token
                url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token
                
                f = open(f1, 'rb')
                img = base64.b64encode(f.read())
                params = {"image": img}
                params = urllib.urlencode(params)
                request = urllib2.Request(url, params)
                request.add_header('Content-Type', 'application/x-www-form-urlencoded')
                response = urllib2.urlopen(request)
                content = response.read()
                if (content):
                    #print(content)
                    content_js = json.loads(content)
                    if content_js.has_key('error_code') == False:
                        #for d in content_js['words_result']:
                        #print content_js
                        return 0, content_js['words_result']
                    else:
                        return -1, {'error_msg':content_js['error_msg']}
            else:
                return -1, {'error_msg':'no access_token'}
        else:        
            return -1, {'error_msg':'no content'}

    except Exception as e:
        return -2,{'error_msg':str(e)}
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_name = sys.argv[1]

    ak = 'SD0kxTcbslKAkjVRIafiu7fy'
    sk = 'C6qHOWHelM0u2XVdzlXOZhDdwqpEiYP7'        
    do_ocr(image_name,ak,sk)
    
    
    