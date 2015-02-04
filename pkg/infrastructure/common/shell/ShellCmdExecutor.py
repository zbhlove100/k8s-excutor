'''
Created on Mar 16, 2013

@author: liutao
'''
import os
import subprocess
import datetime
import commands

from infrastructure.common.file.FileUtil import FileUtil
from infrastructure.common.systemenv.SystemEnv import SystemEnv
from domain.common.dao.impl.AutoOpsConfigDAO import AutoOpsConfigDAO

from infrastructure.common.lock.FileBasedLock import FileBasedLock
from infrastructure.common.logger.LoggerFactory import LoggerFactory
logger = LoggerFactory.getLogger(__name__)
                                 
class ShellCmdExecutor(object):
    '''
    classdocs
    '''
    DEFAULT_TIMEOUT = int(AutoOpsConfigDAO.getValue("default_kill_timeout"))
    
    def __init__(self):
        '''
        Constructor
        '''
    @staticmethod
    def debugEnv(scriptfile=None, env=None) :
        if scriptfile == None or env == None :
            return
    
        outfilepath = scriptfile + ".env"
        os.system("rm -f %s" % outfilepath)

        outfile = open(outfilepath, 'w')
    
        for k in env :
            e = "export %s=\"%s\"\n" % (k, env[k])
            logger.info(e)
            outfile.write(e)

        outfile.close()
    
    @staticmethod
    def execShellScript(cmd, ifPrint=None, timeout=None, env=None):
        if timeout == None :
            timeout = ShellCmdExecutor.DEFAULT_TIMEOUT
            pass
        
        if not cmd:
            return
        
        if not cmd.startswith("bash") :
            logger.debug("The cmd:%s not starts with 'bash'!" % cmd)
            return
        
        shellScriptCmd = None
        cmd = cmd.strip()
        scriptAbsPathAndParams = cmd.lstrip("bash").strip()
        
        elements = scriptAbsPathAndParams.split(" ")
        lenth = len(elements)
        if lenth == 1 :  #no params
            scriptAbsPath = elements[0]
            scriptFileName = os.path.basename(scriptAbsPath)
            scriptDirName = os.path.dirname(scriptAbsPath)
            shellScriptCmd = "cd %s; bash %s" % (scriptDirName, scriptFileName)
        else : #script with params
            params = ""
            scriptAbsPath = elements[0]
            scriptFileName = os.path.basename(scriptAbsPath)
            scriptDirName = os.path.dirname(scriptAbsPath)
            for i in range(1, lenth):
                if elements[i] != '' :
                    params += elements[i]
                    params += " "
                pass
            params = params.strip()
            shellScriptCmd = "cd %s; bash %s %s" % (scriptDirName, scriptFileName, params)
            pass
        
        #write cmd to a temp file in order to support multiple shell commands execution
        msg = 'Executing cmd with timeout(timeout=%s s): %s' % (timeout, shellScriptCmd)
        logger.debug(msg)
        
        strTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        strUUID = commands.getoutput('uuidgen')
        bashFileName = "bashfile-%s-%s.sh" % (strTime, strUUID)
        bashFilePath = "/tmp/%s" % bashFileName
        FileUtil.writeContent(bashFilePath, shellScriptCmd)
        bash_cmd = "bash %s" % bashFilePath
        output = None
        exitcode = -1
        
        try :
            output, exitcode = ShellCmdExecutor.execCmdWithKillTimeout(bash_cmd, ifPrint=ifPrint, kill_timeout=timeout, env=env)
            if exitcode != 0 :
                logger.error("otuput=%s" % output)
                logger.error("exitcode=%s" % exitcode)
                pass
            pass
        except Exception, e:
            logger.error("Write content exception:" + str(e))
        finally:
            if output != None and "[ERROR] [TIMEOUT]" in output :
                logger.error("TIMEOUT when execute cmd:%s" % shellScriptCmd)
                pass
            os.system("rm -rf %s" % bashFilePath)
        return (output, exitcode)

    @staticmethod
    def execCmd(cmd, ifPrint=None, exitcodeSwitch=None, timeout=None, env=None):
        if timeout == None :
            timeout = ShellCmdExecutor.DEFAULT_TIMEOUT
            pass
        
        if exitcodeSwitch == None:
            exitcodeSwitch = False
            pass
        
        if not cmd:
            return
        #write cmd to a temp file in order to support multiple shell commands execution
        msg = 'Executing cmd with timeout(timeout=%s s): %s' % (timeout, cmd)
        logger.debug(msg)
        
        strTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        strUUID = commands.getoutput('uuidgen')
        bashFileName = "bashfile-%s-%s.sh" % (strTime, strUUID)
        bashFilePath = "/tmp/%s" % bashFileName
        FileUtil.writeContent(bashFilePath, cmd)
        bash_cmd = "bash %s" % bashFilePath
        output = None
        exitcode = -1
        
        try :
            output, exitcode = ShellCmdExecutor.execCmdWithKillTimeout(bash_cmd, ifPrint=ifPrint, kill_timeout=timeout, env=env)
            if exitcodeSwitch == True :
                if exitcode != 0 :
                    logger.error("otuput=%s" % output)
                    logger.error("exitcode=%s" % exitcode)
                    pass
                else :
                    logger.debug("otuput=%s" % output)
                    logger.debug("exitcode=%s" % exitcode)
                    pass
                pass
            pass
        except Exception, e:
            logger.error("Write content exception:" + str(e))
        finally:
            if output != None and "[ERROR] [TIMEOUT]" in output :
                logger.error("TIMEOUT when execute cmd:%s" % cmd)
                pass
            os.system("rm -rf %s" % bashFilePath)
