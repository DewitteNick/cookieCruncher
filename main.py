import snmp
import time



def getPlcStartTime():
    upTime = snmp.getRunningTime()
    currentTime = getCurrentGMT()
    startTime = currentTime - upTime
    plcErrorCorrection = 85945
    return startTime + plcErrorCorrection

def getCurrentGMT():
    return int(time.time() // 1)








def main():
    print(getPlcStartTime())


if __name__ == "__main__":
    main()