from os import path
logPath = path.dirname(__file__)+'/main.log' #<-- absolute path to the log file
logPath = logPath.replace("/", "\\\\")
log = open(logPath, 'a')
print('writing')
log.write('hi')
print('finished writing')
print('closing')
log.close()
print('finished closing')