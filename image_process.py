#!/usr/bin/env python
# -*- cording: utf-8 -*-
#インポート
import os
import sys
import time
import subprocess
import cv2
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

#グレースケール
def gray():
    # 画像処理&ファイルの保存
    pass

#Cannyフィルタ
def canny(path):
    im=cv2.imread(path)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    gray=cv2.Canny(gray,100,200)
    #書き出し
    cv2.imwrite(path, gray)

#顔を検出して枠で囲う
def face_detection(path):

    #顔検出のライブラリ読み込み
    face_cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    #処理するファイルを読み込む
    src = cv2.imread(path)
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(src_gray)
    #顔検出範囲を表示
    for x, y, w, h in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = src[y: y + h, x: x + w]
        face_gray = src_gray[y: y + h, x: x + w]
    #書き出し
    cv2.imwrite(path, src)

#モザイク
def mosaic():
    pass

class ChangeHandler(FileSystemEventHandler):
 
    #ファイルやフォルダが作成された場合
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを作成しました。' % filename)
 
    #ファイルやフォルダが更新された場合
    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを変更しました。' % filename)
 
    #ファイル・フォルダが移動
    def on_moved(self, event):
        pass
 
    #ファイル・フォルダ削除
    def on_deleted(self, event):
        pass


if __name__ == "__main__":
    # WatchDogで監視
    #起動ログ
    print('起動しました')

    #インスタンス作成
    event_handler = ChangeHandler()
    observer = Observer()
 
    #フォルダの監視->upload_images
    observer.schedule(event_handler, "./upload_images", recursive=True)
 
    #監視の開始
    observer.start()
 
    try:
        #無限ループ
        while True:
            #待機
            time.sleep(0.05)
 
    except KeyboardInterrupt:
        #監視の終了
        observer.stop()
        #スレッド停止を待つ
        observer.join()
        #終了ログ
        print('終了します')