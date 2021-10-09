import urllib.parse


hello = "こんちは、こんちは"  # 文字列
print(hello)

tweet = "https://twitter.com/intent/tweet?text={}"
hello_quote = urllib.parse.quote(hello)  # URLエンコード (パーセントエンコード)
print(tweet.format(hello_quote))


hello_byte = hello.encode()  # バイト列
print(hello_byte)

hello_byte_quote = urllib.parse.quote(hello_byte)
print(tweet.format(hello_byte_quote))  # URLエンコード (パーセントエンコード)


hogehoge = "ほげほげ"
print(hogehoge)

hogehoge_shiftjs = urllib.parse.quote(hogehoge, encoding='shift-jis')  # shift-jisでエンコード
print(hogehoge_shiftjs)
