# -*- coding: utf-8 -*-

from django.db import models


# 微信的OpenID
class wxOpenID(models.Model):
    openID = models.CharField(max_length=100, db_index=True)
    time = models.CharField(max_length=20)
    name = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=20,null=True)
    # 是否可用，0是默认可用，1是禁用
    availability = models.IntegerField(default=0)


# 接收微信的消息
class msg(models.Model):
    # 公共属性
    message_id = models.CharField(max_length=100, db_index=True)
    # OpenID -- 发送方账号
    source = models.CharField(max_length=100, db_index=True)
    time = models.CharField(max_length=20)
    # text,image,link,location,voice,video,unknown
    type = models.CharField(max_length=20)
    # text
    content = models.CharField(max_length=1024,null=True)
    # image
    img = models.CharField(max_length=1024, null=True)
    # link (标题，描述，链接)
    title = models.CharField(max_length=1024, null=True)
    description = models.CharField(max_length=1024, null=True)
    url = models.CharField(max_length=1024, null=True)
    # location
    location = models.CharField(max_length=1024, null=True)
    scale = models.CharField(max_length=1024, null=True)
    label = models.CharField(max_length=1024, null=True)
    # voice
    media_id = models.CharField(max_length=100, null=True)
    format = models.CharField(max_length=100, null=True)
    recognition = models.CharField(max_length=1024, null=True)
    # video
    media_id = models.CharField(max_length=100, null=True)
    thumb_media_id  = models.CharField(max_length=100, null=True)
    # unknown
    raw = models.CharField(max_length=1024, null=True)