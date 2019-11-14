from acmtrans.Acmtrans import AcmTransSpider


if __name__ == '__main__':
    AcmTransSpider("https://dlnext.acm.org/toc/tompecs/2016/1/1", "json").acmtrans_spider_run()
