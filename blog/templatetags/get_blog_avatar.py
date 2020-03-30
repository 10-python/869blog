from django import template
from ..models import Blog,BlogType
from django.contrib.auth.models import User
from read_statistics.models import ReadNum
#自定义模板标签
register=template.Library()
"""获取高阅读量图片"""
@register.simple_tag
def get_blog_avatar_url(blog):
    try:
        id=ReadNum.objects.filter(id=blog.pk).first().object_id
        avatar=Blog.objects.filter(pk=id).first().avatar.url
    except:
        avatar=None
    return avatar

"""判断用户有无头像"""
@register.simple_tag
def get_blog_user_avatar_url(blog):
    try:
        profile_avatar=User.objects.filter(username=blog.author).first().profile.avatar.url
    except Exception as e:
        profile_avatar=None
    # print(profile_avatar)
    return profile_avatar

"""热门id->object_id"""
@register.simple_tag
def get_blog_for_hotblog(blog):
    id = ReadNum.objects.filter(id=blog.pk).first().object_id
    for_hotblog_blog = Blog.objects.filter(pk=id).first()
    return for_hotblog_blog

"""日期归档数量"""
@register.simple_tag
def get_num_for_date(year,month):
    blogs = Blog.objects.filter(created_time__year=year, created_time__month=month)
    num = blogs.count()
    return num