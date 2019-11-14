# acmtrans
 This is a net spider program by Python to collect a list of ACM transaction papers.

This current version only support scraping paper information (e.g., title, authors, detail, doilink) from the [ACM journal website](https://dlnext.acm.org/journals).
You can get either *.txt* or *.json* files as the results.


Steps:
1. Install the package *`acmtrans`*: 

    *`pip install acmtrans==0.2`*

2. Enter python environment and import *`AcmTransSpider`* library:

    *`from acmtrans.Acmtrans import AcmTransSpider`*

3. Instantiate a spider class by providing a start url and the data store type:

    *`acntrans_spider = AcmTransSpider("https://dlnext.acm.org/toc/tist/2010/1/1", "json")`*
    
4. Run the spider:

    *`acmtrans_spider.acmtrans_spider_run()`*
    
After running the spider, you will get a file containing all papers information from that specific journal. 
This file is named by the abbreviation of the journal name. For example, the journal "ACM Transactions on 
Modeling and Performance Evaluation of Computing Systems (TOMPECS)" with the start url 
"https://dlnext.acm.org/toc/tompecs/2016/1/1" and data type "json", we will get a file *`tompecs.json`*.
 
Thank you for using this tool!
