import snmp
import time
import math


def getPlcStartTime():
    upTime = snmp.getRunningTime()
    currentTime = getCurrentGMT()
    startTime = currentTime - upTime
    plcErrorCorrection = 85945
    return startTime + plcErrorCorrection

def getCurrentGMT():
    # return int(time.time() // 1)
    return int(round(time.time(), 0))


def getPlcStartTimeAccurate(precision=10):  # PLC may give a small delay sometimes, multiple querries subdue this effect
    totalResult = 0
    for i in range(precision):
        totalResult += getPlcStartTime()
    return int(round(totalResult / precision))





def main():
    print("quick estimate:", getPlcStartTime())
    print("Acurate calculation:", getPlcStartTimeAccurate(10))


if __name__ == "__main__":
    main()