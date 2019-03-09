#coding = utf-8

import os
import requests
def download(url):
    filename = "视频" + ".ts"
    download_path = os.getcwd() + "\download"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    all_content = requests.get(url).text  # 获取M3U8的文件内容
    file_line = all_content.split("\n")  # 读取文件里的每一行
    # 通过判断文件头来确定是否是M3U8文件
    if file_line[0] != "#EXTM3U":
        raise BaseException("非M3U8的链接")
    else:
        unknow = True  # 用来判断是否找到了下载的地址
        length = str(int((len(file_line)-6)/2))
        for index, line in enumerate(file_line):
            if "EXTINF" in line:
                unknow = False
                # 拼出ts片段的URL
                domain = url.rsplit("/", 1)[0]
                domain = domain[0:domain.rfind("//")]
                if(file_line[index + 1].find("/") == 0):
                    pd_url = domain + file_line[index + 1]
                else:
                    pd_url = url.rsplit("/", 1)[0] + "/" + file_line[index + 1]

                res = requests.get(pd_url)
                c_fule_name = str(file_line[index + 1]).split("/")[-1]
                with open(download_path + "\\" + filename, 'ab') as f:
                            print(c_fule_name+"-下载完成,共有"  + length+ "片段")
                            f.write(res.content)
                            f.flush()
        if unknow:
            raise BaseException("未找到对应的下载链接")
        else:
            print("全部下载完成")




if __name__ == '__main__':
    download("http://alhlsvodhls01.e.vhall.com//vhallrecord/349644211/20180819225448/record.m3u8")
    #http://alhlsvodhls01.e.vhall.com//vhallrecord/349644211/20180819225448/record.m3u8
    #http://hzresource.cdn.bcebos.com/hls/geruikldsl/hls.m3u8