from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from Article.models import *

#登录装饰器
def loginVaild(fun):
    def inner(request,*args,**kwargs):
        username=request.COOKIES.get('name')
        username_session=request.session.get('username')
        print(username_session)
        if username:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return inner

#登出
def logout(request):
    response=HttpResponseRedirect('/index/')
    response.delete_cookie('name')
    ### 删除session  目的是 用户再次使用相同的session id 进行访问时 拿到的值是不一样的
    # del request.session['username']  ###删除指定session 删除的是保存在服务器上面session的值
    request.session.flush()  ##删除所有的session

    return response

@loginVaild
def index(request):
    """
    查询6条数据
    查询7条推荐数据
    查询点击热度排行榜的12条数据
    """
    # username=request.COOKIES.get('name')
    # print(username)
    # if username:
    article=Article.objects.order_by('-date')[:6]
    recommend_article=Article.objects.filter(recommend=1).all()[:7]
    heat_article=Article.objects.order_by('-heat')[:12]
    return render(request,'index.html',locals())
    # else:
    #     return HttpResponseRedirect('/login/')

def about(request):
    return render(request,'about.html')
def listpic(request):
    return render(request,'listpic.html')

def newslistpic(request,page=1):
    page=int(page)
    article=Article.objects.order_by('-date')
    paginator=Paginator(article,6)#每页显示6条数据
    page_obj=paginator.page(page)  # 当前页 <Page 4 of 17>
    # print(page_obj)
    ##获取当前页
    current_page=page_obj.number
    print(current_page)
    start=current_page -3
    if start<1:
        start=0
    end=current_page +2
    if end>paginator.num_pages:
        end=paginator.num_pages
    if start ==0:
        end = 5
    if end==paginator.num_pages:
        start=end-5
    page_range=paginator.page_range[start:end]
    return render(request,'newslistpic.html',locals())

def base(request):
    return render(request,'base.html')
def addarticle(request):
    for x in range(100):
        article=Article()
        article.title = 'title_%s' % x
        article.content = 'content_%s' % x
        article.description = 'description_%s' % x
        article.author = Author.objects.get(id=1)
        article.save()
        article.type.add(Type.objects.get(id=1))
        article.save()
    return HttpResponse('增加数据')

from django.core.paginator import Paginator
def fytest(request):
    ##使用django自带分页 Paginator 的时候 原数据要增加排序属性
    article=Article.objects.all().order_by('-date')
    # print(article)
    #每次显示5条数据
    paginator=Paginator(article,5)  #设置每一页显示多少条，返回一个Paginator 对象
    # print(paginator.count)  ## 返回内容总条数
    # print(paginator.page_range)  ##可迭代的页数
    # print(paginator.num_pages)   ##最大页数
    page_obj=paginator.page(2)
    print(page_obj)    ##可以有的页数的数据  表示的当前对象
    for one in page_obj:
        print(one.content)

    # print(page_obj.number)  ##当前页数
    # print(page_obj.has_next())   ##有没有下一页 返回值 是True 或者Flase
    # print(page_obj.has_previous())  ##判断是否有上一页  是True 或者是Flase
    # print(page_obj.has_other_pages())  ##判断是否有其他页 是True或者是Flase
    # print(page_obj.next_page_number())##返回 下一页的页码 如果没有下一页 抛出异常
    # print(page_obj.previous_page_number())  ##返回上一页的页码

    return HttpResponse('分页功能测试')
def textcontent(request,id):
    id=int(id)
    article=Article.objects.get(id=id)
    return render(request,'textcontent.html',locals())
def sexceshi(request):
    author=Author.objects.get(id=1)
    print(author.gender)
    gender=author.get_gender_display()
    print(gender)
    return HttpResponse('性别测试')

def request(request):
    ##获取get请求传递参数
    # data=request.GET
    # print(data)
    # print(data.get('name'))
    # print(type(data.get('name')))
    # print(data.get('age'))
    # return HttpResponse('姓名：%s 年龄：%s'%(data.get('name'),(data.get('age'))))

    ##request 包含请求信息的请求对象
    # print(dir(request))
    # print(request.COOKIES)   #用户身份
    # print(request.FILES)    #请求携带的文件，比如文件
    # print(request.GET)   #get 请求携带的参数
    # print(request.POST)    #post 请求携带的参数
    # print(request.scheme)    #scheme  https还是http
    # print(request.method)   #method  请求的方式
    # print(request.path)    #path 请求的路径
    # print(request.body)    #body  请求的主体，返回的是一个字符串
    #
    # print(request)
    # print(dir(request))
    # meta=request.COOKIES
    # for i in meta:
    #     print(i)
    # print(request.FILES)
    # print(request.GET)
    # print(request.POST)
    print(request.method)

    # meta=request.META  ##  包含了具体的请求数据，包含所有的http的请求信息
    # # print(meta)
    # for key in meta:
    #     print(key)
    # print('++++')
    # print(request.META.get('OS'))  ##请求的系统
    # print(request.META.get('HTTP_USER_AGENT'))  ##发出请求的浏览器版本
    # print(request.META.get('HTTP_HOST'))  ##请求的主机
    # print(request.META.get('HTTP_REFERER'))  ##请求的来源
    #


    # meta=request.META
    # # print(meta)
    # # for i in meta:
    # #     print(i)
    # print('+++++++++++++++++++')
    # print(request.META.get('OS'))
    # print(request.META.get('HTTP_USER_AGENT'))
    # print(request.META.get('HTTP_HOST'))
    # print(request.META.get('HTTP_REFERER'))
    return HttpResponse('请求测试')

