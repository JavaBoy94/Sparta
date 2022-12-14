from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.k3kqx9z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    # print(sample_receive)  #클라로부터 서버가 데이터를 잘 받았는지 확인용 (클라에서 console.log역할)
    doc = {                           # DB에 저장할 데이터 양식
        'name':name_receive,
        'address':address_receive,
        'size':size_receive
    }

    db.mars.insert_one(doc)             #DB에 데이터 저장

    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list = list(db.mars.find({}, {'_id': False}))       #DB에 저장된 데이터 불러오기
    return jsonify({'orders': order_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)