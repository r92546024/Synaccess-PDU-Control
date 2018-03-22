import sys,re,urllib,socket,time
import logging

module_logger = logging.getLogger('ControlPDU')


class ControlPDU(object):
    __PDUIP = None
    __NumberOfPort = None
    __DUTID = None
    __PDUFolder = None
    __NumberOfPort = None
    __JobFolderPath = None


    def __init__(self,IP=None):
        if __name__ == "__main__":
            from LogOutput import Setlogger
            self.logger = Setlogger(__name__, __file__+'.log' , logging.DEBUG)
        else:
            self.logger = logging.getLogger('ControlPDU')

        self.logger.debug('ControlPDU_Class __init__')
        if IP !=None:
            self.PDUIP=IP

    @property
    def PDUIP(self):
        return self.__PDUIP

    @PDUIP.setter
    def PDUIP(self, value):
        if self.CheckIPformat(value)==True:
            self.__PDUIP = value
            self.logger.info('PDUIP={}'.format(value))


    @property
    def NumberOfDUTPort(self):
        return self.__NumberOfPort

    @PDUIP.setter
    def NumberOfDUTPort(self, value):
        if self.RepresentsInt(value) == True :
            self.__NumberOfPort = int(value)
            self.logger.info('NumberOfDUTPort={}'.format(value))
        else:
            self.logger.error('please assign NumberOfDUTPort={} to integer'.format(self.__NumberOfPort))
            #print ('please assign NumberOfDUTPort={} to integer'.format(self.__NumberOfPort))

    @property
    def DUTID(self):
        return self.__DUTID

    @DUTID.setter
    def DUTID(self, value):
        if self.RepresentsInt(value) == True :
            self.__DUTID = int(value)
            self.logger.info('DUTID={}'.format(value))
        else:
            self.logger.error('please assign DUTID={} to integer'.format(self.__DUTID))
            #print ('please assign DUTID={} to integer'.format(self.__DUTID))

    @staticmethod
    def RepresentsInt(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def CheckIPformat(addr):
        import socket
        try:
            socket.inet_aton(addr)
            return True
        except socket.error:
            self.logger.warning('IP {} format error'.format(addr))
            return False

    @staticmethod
    def GetParserPDUInfo(IP, pattern):
        # Using request - for Python 3.x
        # import re,request
        # url = 'http://%s/cmd.cgi?$A5' %IP
        # response = requests.post(url)
        # text = response.text

        # Using urllib - for Python 2.7
        import re, urllib
        url = 'http://admin:admin@%s/cmd.cgi?$A5' % IP
        response = urllib.urlopen(url)
        text = response.read()

        if pattern != 'all':
            PaserResult = re.findall(pattern, text)
        else:
            PaserResult = text
        PaserResult = ''.join(PaserResult)  # list covert string

        return PaserResult

    def GetPDUStatusInfo(self):
        return self.GetParserPDUInfo(self.__PDUIP,'all')


    def PortPowerControl(self,portN,switch):
        if self.__PDUIP != None:
            import re, urllib, time
            url = 'http://admin:admin@{0}/cmd.cgi?$A3%20{1}%20{2}'.format(self.__PDUIP, portN, switch)

            PDURetryTimes = 3
            PDUResponse = ''
            PDUPortResult = ''
            Retry = 0

            try:
                while (Retry < PDURetryTimes and PDUResponse != '$A0' and PDUPortResult == ''):
                    response = urllib.urlopen(url)
                    time.sleep(1)
                    PDUResponse = response.read()

                    # print (ControlPDU.GetParserPDUInfo(self.__PDUIP, 'all'))
                    while PDUPortResult == switch:
                        PDUPortResult = ControlPDU.GetParserPDUInfo(self.__PDUIP, '.+,\d{%s}(\d)\d*,' % (portN - 1))
                        time.sleep(1)
                    Retry += 1
            except :
                self.logger.error('PDUIP {} is unstable connection, please reset PDU'.format(self.PDUIP))
        else:
            self.logger.error("PDUIP={0} , DUTID={1} , NumberOfDUTPort={2}".format(self.__PDUIP,self.__DUTID,self.__NumberOfPort))
            self.logger.error("Please Check if script already assign value by .PDUIP , .DUTID , .NumberOfDUTPort")


    def AllPortPowerControl (self, switch):
        if self.__PDUIP != None:
            import re, urllib, time
            url = 'http://admin:admin@{0}/cmd.cgi?$A7%20{1}'.format(self.__PDUIP, switch)

            PDURetryTimes = 3
            PDUResponse =''
            PDUPortResult = ''
            Retry = 0

            try:
                while (Retry < PDURetryTimes and PDUResponse != '$A0' and PDUPortResult == ''):
                    response = urllib.urlopen(url)
                    time.sleep(1)
                    PDUResponse = response.read()

                    # print (ControlPDU.GetParserPDUInfo(self.__PDUIP, 'all'))
                    while PDUPortResult == '':
                        if switch == 1:
                            PDUPortResult = ControlPDU.GetParserPDUInfo(self.__PDUIP, '.+,([1]{8,16}),')
                        elif switch == 0:
                            PDUPortResult = ControlPDU.GetParserPDUInfo(self.__PDUIP, '.+,([0]{8,16}),')
                        time.sleep(1)
                    Retry += 1
            except :
                self.logger.error('PDUIP {} is unstable connection, please reset PDU'.format(self.PDUIP) )

        else:
            self.logger.error("PDUIP={0} , DUTID={1} , NumberOfDUTPort={2}".format(self.__PDUIP, self.__DUTID,self.__NumberOfPort))
            self.logger.error("Please Check if script already assign value by .PDUIP , .DUTID , .NumberOfDUTPort")

    def PowerOn(self):
        if self.__NumberOfPort!=None and  self.__PDUIP!=None and self.__DUTID!=None :
            EndPort = self.DUTID*self.__NumberOfPort+1
            StarPort = EndPort - self.__NumberOfPort
            for i in range(StarPort,EndPort):
                self.logger.info( "PDUIP={0},DUTID={1},NumberOfDUTPort={2}".format(self.__PDUIP,self.__DUTID,self.__NumberOfPort) + ',PDUPort' +  str(i) + ' On')
                time.sleep(1)
                self.PortPowerControl(i, 1)
        else:
            self.logger.error("PDUIP={0} , DUTID={1} , NumberOfDUTPort={2}".format(self.__PDUIP,self.__DUTID,self.__NumberOfPort))
            self.logger.error("Please Check if script already assign value by .PDUIP , .DUTID , .NumberOfDUTPort")

    def PowerOff(self):
        if self.__NumberOfPort!=None and  self.__PDUIP!=None and self.__DUTID!=None :
            EndPort = self.DUTID*self.__NumberOfPort+1
            StarPort = EndPort - self.__NumberOfPort
            for i in range(StarPort,EndPort):
                self.logger.info( "PDUIP={0},DUTID={1},NumberOfDUTPort={2}".format(self.__PDUIP,self.__DUTID,self.__NumberOfPort) + ',PDUPort' +  str(i) + ' Off')
                time.sleep(1)
                self.PortPowerControl(i, 0)
        else:
            self.logger.error("PDUIP={0} , DUTID={1} , NumberOfDUTPort={2}".format(self.__PDUIP,self.__DUTID,self.__NumberOfPort))
            self.logger.error("Please Check if script already assign value by .PDUIP , .DUTID , .NumberOfDUTPort")



if __name__ == "__main__":
    from ControlDUT import  *

    PDU = ControlPDU()
    PDU.PDUIP = '192.168.1.100'
    PDU.DUTID= 1
    PDU.NumberOfDUTPort= 1
    PDU.PowerOff()
    PDU.PowerOn()

    print PDU.GetPDUStatusInfo()
    PDU.PortPowerControl(1, 0)
    PDU.PortPowerControl(1, 1)
    PDU.PortPowerControl(2, 0)
    PDU.PortPowerControl(2, 1)
    PDU.PortPowerControl(2, 0)
    PDU.PortPowerControl(2, 1)
    
    PDU.PortPowerControl(3, 0)
    PDU.PortPowerControl(3, 1)
    PDU.PortPowerControl(3, 0)
    PDU.PortPowerControl(3, 1)
    
    PDU.AllPortPowerControl(0)
    PDU.AllPortPowerControl(1)


