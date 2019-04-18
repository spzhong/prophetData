#coding:utf-8
from werobot import WeRoBot
import random
from werobot.replies import ArticlesReply, Article

robot = WeRoBot(token='8cf561d3b980e1143ee962256805be24')
# 明文模式不需要下面三项
# robot.config["APP_ID"]='wxbb2b262238938195'
# #robot.config["APP_SECRET"]=''
# robot.config['ENCODING_AES_KEY'] = 'OWWxHPqt4tkz274VtiLNcpGmQmerlk4E0lWazNUjMHP'


# 被关注
@robot.subscribe
def subscribe(message):
    return '你好，欢迎关注鸭先知数据！'


# 卡片 回复卡片
@robot.filter('卡片')
def blog(message):
    reply = ArticlesReply(message=message)
    article = Article(
        title="标题",
        description="测试百度",
        img="https://upload.jianshu.io/users/upload_avatars/9691564/d4404291-308a-4159-b324-4ae400d8c977.png",
        url="http://www.baidu.com"
    )
    reply.add_article(article)
    return reply


# 文本消息返回原文
@robot.text
def echo(message):
    return message.content

robot.config['HOST'] = '127.0.0.1'
robot.config['PORT'] = 9001
robot.run()
