import unittest
import wencai as wc

class TestWenCai(unittest.TestCase):

    def test_get_scrape_transaction(self):
        r = wc.get_scrape_transaction('跳空高开,平台突破,非涨停,股价大于ma120,ma30ma120ma250上移,股价大于前30日最高价,非银行版块')
        print(r)

    def test_get_strategy(self):
        r = wc.get_strategy('非银行版块')
        print(r)

    def test_get_scrape_report(self):
        r=  wc.get_scrape_report('跳空高开,平台突破,非涨停,股价大于ma120,ma30ma120ma250上移,股价大于前30日最高价,非银行版块')
        print(r)

if __name__ == '__main__':
    unittest.main()