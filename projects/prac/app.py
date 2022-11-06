from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')    #해당 url에 대한 요청시 서버에서 응답할(보내줄) 동작(데이터)
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET']) #'/test'에 대해 GET 요청이 들어올 시 응답할 동작
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)            # 터미널에 '봄날은 간다'가 출력됨
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST']) #'/test'에 대해 POST 요청이 들어올 시 응답할 동작
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '요청을 잘 받았어요'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)