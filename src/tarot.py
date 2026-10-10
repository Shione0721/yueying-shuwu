# -*- coding: utf-8 -*-
"""月影书屋 · made by 汐宁 —— 桌面版入口"""
import json
import os
import sys

import webview
from urllib.parse import quote



def resource_path(rel):
    if getattr(sys, "frozen", False):
        base = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
        return os.path.join(base, rel)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), rel)


def file_url(path):
    return "file:///" + quote(os.path.abspath(path).replace("\\", "/"), safe="/:")


def data_path():
    if getattr(sys, "frozen", False):
        return os.path.join(os.path.dirname(sys.executable), "tarot_data.json")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "tarot_data.json")


class Api:
    def load(self):
        try:
            with open(data_path(), encoding="utf8") as f:
                return json.load(f)
        except Exception:
            return {}

    def save(self, data):
        try:
            with open(data_path(), "w", encoding="utf8") as f:
                json.dump(data, f, ensure_ascii=False)
            return True
        except Exception:
            return False

    def log(self, msg):
        try:
            with open(data_path() + ".log", "a", encoding="utf8") as f:
                f.write(str(msg) + "\n")
        except Exception:
            pass


def main():
    webview.create_window(
        "月影书屋 · made by 汐宁",
        url=file_url(resource_path("tarot.html")),
        js_api=Api(),
        width=1080,
        height=800,
        min_size=(780, 620),
        text_select=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
