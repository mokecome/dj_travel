from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import datetime
from django.urls import reverse_lazy
from myapp.models import User
from django.contrib import messages
from .travel.travel import main
from .travel.Mail import sendmail
from .travel.schedule import Schedule

flag=0
# Create your views here.
def index(request):
    global flag
    if request.session.has_key('user'):
        user = request.session['user']
        if flag == 0:
            # 排程
            work = Schedule()
            work.run()
            flag = 1
        return render(request, "index.html", {"role": user})
    else:
        return render(request, "index.html", {"role": "0"})


def login(request):
    # today = datetime.datetime.now().date()
    return render(request, "login.html")  # 表格會再進入processLogin


def processLogin(request):
    global flag
    account = request.POST.get("account")
    passwd = request.POST.get("passwd")
    if User.objects.filter(account=account).exists():
        u = User.objects.get(account=account)
        if u.passwd != passwd:
            messages.error(request, '帳號/密碼錯誤，請重新輸入')
            return HttpResponseRedirect(reverse_lazy(login))
        else:
            request.session['user'] = u.name
            request.session['mail']=u.mail
            if flag==0:
                # 排程
                work = Schedule()
                work.run()
                flag=1
            return redirect('index')
    else:
        messages.error(request, '查無該帳號請註冊')
        return HttpResponseRedirect(reverse_lazy(login))

def sign(request):
    return render(request, "sign.html")

def processSign(request):
    name = request.POST.get("name")
    mail = request.POST.get("mail")
    account = request.POST.get("account")
    passwd = request.POST.get("passwd")

    if User.objects.filter(account=account).exists():
        messages.error(request, '該帳號已註冊!')
        # return render(request, "logintest.html")
        return HttpResponseRedirect(reverse_lazy(sign))
    else:
        user = User(
            name=name,
            mail=mail,
            account=account,
            passwd=passwd
        )
        user.save()
        return render(request, "login.html", {"message": "0"})

def logout(request):
    try:
        del request.session['user']
    except:
        pass
    return redirect('index')

def viewcharts(request):        #管理者
    #寄送email

    #sendmail(request.session['mail'])
    data4= main('./myapp/travel/去哪儿_数分.csv')
    return render(request, "render.html")    #管理者

'''
def recommend(request):         # 使用者
    data4= main('./myapp/travel/去哪儿_数分.csv')
    return render(request, "mycharts_demo.html")
'''

def chatbot(request):
    return render(request, "chatbot.html")

def processtravel(request):
    # 可以設定權限
    name= request.POST.get("name")
    month = request.POST.get("month")    #下拉
    people = request.POST.get("people")  #下拉選單
    price = request.POST.get("price")
    daydown = request.POST.get("dayup")
    dayup = request.POST.get("daydown")

    price=int(price)
    daydown=int(daydown)
    dayup=int(dayup)

    '''
    user_info = User_info(
            name=name,
            month=month,
            people=people,
            price=price,
            dayup=dayup,
            daydown=daydown
        )
        user_info.save()
    '''


    data4= main('./myapp/travel/去哪儿_数分.csv')
    data5 = data4[data4['旅行月份'] == str(month)]  #下拉式選單
    data6 = data5[data5['人物'] == str(people)]
    data7 = data6[data6['人均费用']<=price]
    data8 = data7[(data7['天数']>=daydown)&(data7['天数']<=dayup)]

    data8.to_html('./templates/df.html')
    data9=data8[['地点', '天数', '人均费用', '人物', '玩法', '旅行月份', '浏览次数']]
    data9.to_csv('./myapp/travel/data9.csv',index=False)
    return HttpResponseRedirect(reverse_lazy(look)) #不能直接渲染

def look(request):  # 查看的

    return render(request, "df.html")


