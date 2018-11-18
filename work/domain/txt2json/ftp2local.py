from ftplib import FTP
def getfile():
    ftp=FTP()
    timeout=30
    port =21
    ftp.connect("192.168.1.222",port,timeout)
    ftp.login()
    ftp.cwd('cds/ftp/cnc-up/')
    filesname=ftp.nlst()
    httpfile='feixiang_pic_domain_'
    demandfile='feixiang_vod1_domain_'
    livefile='feixiang_vod2_domain_'
    for filename in filesname:
        if "feixiang_pic_domain_" in filename:
            if filename > httpfile:
                httpfile=filename
        if 'feixiang_vod1_domain_' in filename:
            if filename > demandfile:
                demandfile=filename
        if 'feixiang_vod2_domain_' in filename:
            if filename > livefile:
                livefile=filename
        else:
            pass
    print (httpfile,demandfile,livefile)
    bufsize=1024
    ftp.retrbinary("RETR " + httpfile , open(httpfile,"wb").write , bufsize)
    ftp.retrbinary("RETR " + demandfile , open(demandfile,"wb").write , bufsize)
    ftp.retrbinary("RETR " + livefile , open(livefile,"wb").write , bufsize)
    ftp.quit()
    return (httpfile,demandfile,livefile)

if __name__=="__main__":
    getfile()
