#TwicastThumbnailDownloader v1.00
from pytwitcasting.auth import TwitcastingApplicationBasis
from pytwitcasting.api import API
import math
import os
import urllib.request
import time
import sys

#認証
client_id = ''
client_secret = ''
app_basis = TwitcastingApplicationBasis(client_id=client_id,
                                        client_secret=client_secret)

api = API(application_basis=app_basis)

#とりあえずget
userid = input("ユーザーのidを入力してください>>")
dic = api._get_movies_by_user(user_id=userid,offset=0,limit=50)
#放送回数をカウント
count = dic["total_count"]

#何回リクエストする必要があるか計算
need_req = count/50
print(f"{count}枚のサムネイルが見つかりました")
time.sleep(1)

#リクエスト必要回数で分岐
#need_reqが0より大きく1以下の場合は一回のリクエストで済む
if 0<need_req<=1:
    req =1
#それより大きい場合、さらにその値が少数なら切り上げを行って代入
elif need_req>1 and isinstance(need_req,float):
    req = math.ceil(need_req)
#整数ならそのまま代入する
elif need_req>1 and isinstance(need_req,int):
    req = need_req
#DLできるサムネが一枚もなかった場合
else:
    print("ダウン可能なサムネがありませんでした")
    sys.exit()

#ダウンロード専用の関数を定義
def download(url,path):
    #まずフォルダを直下に作成して
    os.makedirs(path,exist_ok=True)
    try:
        with urllib.request.urlopen(url=url) as bin:
            filename = os.path.basename(bin.url)
            writedata = bin.read()
            with open(path+"/"+filename,mode='wb') as file:
                file.write(writedata)
            return filename
            

    except urllib.error.URLError as e:
        print(e)


#ここからリクエストとダウンロード
num = 1
ofst = 0
while num!=count: #写真枚数と周回用変数numが一致するまで続ける
    usedic = api._get_movies_by_user(user_id=userid,offset=ofst,limit=50)
    for i in range(50):
        thumburl = vars(usedic["movies"][i])["large_thumbnail"]
        downname = download(url=thumburl,path=userid)
        print(f"{downname}をダウンロード完了。{num}/{count}")
        #もし50回ループの途中で一致した場合はbreakして抜ける
        if num==count:
            break
        elif num!=count:
            num += 1
    #次処理のために増やす
    ofst += 50
print("すべてのダウンロードが完了しました。")