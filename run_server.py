# -*- coding: utf-8 -*-
import argparse
import glob
import os
import random

import magic
import tornado
import tornado.httpclient
import tornado.httpserver
import tornado.web

import danicofan
import json

ROOTPATH = os.path.dirname(__file__)

danime = danicofan.danime.DAnimeService(os.path.join(ROOTPATH, "data"))


class SeriesHandler(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument("title")
        series = danime.search_series_by_title(title)
        print(series)

        self.write(series.dump())


class AllTitlesHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(list(danime.title_index.keys())))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(open(os.path.join(os.path.dirname(__file__), "front/index.html")).read())


if __name__ == "__main__":
    application = tornado.web.Application(
        handlers=[
            (r"/", MainHandler),
            (r"/api/series", SeriesHandler),
            (r"/api/all", AllTitlesHandler),
        ],
        static_path=os.path.join(os.path.dirname(__file__), "front/static"),
        debug=True
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()
