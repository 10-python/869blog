from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.forms import LoginForm,RegisterForm
# 关于我们
def test(request):
    context={}
    context['login_form'] = LoginForm()
    context['register_form'] = RegisterForm()
    return render(request,'information.html',context)
@csrf_exempt
def contact(request):
    name=request.POST.get('name','')
    email=request.POST.get('email','')
    content=request.POST.get('content','')
    data={}
    if email!='':
        try:
            send_mail(
                '博客有消息啦!',  # 邮件主题
                '用户:%s(%s):%s'% (name,email,content),  # 内容
                ['1765300685@qq.com '],  # from
               ['1765300685@qq.com '],#to
                fail_silently=False,
            )
            data['status'] = "SUCCESS"
        except Exception as e:
            print(e)
            data['status'] = "发送失败"
    else:
        data['status']='操作失败,请重新操作'

    return JsonResponse(data)
def information(request):
    context = {}
    context['login_form'] = LoginForm()
    context['register_form'] = RegisterForm()
    return render(request,'error.html',context)