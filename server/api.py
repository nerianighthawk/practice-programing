from flask import Blueprint, request, jsonify


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/', methods=['POST'])
def check_age():
    print('check_age')
    # 以下の手順で実装すること
    # request body から name と date_of_birth を取得
    # date_of_birth から年齢を計算
    # 年齢が18歳未満の場合は data: 'NG' を返す
    # 年齢が18歳以上の場合は data: 'OK' を返す
    request_body = request.get_json()


# エラーのハンドリング
@api.errorhandler(400)
@api.errorhandler(404)
def error_handler(error):
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code
