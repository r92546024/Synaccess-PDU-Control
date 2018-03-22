# Synaccess-PDU-Control
For Power Distribution Unit , the script can control Power ON ,Power OFF or get voltage or temperature


    from ControlDUT import  *

    PDU = ControlPDU()
    PDU.PDUIP = '192.168.1.100'  #PDU IP address for access
    
    PDU.PortPowerControl(1,1) # Port 1 ON
    PDU.PortPowerControl(1,0) # Port 1 OFF
    PDU.PortPowerControl(3,1) # Port 3 ON
    
    PDU.AllPortPowerControl(1) # All Port ON
    PDU.AllPortPowerControl(0) # All Port OFF
    
    
