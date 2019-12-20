''' 
Simple logging wrapper
@author: TheBdouilleur
@license: Free licensed
http://thebdouilleur.github.io
"c:\\Users\\pmhue\\Dropbox\\PythonScripts\\Typer\\main.log"
'''
from os import path
import datetime
date = str(datetime.date.today().strftime("%B %d, %Y"))
time = str(datetime.datetime.now().time())
startText = 3*'\n' +'------------------------------------------------\n' + date + ', at ' + time +', in typr.py:'
logPath = path.dirname(__file__)+'/main.log' #<-- absolute path to the log file
logPath = logPath.replace("/", "\\\\")
def log_start():
    print("Logs can be found at:"+logPath)
    log = open(logPath,"a")
    log.write("\n"+startText+"\n")
    log.close()
def log_exception(e):
    e = e
    log = open(logPath,"a")
    log.write('\nError:\n'+str(e))
    log.close()
if __name__ == "__main__":
    log_start()
    try:
        print(5+'5') # Simple error to demonstrate program
    except Exception as e:
        log_exception(e)