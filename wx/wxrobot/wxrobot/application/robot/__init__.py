#coding=utf8

from werobot import WeRoBot

robot = WeRoBot(token='token')


@robot.handler
def hello(message):
    return 'Hello World!'