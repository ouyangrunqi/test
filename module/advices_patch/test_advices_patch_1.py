import os
import allure
import pytest
import re
import requests
import json


class TestAdvicesPatch():
    def __init__(self):
        # self.advices_patch_url = f'https://raas-dev.aqumon.com/raas-api/v1/app/advices/{adviceId}'
        self.headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJyYWFzX2FsbF9xYTFfYXBwMSIsInVzZXJfY29kZSI6ImF1dG8xMDAyIiwiZXhwIjoxNjMzMDE3NjAwfQ.Vjs_-XqhG4TgNj7_ufTFKBCQDeRk1JaLDeNGvA-VIGTlmD0ysWkarHO-ioHrnymgeKyVLiozFFgtXEBo4kv9QSf43Q2K6Vyc0WQAy2MxJYw85LZCxGripY-h_4L0E4gsl7JI-woj31KpS_G044_EyirBdeubu59oMMoYY9CBJzAX5hIB0gbZwyMSIZYk2W5ZSMlITM1APQBjWumvYIey9arBrcgdj5m31XRZwflx8rXuMriDl7Q1PEaV3AMezMF4m9o3nyz-Yuh4BG90W9LZYs2OAdJgzWv8Flf95L2qu6QpkOnAn__jdPE5NhKhezVTDXI7rWTH-eoJN9be3-9-mQ',
            'Host':'raas-dev.aqumon.com',
            'X-Api-Pid':'101'
        }
        self.raw = {
            "status":100
        }

    def get_adviceid(self):
        # adviceId只能确认一次
        with open('adviceId.txt') as f:
            adviceId = f.read().replace('\n', '')
        print(f'adviceId为：', adviceId)
        advices_patch_url = f'https://raas-dev.aqumon.com/raas-api/v1/app/advices/{adviceId}'
        res = requests.patch(advices_patch_url, headers=self.headers, json=self.raw)
        res_json = json.loads(res.text)
        # print(res_json)
        real_data = res_json['data']
        errors = res_json['errors']
        if real_data:
            taskId = real_data['taskId']
            serialNum = real_data['serialNum']
            print(f'taskId：', taskId)
            print(f'serialNum：', serialNum)
        elif errors[0]['code'] == 300012:
            print('\nmessage:The advice is confirmed.')




if __name__ == '__main__':
    # pytest.main(['-v', 'test_advices_path_1.py'])
    a = TestAdvicesPatch()
    a.get_adviceid()
