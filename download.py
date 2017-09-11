#!/bin/python3
import refrom urllib.request 
import urlopen
import os
def main(geo):   
# find the FTP address from [url=https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GEO]https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GEO[/url]
   response = urlopen("https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={}".format(geo))
    pattern = re.compile("<a href=\"(.*?)\">\(ftp\)</a>")
    # use wget from shell to download SRA data 
   ftp_address = re.search(pattern,response.read().decode('utf-8')).group(1)
    os.system(' wget -nd -r 1 -A *.sra ' + ftp_address)
 
if __name__ == '__main__':
    from sys import argv
    main(argv[1])
    """
    保存命名为SRR_downloader.py，在命令行里运行
python3 SRR_downloader.py GSE81916
简单说明：
用sys.argv从命令行中读取参数
用urllib.request向网页发起请求，获取response
用正则表达式(re)提取FTP地址
用os.system运行shell的命令""
