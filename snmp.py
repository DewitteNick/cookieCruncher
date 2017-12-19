import pip
try:
    from pysnmp.hlapi import *
except Exception as e:
    print("installing required modules")
    pip.main(['install', 'pysnmp'])



def getRunningTime():
    engine = SnmpEngine()
    authData = CommunityData('public')
    transportTarget = UdpTransportTarget(('10.10.36.224', 161)) # TODO request IP address
    contextData = ContextData()
    objectType = ObjectType(ObjectIdentity("SNMPv2-MIB", "sysUpTime", 0))

    g = getCmd(engine, authData, transportTarget, contextData, objectType)
    propertyUptime = str(next(g)[-1][-1])  # time in 1/100 s
    uptime = int(str.split(propertyUptime, ' ')[-1])
    uptime = int(uptime // 100)

    return uptime