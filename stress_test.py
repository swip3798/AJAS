from multiprocessing import Pool 
import requests
import json

def tester(number):
    res = requests.get("http://localhost:8080/hello?hello=" + str(number))
    data = json.loads(res.text)
    print(number, data["hi"] == number)


if __name__ == "__main__":
    pool = Pool(30)
    pool.map(tester, [ i for i in range(1200) ])
    