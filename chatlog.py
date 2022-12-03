
import threading
import os
from datetime import date

delayAmountInSeconds = 30.0


def writeLog():
  threading.Timer(delayAmountInSeconds, writeLog).start()
  
  today = date.today()
  auctionFileName = "auction"+today.strftime("%Y-%m-%d")+".txt"
  latestLog = open("latest.log", "r")
  for latestLogLine in latestLog:
    if "AUCTION" in latestLogLine:
      if not os.path.exists(auctionFileName):
        open(auctionFileName, 'w').close()
      auctionFile = open(auctionFileName, "r")
      foundInFile = False
      for autionFileLine in auctionFile:
        if latestLogLine in autionFileLine:
          foundInFile = True
      auctionFile.close()
      if foundInFile == False:
        auctionFile = open(auctionFileName, "a")
        auctionFile.write(latestLogLine)
        auctionFile.close()
      
  latestLog.close()

writeLog()
