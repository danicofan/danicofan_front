# -*- coding: utf-8 -*-
import argparse
import json
import os

import tornado.web

import danicofan

ROOTPATH = os.path.dirname(__file__)

danime = danicofan.danime.DAnimeService(os.path.join(ROOTPATH, "data"))


class SeriesHandler(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument("title")
        series = danime.search_series_by_title(title)
        print(series)

        self.write(series.dump_json())


class AllTitlesHandler(tornado.web.RequestHandler):
    def initialize(self):
        all_series = []
        for series in danime.title_index.values():
            d = series.dump_dict()
            del d["videos"]
            all_series.append(d)
        self.all_series = all_series

    def get(self):
        self.write(json.dumps(self.all_series))


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
    parser.add_argument("--datapath")
    args = parser.parse_args()

    if args.datapath is not None:
        danime = danicofan.danime.DAnimeService(args.datapath)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()