#         logger.info(cmd)
        return (output, exitcode)
    
    #The type of env should be dict.
    @staticmethod
    def execCmdWithoutKillTimeout(cmd, ifPrint=None, env=None):
        if not cmd:
            return
        
        logger.info('Executing cmd without timeout : %s' % cmd)
        output = None
        error = None
        outputFile = None
        outputFilePath = ""
        try :
            strTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            strUUID = commands.getoutput('uuidgen')
            outputFileName = "output%s.%s.log" % (strTime, strUUID)
            outputFilePath = "/tmp/%s" % outputFileName
            logger.info("OutputFileName=%s" % outputFilePath)
            outputFile=open(outputFilePath, 'w')
            
            if env != None :
                try:
                    import inspect
                    import json
                    stack = inspect.stack()
                    the_class = stack[2][0].f_locals["self"].__class__.__name__
                    if not os.path.exists("/var/log/autoops_env.json"):
                        record_env = {the_class: env}
                        content = json.dumps(record_env, sort_keys=True, indent=4)
                    else:
                        content_data = json.load(file("/var/log/autoops_env.json"))
                        content_data[the_class] = env
                        content = json.dumps(content_data, sort_keys=True, indent=4)
                    FileUtil.writeContent("/var/log/autoops_env.json", content)
                except Exception as ex:
                    logger.error("Save parsed Env params Failed")
                    logger.error(ex)
                env = dict(os.environ.items() + env.items())
                pass
            p = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=outputFile, stderr=subprocess.PIPE, env=env)
            output, error = p.communicate()
            
            output = FileUtil.readContent(outputFilePath)
            
            if ifPrint == True :
                logger.info("cmd output=%s---" % output)
            elif ifPrint == False or ifPrint == None :
                pass
            
            if error!=None and error!="" :
                logger.error("cmd error=%s---" % error)
                pass
            
            if error!=None and error!="" and cmd.find(".sh") > -1:
                error = "SOE: " + str(error)
        except Exception, e :
            logger.error(e)
        finally:
            if outputFile!=None:
                outputFile.close()
