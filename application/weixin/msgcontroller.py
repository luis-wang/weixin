# -*- coding: utf-8 -*-
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from application.Logger import weixinLogger
from application.weixin.userinfo import UserInfo

# 定义日志工具
log = weixinLogger.getInstance().logging


class MsgTextController:
    """
    文本消处理
    """


    def __init__(self):
        """

        :return:
        """


    def reciveTextMsg(self,requstHandler,msgData):
        """
            处理文本消息
        :param msgData:
        :return:
        """
        # 消息类型
        msgType = msgData.find('MsgType').text
        # 公众账号
        toUserName = msgData.find('ToUserName').text
        # 来源用户名称
        fromUserName = msgData.find('FromUserName').text
        # 消创建时间
        createTime = msgData.find('CreateTime').text
        # 消息类型
        msgType = msgData.find('MsgType').text
        # 消息ID
        msgid = msgData.find('MsgId').text
        # 消息内容
        content = msgData.find('Content').text
        log.info("存储消息：%s" % content)

        #user = UserInfo.get_userinfo_openid(fromUserName)

        #log.info("用户 %s 发来了消息: %s" %(user["nickname"],content))


        """
        根据content去数据库中查询要回复的内容，如果存在，将查询的信息直接回复
        否则回复:你在说什么
        """


        # 根据消内容，确认回复消息
        # sendMsgConent = getSendMsg(content)
        sendMsgContent = "你在说什么？我又不认识你。。。\n" \
                         "<a href='pyweb.coding.io'>来这看看吧</a>"

        sendMsgData = { "toUser":fromUserName,"fromUser":toUserName,"msgType":msgType,
                        "sendMsg":sendMsgContent }


        # 调用回复文本消息方法
        self.sendTextMsg(requstHandler,sendMsgData)
        return True


    def sendTextMsg(self,requstHandler,sendMsgData):
        """
            发送文本消息
        """

        sendXmlStr =\
            """<xml>
                    <ToUserName><![CDATA[""" + sendMsgData["toUser"] + """]]></ToUserName>
                <FromUserName><![CDATA[""" + sendMsgData["fromUser"] + """]]></FromUserName>
                <CreateTime>""" + str(int(time.time())) + """</CreateTime>
                <MsgType><![CDATA[""" + sendMsgData["msgType"] + """]]></MsgType>
                <Content><![CDATA[""" + sendMsgData["sendMsg"] + """]]></Content>
                </xml>
            """

        # 设置返回消息头
        requstHandler.set_header("Content-type","text/xml; charset='UTF-8'")
        requstHandler.write(sendXmlStr)
        return True


class MsgImgController:
    """
    图片消息处理
    """


    def __init__(self):
        pass


    def reciveImgMsg(self,requstHandler,msgData):
        """
        处理图片消息
        :param requstHandler:
        :param msgData:
        :return:
        """
        pass


class MsgVoiceController:
    """
    声音消息处理
    """


    def __init__(self):
        pass


    def reciveVoiceMsg(self,requstHandler,msgData):
        pass


class MsgVideoController:
    """
    视频消息处理
    """


    def __init__(self):
        pass


    def reciveVideoMsg(self,requstHandler,msgData):
        pass


class MsgLocationController:
    """
    位置消息处理
    """


    def __init__(self):
        pass


    def reciveLocationMsg(self,requstHandler,msgData):
        pass


class MsgLinkController:
    """
    链接消息处理
    """


    def __init__(self):
        pass


    def reciveLinkMsg(self,requstHandler,msgData):
        pass


class MsgEventController:
    """
    事件消息处理
    """


    def __init__(self):
        pass


    def reciveEventMsg(self,requstHandler,msgData):
        eventtype = msgData.find("Event").text

        if eventtype == "subscribe":
            # 订阅事件
            pass
        elif eventtype == "unsubscribe":
            # 取消订阅事件
            pass
        elif eventtype == "SCAN":
            # 扫描订阅事件
            pass
        elif eventtype == "LOCATION":
            # 上报地理位置事件
            pass
        elif eventtype == "CLICK":
            # 自定义菜单事件
            pass
        elif eventtype == "VIEW":
            # 点击菜单跳转链接事件
            pass


__author__ = 'zhgk'
