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
def gray(filename):
    #filename は　upload_imagesに入るファイルの名前(文字列型)　例えば sample.jpg　など
    # TODO cv2でグレースケールにする
    #ファイル読み込み　コメントを外して利用して
    #im=cv2.imread("./upload_images/" + filename)
    #ファイルの書き出し　コメントを外して利用して
    #cv2.imwrite("./output_gray_images/" + filename, グレーにした画像を入れた変数名)
    pass

#Cannyフィルタ
def canny(filename):
    im=cv2.imread("./upload_images/" + filename)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    gray=cv2.Canny(gray,100,200)
    #書き出し
    cv2.imwrite("./output_canny_images/" + filename, gray)

#顔を検出して枠で囲う
def face_detection(filename):

    #顔検出のライブラリ読み込み
    face_cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    #処理するファイルを読み込む
    src = cv2.imread("./upload_images/" + filename)
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(src_gray)
    #顔検出範囲を表示
    for x, y, w, h in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = src[y: y + h, x: x + w]
        face_gray = src_gray[y: y + h, x: x + w]
    #書き出し
    cv2.imwrite("./output_frame_images/" + filename, src)

#モザイク
def mosaic(filename):

    face_cascade_path = 'haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    src = cv2.imread("./upload_images/" + filename)
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(src_gray)

    ratio = 0.05

    for x, y, w, h in faces:
        small = cv2.resize(src[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        src[y: y + h, x: x + w] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    
    cv2.imwrite("./output_mosaic_images/" + filename, src)

class ChangeHandler(FileSystemEventHandler):
 
    #ファイル・フォルダ作成
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #確認の為（デバッグ用）
        print('%sを作成しました。' % filename)

        #ファイルを反映するのに時間かかるのでsleep１をして遅らせて処理する(無理やり)
        time.sleep(1)
        #グレースケールの関数呼び出し
        gray(filename)
        #cannyの関数呼び出し
        canny(filename)
        #face_detectionの関数呼び出し
        face_detection(filename)
        #mosaicの関数呼び出し
        mosaic(filename)
        
        #デバッグ用
        # print("filename:", filename)
        # print("filepath:", filepath)
        # print("./upload_images/" + filename)

 
    #ファイル・フォルダ更新
    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)

        #画像置くと生成されるやつは無視して関数を閉じる
        if ".DS_Store" == filename:
            return
        
        #upload_imagesの中身が空になったときの処理
        if "upload_images" == filename:
            print(f"{filename}の中身が空になりました。")
            return
        
        #確認の為（デバッグ用）
        print('%sを更新しました。' % filename)
        
        #ファイルを反映するのに時間かかるのでsleep１をして遅らせて処理する(無理やり)
        time.sleep(1)

        #もしエラーが出たときの対応
        try:
            #ファイルの安否確認(更新のときはファイルが消えても作動してしまうため)
            if os.path.exists("./upload_images/" + filename):
                #グレースケールの関数呼び出し
                gray(filename)
                #cannyの関数呼び出し
                canny(filename)
                #face_detectionの関数呼び出し
                face_detection(filename)
                #mosaicの関数呼び出し
                mosaic(filename)
            else:
                print('ファイルが存在しませんでした。')
        except:
            print('正常に動作しませんでした。')
 
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