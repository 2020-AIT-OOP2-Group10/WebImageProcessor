# WebImageProcessor
OOP2第11回による演習用プロジェクト

# 内部ディレクトリ構造
    project_directory/
        ├ output_canny_images/
        |   └ (Canny filtered images)
        ├ output_frame_images/
        |   └ (Face detected images)
        ├ output_gray_images/
        |   └ (Grayscaled images)
        ├ output_mosaic_images/
        |   └ (Mosaicized images)
        ├ static/
        ├ templates/
        |   ├ filelist.html
        |   └ index.html
        ├ upload_images/
        |   └ (Uploaded images)
        ├ image_process.py
        ├ README.md
        └ web.py

# 担当者
Web分野

- Flaskによるルーティング
- 画像のアップロードおよび保存
- 画像一覧ページ

## 画像アップロードページ

k19051

## 画像一覧ページ

KawaiKohsuke
***
画像処理分野

- WatchDogによるディレクトリの監視
- 画像処理
- 処理した画像を保存

## Cannyフィルタリング&WatchDog

EveSquare

## グレースケール

LongMine

# ライブラリのバージョン
watchdog=0.10.4
opencv-python=4.4.0.44
