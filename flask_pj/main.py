from flask import Flask, render_template, jsonify, request
import json
import firebase_admin
from firebase_admin import credentials, firestore
from db_01 import DBstorage as db
import model_train_04 as m_t

app = Flask(__name__)

mdltrnnobjecrcgn = m_t.MdlTrnnObjcRcgn()  # 클래스 객체 생성
mdltrnnobjecrcgn.showModelPrediction()  # 모델 보여줌

mdltrnnobjecrcgn.camera_exit()  # 카메라 종료


@app.route("/")
def index():
    return render_template("index.html")


# @app.route('/video')

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
