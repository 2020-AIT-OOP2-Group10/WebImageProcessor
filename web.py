from flask import Flask, request, render_template

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/upload
# メソッドでPOST指定してね
@app.route('/upload')
def upload():
    # k19051
    # ここでアップロードされた画像をupload_images/に保存する処理
    return render_template('index.html')


# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
