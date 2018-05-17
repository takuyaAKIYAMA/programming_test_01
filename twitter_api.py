# -*- coding: UTF-8 -*-

'''
TwitterAPIを利用した画像取得

@author: Takuya_AKIYAMA
'''

from requests_oauthlib import OAuth1Session
import json
import os
import urllib
import api_key_config

# OAuth認証
twitter = OAuth1Session(api_key_config.CONSUMER_KEY, api_key_config.CONSUMER_SECRET, api_key_config.ACCESS_TOKEN, api_key_config.ACCESS_TOKEN_SECRET)

# 画像保存先ディレクトリの作成
def make_dir(mkdir_name):
    if not os.path.isdir(mkdir_name):
        os.mkdir(mkdir_name)
    return mkdir_name

# 検索ワードの入ったツイートを取得
def get_target_tweet(ward):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {'q':ward,
              'count':100
          }
    req = twitter.get(url, params = params)
    return json.loads(req.text)

# 取得したツイートに画像がある場合、その画像を取得
def get_image(timeline, dir_name):
    global image
    global image_number
    image_number = 0
    check_image = []
    for tweet in timeline['statuses']:
        try:
            media_list = tweet['extended_entities']['media']
            for media in media_list:
                image = media['media_url']
                if image in check_image:
                    continue
                with open(dir_name + "/image" + str(image_number+1) + "_" +os.path.basename(image), 'wb') as f:
                    img = urllib.request.urlopen(image).read()
                    f.write(img)
                check_image.append(image)
                image_number += 1
                if image_number == 10:
                    break
        except KeyError:
            pass
        except:
            print("error")
        finally:
            if image_number == 10:
                break

if __name__ == '__main__':
    get_image(get_target_tweet("JustinBieber"), make_dir("test_dir"))
