'''
Created on Mar 17, 2013

@author: marsliutao
'''
import os
import md5
import random
import types

#from infrastructure.common.logger.LoggerFactory import LoggerFactory
#logger = LoggerFactory.getLogger(__name__)

class FileUtil(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    @staticmethod
    def readContent(file_path):
        print(file_path)
        config_file = file(file_path, 'r')

        file_content = ""
        file_lines = config_file.readlines();
        for line in file_lines :
            file_content = file_content + line.strip()
        config_file.close()
        return file_content
    
    @staticmethod
    def writeContent(file_path, content):
        dir_path = os.path.dirname(file_path)
        os.system("mkdir -p %s" % dir_path)
        config_file = file(file_path, 'w')
        config_file.write(content)
        config_file.close()

    @staticmethod
    def appendContent(file_path,content):
        dir_path = os.path.dirname(file_path)
        os.system("mkdir -p %s" % dir_path)
        config_file = open(file_path, 'a')
        config_file.write(content)
        config_file.close()

    @staticmethod
    def replaceFileContent(filePath, replaceToken, replaceValue):
        #logger.info("Replace %s to %s in conf file %s" % (replaceToken, replaceValue, filePath))
        content = FileUtil.readContent(filePath)
        content = content.replace(replaceToken, replaceValue)
        FileUtil.writeContent(filePath, content)
        pass
    
    #get md5 of a input string
    @staticmethod
    def getStringMD5(str):
        m = md5.new()
        m.update(str)
        return m.hexdigest()
    
    
    #get md5 of a input file
    @staticmethod
    def getFileMD5(file):
        fileinfo = os.stat(file)
        if int(fileinfo.st_size)/(1024*1024)>1000:
            return FileUtil.getBigFileMD5(file)
        m = md5.new()
        f = open(file,'rb')
        m.update(f.read())
        f.close()
        return m.hexdigest()
    
    
    #get md5 of a input bigfile
    @staticmethod
    def getBigFileMD5(file):
        m = md5.new()
        f = open(file,'rb')
        maxbuf = 8192
    
    
        while 1:
            buf = f.read(maxbuf)
            if not buf:
                break
            m.update(buf)
    
    
        f.close()
        return m.hexdigest()
    
    
    #get md5 of a input folder.
    #result will be output to the specified file
    @staticmethod
    def getBetchFilesMD5(dir,outMD5File):
        strDirEncodeType=type(dir)
        
        if(strDirEncodeType == types.UnicodeType) :
            strDir = str(dir)
        else :
            strDir=dir
        outfile = open(outMD5File,'w')
        for root ,subdirs, files in os.walk(strDir):
            for file in files:
                filefullpath = os.path.join(root,file)
                md5 = FileUtil.getFileMD5(filefullpath)
                outfile.write(file+'   md5:   '+md5+"\n")
        outfile.close()
    
    @staticmethod
    def getDirsComparison(leftdir, rightdir):
        dir_comparison = False
        #To Do: add parameter verification, if dir not exist then throw Exception
        
        if leftdir.endswith("/") :
            size = len(leftdir)
            dir_path = leftdir[0:size-1]
        else :
            dir_path = leftdir            
        dirname = os.path.basename(dir_path)
        
        random_num = random.uniform(0, 20)
        left_md5_file  = "/tmp/%s-%s-left.md5" % (dirname, random_num)
        right_md5_file = "/tmp/%s-%s-right.md5" % (dirname, random_num)
        
        if os.path.isfile(left_md5_file):
            os.remove(left_md5_file)
        
        if os.path.isfile(right_md5_file):
            os.remove(right_md5_file)

        FileUtil.getBetchFilesMD5(leftdir, left_md5_file)
        FileUtil.getBetchFilesMD5(rightdir, right_md5_file)
        
        #sort the content in left file and right file
        sorted_left_md5_file = "%s.sort" % left_md5_file
        sorted_right_md5_file = "%s.sort" % right_md5_file
        
        sort_left_file_cmd = "cat %s | sort > %s" % (left_md5_file, sorted_left_md5_file)
        sort_right_file_cmd = "cat %s | sort > %s" % (right_md5_file, sorted_right_md5_file)
        os.system(sort_left_file_cmd)
        os.system(sort_right_file_cmd)
        
        left_md5  = open(sorted_left_md5_file, "r")
        right_md5 = open(sorted_right_md5_file, "r")
        
        try:
            left_md5_contents = left_md5.read()
            right_md5_contents = right_md5.read()
            
            left_md5_contents = left_md5_contents.strip()
            right_md5_contents = right_md5_contents.strip()
            if left_md5_contents == right_md5_contents:
                dir_comparison = True
        except Exception, e:
            print("exception")
            #logger.error("File I/O exception!" + str(e))
        finally:
            left_md5.close()
            right_md5.close()
            #logger.info("left_md5_file=%s" % left_md5_file)
            #logger.info("right_md5_file=%s" % right_md5_file)
            #os.remove(left_md5_file)
            #os.remove(right_md5_file)
        
        return dir_comparison  
    
        
