from ftplib import FTP
import socket
import sys
import urllib.request



"""
This function download file from website using http protocol.
"""
def httpDownload(website, path, fileName):
    url = website + path + fileName

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception:
        print("Socket creation failed\n")
        return 0
        
    if len(website) <= 7:
        raise Exception("Invalid website address\n")
        return 0
    
    host = website[7:]
    port = 80
    try:
        remote_ip = socket.gethostbyname( host )
        s.connect((remote_ip , port))
    except Exception:
        print("Building connection failed\n")
        return 0

    urllib.request.urlretrieve(url, fileName)
 
    s.close()


"""
This function download file from website using ftp protocol.
"""
def ftpDownload(website, path, fileName):
    try:
        ftp = FTP(website)
    except Exception:
        print("The website address is wrong\n")
        return 0

    try:    
        ftp.login(user='anonymous', passwd='coms3200@uq.edu.au')
    except Exception:
        print("Can not login, username or password is wrong\n")
        return 0
        
    try:
        ftp.cwd(path)
    except Exception:
        print("The path is wrong.\n")
        return 0
        
    ftp.set_pasv(True)

    try:
        filename = fileName
        localfile = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    except Exception:
        print("The filename is wrong\n")
        return 0
    
    ftp.quit()
    localfile.close()




if __name__ == '__main__':
    protocol = input('Choose protocol, http or ftp\n')
    
    if protocol == "http":
        httpDownload("http://eait.uqstatic.net", "/", "up")
        
    elif protocol == "ftp":
        ftpDownload("ftp.uq.edu.au", "/", "welcome.msg")
        
    else:
        print("Invalid input, enter either 'http' or 'ftp'\n")
        raise Exception("Invalid input, enter either 'http' or 'ftp'\n")
        return 0
        
        
        

