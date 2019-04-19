#coding:utf-8
from werobot import WeRoBot
import random
from werobot.replies import ArticlesReply, Article

robot = WeRoBot(token='8cf561d3b980e1143ee962256805be24')
# 明文模式不需要下面三项
# robot.config["APP_ID"]='wxbb2b262238938195'
# #robot.config["APP_SECRET"]='e5007656796347a71fbc7125ac1d17de'
# robot.config['ENCODING_AES_KEY'] = 'OWWxHPqt4tkz274VtiLNcpGmQmerlk4E0lWazNUjMHP'


# 被关注
@robot.subscribe
def subscribe(message):
    return '你好，欢迎关注鸭先知数据！'


# 取消关注
@robot.unsubscribe
def subscribe(message):
     pass



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

# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message):
    return message.img




#
# robot.config['HOST'] = '127.0.0.1'
# robot.config['PORT'] = 9001
# robot.run()



# 获取操作的客户端

# #自定义菜单
# from werobot import WeRoBot
# robot = WeRoBot()
# robot.config["APP_ID"] = "你的 AppID"
# robot.config["APP_SECRET"] = "你的 AppSecret"
#
# client = robot.client
#
# client.create_menu({
#     "button":[{
#          "type": "click",
#          "name": "今日歌曲",
#          "key": "music"
#     }]
# })
#
# @robot.key_click("music")
# def music(message):
#     return '你点击了“今日歌曲”按钮'