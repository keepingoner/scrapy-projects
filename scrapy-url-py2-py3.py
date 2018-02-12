"""
scrapy
"""

#python2.7

import urllib2
resp = urllib2.urlopen("http://www.baidu.com")
print resp.read()
#调用了urllib2库里边的urlopen方法，传入一个url，这个方法一般接收三个参数，如下：
urlopen(url, data, timeout) 
第一个是地址，data是访问url时要传送的数据，timeout是设置超时时间，后两个为选填，data默认为None，


#构造方法
import urllib2  
request = urllib2.Request("http://www.baidu.com")  
response = urllib2.urlopen(request)  
print response.read()
这样写会更明白一些


#POST GET 的构造
#POST
import urllib  
import urllib2  
values = {"username":"1016903103@qq.com","password":"XXXX"}  
data = urllib.urlencode(values)   
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"  
request = urllib2.Request(url,data)  
response = urllib2.urlopen(request)  
print response.read() 


#GET
import urllib  
import urllib2  
values={}  
values['username'] = "1016903103@qq.com"  
values['password']="XXXX"  
data = urllib.urlencode(values)   
url = "http://passport.csdn.net/account/login"  
geturl = url + "?"+data  
request = urllib2.Request(geturl)  
response = urllib2.urlopen(request)  
print response.read()  


#设置headers
import urllib    
import urllib2     
url = 'http://www.server.com/login'  
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    
values = {'username' : 'cqc',  'password' : 'XXXX' }    
headers = { 'User-Agent' : user_agent }    
data = urllib.urlencode(values)    
request = urllib2.Request(url, data, headers)    
response = urllib2.urlopen(request)    
page = response.read()   

注意：对付防盗链，服务器会识别headers中的referer是不是它自己
如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer，如下：
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,  
                        'Referer':'http://www.zhihu.com/articles' }  
其他设置：
User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
application/json ： 在 JSON RPC 调用时使用
application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务


Proxy（代理）的设置：
urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。
假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。
所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理。
下面一段代码说明了代理的设置用法

import urllib2  
enable_proxy = True  
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})  
null_proxy_handler = urllib2.ProxyHandler({})  
if enable_proxy:  
    opener = urllib2.build_opener(proxy_handler)  
else:  
    opener = urllib2.build_opener(null_proxy_handler)  
urllib2.install_opener(opener)  


Timeout设置：
可以设置等待多久超时，为了解决一些网站实在响应过慢而造成的影响。
例如下面的代码,如果第二个参数data为空那么要特别指定是timeout是多少，写明形参，如果data已经传入，则不必声明。

import urllib2  
response = urllib2.urlopen('http://www.baidu.com', timeout=10) 
或者
import urllib2  
response = urllib2.urlopen('http://www.baidu.com',data, 10) 


#URLError异常处理：
#URLError捕获相应异常：

import urllib2  
requset = urllib2.Request('http://www.xxxxx.com')  
try:  
    urllib2.urlopen(requset)  
except urllib2.URLError, e:  
    print e.reason  
    
 
#HTTPError：
HTTPError是URLError的子类，在你利用urlopen方法发出一个请求时，
服务器上都会对应一个应答对象response，其中它包含一个数字”状态码”。

100：继续  客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。

101： 转换协议  在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。

102：继续处理   由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。

200：请求成功      处理方式：获得响应的内容，进行处理

201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到    处理方式：爬虫中不会遇到

202：请求被接受，但处理尚未完成    处理方式：阻塞等待

204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。    处理方式：丢弃

300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。    处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源    处理方式：重定向到分配的URL

302：请求到的资源在一个不同的URL处临时保存     处理方式：重定向到临时的URL

304：请求的资源未更新     处理方式：丢弃

400：非法请求     处理方式：丢弃

401：未授权     处理方式：丢弃

403：禁止     处理方式：丢弃

404：没有找到     处理方式：丢弃

500：服务器内部错误  服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。

501：服务器无法识别  服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。

502：错误网关  作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。

503：服务出错   由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复





