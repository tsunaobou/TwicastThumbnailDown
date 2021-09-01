# TwicastThumbnailDown
Twitcasting thumbnail downloader.   
ツイキャスのサムネをダウンロードできます。

# How to Use
まずはじめに外部ライブラリをインストール
``` 
pip install pytwitcasting 
```
次に https://twitcasting.tv/developernewapp.php にアクセスし、 
Create New Appsからアプリを作成。   
(コールバックURLは適当でいい)   
そして発行されたAppsをクリックし、出てきたDetailタブの```ClientID```と```ClientSecret```をメモする。   
最後にこのリポジトリを```git clone```し、getthumb.pyに書き加える。   
あとは実行して指示に従えばダウンロードできます。