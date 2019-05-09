# -*- coding：utf-8 -*-
# time ：2019/5/9 20:07
# author: 毛利

import tornado.options
from tornado.options import define,options
from handlers.main import IndenxHandler,Explorehandler,PostHandler


define('port',default='8000',help='Listening port',type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndenxHandler),
            (r'/explore', Explorehandler),
            (r'/post/(?P<post_id>[0-9]+)', PostHandler),
        ]
        settings = dict(
            debug = True,
            template_path = 'templates',
            static_path = 'statics',
        )
        super().__init__(handlers,**settings)

application = Application()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    print('Server start on port {}'.format('8000'))
    tornado.ioloop.IOLoop.current().start()
