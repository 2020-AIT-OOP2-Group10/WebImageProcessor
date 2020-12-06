import os
from flask import Flask, request, redirect, url_for,render_template
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory
# フォルダ内のファイル一覧を取得するglobモジュール
import glob

# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
app = Flask(__name__)

def allwed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/upload
@app.route('/upload',methods = ['POST'])
def upload():
    # ここでアップロードされた画像をupload_images/に保存する処理
    # ファイルがなかった場合の処理
    if 'file' not in request.files:
        print('ファイルがありません')
        return render_template('index.html')
    # データの取り出し
    file = request.files['file']
    # ファイル名がなかった時の処理
    if file.filename == '':
        print('ファイルがありません')
        return render_template('index.html')
    # ファイルのチェック
    if file and allwed_file(file.filename):
        # 危険な文字を削除（サニタイズ処理）
        filename = secure_filename(file.filename)
        # ファイルの保存
        file.save(os.path.join('./upload_images', filename))
        # アップロード後のページに転送
        return render_template('index.html')


# http://127.0.0.1:5000/upload_list
@app.route("/upload_list")
def upload_list():
    # フォルダ内のファイルの一覧を取得
    files = glob.glob("./upload_images/*")

    # ファイル一覧を回して、ファイルパスに"img"を結合
    for index, file in enumerate(files):
        files[index] = os.path.join("img", file)

    # ファイル一覧をJavaScriptに送る
    return render_template("filelist.html", files=files)


# http://127.0.0.1:5000/gray_list
@app.route("/gray_list")
def gray_list():
    files = glob.glob("./output_gray_images/*")

    return render_template("filelist.html", files=files)


# http://127.0.0.1:5000/canny_list
@app.route("/canny_list")
def canny_list():
    files = glob.glob("./output_canny_images/*")

    return render_template("filelist.html", files=files)


# http://127.0.0.1:5000/frame_list
@app.route("/frame_list")
def frame_list():
    files = glob.glob("./output_frame_images/*")

    return render_template("filelist.html", files=files)


# http://127.0.0.1:5000/mosaic_list
@app.route("/mosaic_list")
def mosaic_list():
    files = glob.glob("./output_mosaic_images/*")

    return render_template("filelist.html", files=files)


# http://127.0.0.1:5000/img/<path:dir_path>/<path:file_path>
@app.route("/img/<path:dir_path>/<path:file_path>")
def get_img_file(dir_path, file_path):
    return send_from_directory(dir_path, file_path)

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