def formtest(request):
    ##get 请求
    # data= request.GET
    # # # print(data)
    # serach=data.get('serach')
    # print(serach)
    #
    # ##通过输入搜索查询值
    # if serach:
    #     article=Article.objects.filter(title__contains=serach).all()
    # print(article)


    # print(request.method)
    # data=request.POST
    # print(data.get('username'))
    # print(data.get('password'))

    print(request.method)
    data=request.POST
    print(data.get('username'))
    print(data.get('password'))

    return render(request,'formtest.html',locals())

import hashlib
def setPassword(password):
    ##实现一个密码加密
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result



from Article.forms import Register
def register(request):
    register_from=Register()
    error=''
    if  request.method=='POST':
        data=Register(request.POST)   #将post请求传递过来的数据，传给form表单进行检验
        if data.is_valid():
            clean_data=data.cleaned_data  #将通过校验传回来的数据返回成一个字典类型
            username=clean_data.get('name')
            password=clean_data.get('password')
            user=User()
            user.name=username
            user.password=setPassword(password)
            user.save()
            error='添加成功'
        else:
            error=data.errors


    # register_from=Register()
    # if request.method=='POST':
    #     data=request.POST
    #     username=data.get('name')
    #     print(username)
    #     password=data.get('password')
    #     print(password)
    #     # password2=data.get('password2')
    #
    #     if username and password :
    #         if User.objects.filter(name=username).first():
    #         # error='数据重复'
    #             content = '参数不全'
    #         else:
    #             user=User()
    #             user.name=username
    #             user.password=setPassword(password)
    #             user.save()
    #             content='添加成功'
    #         # error='添加成功'
    return render(request,'register.html',locals())

def ajax_get(request):
    return render(request, 'ajax_get.html')
def ajax_get_data(request):
    result={'code':10000,'content':''}
    data=request.GET
    username=data.get('username')
    password=data.get('password')
    # print(username)
    # print(password)
    if len(username)==0 or len(password)==0 :
        result['code']=10001
        result['content']=u'参数为空'
    else:
        user=User.objects.filter(name=username,password=setPassword(password)).first()
        if user:
            result['code']=10000
            result['content']=u'用户存在可登陆'
        else:
            result['code']=10002
            result['content']=u'用户不存在或者密码错误'

    return JsonResponse(result)
    # return HttpResponse('ajax提交')


def ajax_post(request):
    return render(request,'ajax_post.html')
def ajax_post_data(request):
    result={}
    data=request.POST
    username=data.get('username')
    # print(username)
    password=data.get('password')
    # print(password)
    if len(username)==0 or len(password)==0:
        result['code']=10001
        result['content']='参数为空'
    else:
        user=User()
        user.name=username
        user.password=setPassword(password)
        try:
            user.save()
            result['code']=10000
            result['content']='添加成功'
        except:
            result['code']=10002
            result['content']='添加失败'

    return JsonResponse(result)

def checkusername(request):
    result={'code':10000,'content':''}
    username=request.GET.get('username')
    user=User.objects.filter(name=username).first()
    if user:
        result={'code':10001,'content':'用户已存在'}
    else:
        result={'code':10000,'content':'用户不存在'}
    return JsonResponse(result)

from django.http import HttpResponseRedirect
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(name=username).first()
        if user:
            if user.password == setPassword(password):
                response = HttpResponseRedirect('/index/')
                response.set_cookie('name',username)
                request.session['username']=username
                return response
    return render(request,'login.html')

from django.http import JsonResponse
def ajax_gets(request):
    return render(request,'ajax_gets.html')
def ajax_gets_data(request):
    result = {'code':10000,'content':''}
    data = request.GET
    print(data)
    username=data.get('username')
    # print(username)
    password=data.get('password')
    if len(username)==0 and len(password)==0:
        result['code'] = 10001
        result['content'] = '参数不正确'
    else:
        user=User.objects.filter(name=username,password=setPassword(password)).first()
        if user:
            result['code'] = 10000
            result['content'] = '可以登陆'
        else:
            result['code'] = 10001
            result['content'] = '用户不存在或密码错误'

    return JsonResponse(result)

def ajax_posts(request):
    return render(request,'ajax_posts.html')
def ajax_posts_data(request):
    result= { 'code':10000,'content':''}
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username)
    if len(username)==0 or len(password)==0:
        result['code']=10001
        result['content']='参数有误'
    else:
        user=User.objects.filter(name=username,password=password).first()
        if user:
            result['code']=10000
            result['content']='用户登录成功'
        else:
            result['code']=10002
            result['content']='用户不存在或密码输入错误'
    return JsonResponse(result)