#            os.system("rm -f %s" % outputFilePath)
            pass
        
        return output,error
    
    #The type of env should be dict.
    @staticmethod
    def execCmdWithKillTimeout(cmd, ifPrint=None, kill_timeout=600, env=None):
        if not cmd:
            return
        
        output = None
        outputFile = None
        exitcode = -1
        outputFilePath = ""
        content = ""
        try :
            if kill_timeout == None :
                kill_timeout = ShellCmdExecutor.DEFAULT_TIMEOUT
                pass
            strTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            strUUID = commands.getoutput('uuidgen')
            outputFileName = "output%s.%s.log" % (strTime, strUUID)
            
            ######################################
            cmd = cmd.strip()
            if cmd.startswith("bash") :
                scriptPath = cmd.strip().lstrip("bash").strip()
                content = FileUtil.readContent(scriptPath)
                #get script name
                content = content.strip()
                if content.startswith("bash") or content.startswith("sh") or content.startswith("python") or content.startswith("ruby"):
                    strCmd = content.strip()
                    elements = strCmd.split(" ")
                    scriptName = elements[1].split("/")[-1]
                    outputFileName = "%s-%s-%s.log" % (scriptName, strTime, strUUID)
                    pass
                elif content.startswith("./"):
                    pass
                pass
            ######################################
            outputDir = "/var/log/autoopsscriptslog"
            if not os.path.exists(outputDir) :
                os.system("mkdir -p %s" % outputDir)
                pass
            
            outputFilePath = "%s/%s" % (outputDir, outputFileName)
            logger.info("OutputFileName=%s" % outputFilePath)
            logger.info(content)
            outputFile=open(outputFilePath, 'w')
            
            current_dir = os.path.dirname(__file__)
            timeout3ScriptPath= "%s/timeout3.sh" % current_dir
            timeoutCmd = "bash %s -t %s -i 1 -d 1 %s" % (timeout3ScriptPath, kill_timeout, cmd)
            #logger.info("you can check the cmd %s logs @ %s if the cmd execution time is long" % (cmd, outputFilePath))
            if env != None :
                try:
                    import inspect
                    import json
                    stack = inspect.stack()
                    the_class = stack[2][0].f_locals["self"].__class__.__name__
                    if not os.path.exists("/var/log/autoops_env.json"):
                        record_env = {the_class: env}
                        content = json.dumps(record_env, sort_keys=True, indent=4)
                    else:
                        content_data = json.load(file("/var/log/autoops_env.json"))
                        content_data[the_class] = env
                        content = json.dumps(content_data, sort_keys=True, indent=4)
                    FileUtil.writeContent("/var/log/autoops_env.json", content)
                except Exception as ex:
                    logger.error("Save parsed Env params Failed")
                    logger.error(ex)

                env = dict(os.environ.items() + env.items())
                pass
            p = subprocess.Popen(timeoutCmd, shell=True, close_fds=True, stdout=outputFile, stderr=subprocess.STDOUT, env=env)
            #ToDo: start a thread to print the logs to log file
            output, error = p.communicate()
            exitcode = p.returncode
            
            output = FileUtil.readContent(outputFilePath)
            
            if ifPrint == True :
                logger.info("cmd output=%s---" % output)
                logger.info("The returncode is : %s" % exitcode)
                pass
            elif ifPrint == False or ifPrint == None :
                pass
        except Exception, e :
            logger.error(e)
        finally:
            if outputFile!=None:
                outputFile.close()
            
            if(exitcode==0) :
                stdoutFilePath = outputFilePath.rstrip(".log") + "-stdout.log"
                stderrFilePath = outputFilePath.rstrip(".log") + "-stderr.log"
                os.system("mv %s %s" % (outputFilePath, stdoutFilePath))
                os.system("touch %s" % stderrFilePath)
                #logger.info("exitcode is 0")
#                os.system("rm -f %s" % outputFilePath)
                logger.info("you can check the cmd output logs @ %s.The exitcode=%s." % (stdoutFilePath, exitcode))
                pass
            else :
                stdoutFilePath = outputFilePath.rstrip(".log") + "-stdout.log"
                stderrFilePath = outputFilePath.rstrip(".log") + "-stderr.log"
                os.system("mv %s %s" % (outputFilePath, stderrFilePath))
                os.system("touch %s" % stdoutFilePath)
                
                logger.error("you can check the cmd output logs @ %s.The exitcode=%s." % (stderrFilePath, exitcode))
                pass
            pass
        
        return (output, exitcode)
#1.Implement execute cmd with timeout, it will return the output including both stdout and stderr.
    

