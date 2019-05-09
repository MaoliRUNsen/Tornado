# -*- coding：utf-8 -*-
# time ：2019/5/9 20:25
# author: 毛利
import tornado.web


class IndenxHandler(tornado.web.RequestHandler):
    '''
    首页，用户上传图片的展示
    '''
    def get(self):
        self.render('index.html')

class Explorehandler(tornado.web.RequestHandler):
    '''
    最近上传图片的页面
    '''
    def get(self):
        self.render('explore.html')

class PostHandler(tornado.web.RequestHandler):
    '''
    当个图片详情页面
    '''
    def get(self,post_id):
        self.render('post.html',post_id = post_id)
