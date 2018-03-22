
def GetParserPDUInfo(IP,pattern):
    # Using request - for Python 3.x
    # import re,request
    # url = 'http://%s/cmd.cgi?$A5' %IP
    # response = requests.post(url)
    # text = response.text

    # Using request - for Python 2.7
    import re,urllib
    url = 'http://admin:admin@%s/cmd.cgi?$A5' % IP
    response = urllib.urlopen(url)
    text = response.read()

    if pattern != 'all' :
        PaserResult = re.findall(pattern, text)
    else:
        PaserResult = text
    PaserResult = ''.join(PaserResult) #list covert string
    return str(PaserResult)


def Sendmail(content):
    # Import smtplib for the actual sending function
    import smtplib

    # Import the email modules we'll need
    from email.mime.text import MIMEText

    msg = MIMEText(  content  )

    From = 'xxx@xxx.com' #= the sender's email address
    To = 'xxx@xxx.com'  
    CC = 'xx@xxx.com' 
    msg['Subject'] = '[Warning]Temperature Monitor Report' 
    msg['From'] = From
    msg['To'] = To
    msg['CC'] = CC

    s = smtplib.SMTP('localhost')
    s.sendmail(From, To, msg.as_string())
    s.quit()


def main():
    import datetime
    now = datetime.datetime.now()
    currenttime = now.strftime("%Y-%m-%d %H:%M:%S")

    Rack ={}
    pattern = r'.+,[0-1]{8,16},\d+.\d+,\d+.\d+,(..)'

    Rack['PDU57']= str(GetParserPDUInfo('192.168.193.57' , pattern ))
    Rack['PDU67']= str(GetParserPDUInfo('192.168.193.67' , pattern ))
    Rack['PDU77']= str(GetParserPDUInfo('192.168.193.77' , pattern ))
    Rack['PDU87']= str(GetParserPDUInfo('192.168.193.87' , pattern ))
    Rack['PDU97']= str(GetParserPDUInfo('192.168.193.97' , pattern ))
    Rack['PDU107'] = str(GetParserPDUInfo('192.168.193.107', pattern ))
    Rack['PDU117'] = str(GetParserPDUInfo('192.168.193.117', pattern ))
    Rack['PDU127'] = str(GetParserPDUInfo('192.168.193.127', pattern ))
    Rack['PDU137'] = str(GetParserPDUInfo('192.168.193.137', pattern ))
    Rack['PDU147'] = str(GetParserPDUInfo('192.168.193.147', pattern ))
    Rack['PDU157'] = str(GetParserPDUInfo('192.168.193.157', pattern ))
    Rack['PDU167'] = str(GetParserPDUInfo('192.168.193.167', pattern ))
    Rack['PDU177'] = str(GetParserPDUInfo('192.168.193.177', pattern ))
    Rack['PDU187'] = str(GetParserPDUInfo('192.168.193.187', pattern ))
    Rack['PDU197'] = str(GetParserPDUInfo('192.168.193.197', pattern ))
    Rack['PDU207'] = str(GetParserPDUInfo('192.168.193.207', pattern ))
    Rack['PDU217'] = str(GetParserPDUInfo('192.168.193.217', pattern ))
    Rack['PDU227'] = str(GetParserPDUInfo('192.168.193.227', pattern ))

    Burnin1Map = 'Burnin Room 1 Map- Each Rack Temperature(deg C)\n' + \
              '|+++++++++++++++++++++++++++++++++++|' + '\n'\
              '|%s  %s    %s|'%('PDU87='+Rack['PDU87'],'PDU217='+Rack['PDU217'],'PDU157='+Rack['PDU157']) + '\n'\
              '|%s  %s    %s|'%('PDU77='+Rack['PDU77'],'PDU207='+Rack['PDU207'],'PDU147='+Rack['PDU147']) + '\n'\
              '|%s  %s    %s|'%('PDU67='+Rack['PDU67'],'PDU187='+Rack['PDU187'],'PDU127='+Rack['PDU127']) + '\n'\
              '|%s  %s    %s|'%('PDU57='+Rack['PDU57'],'PDU177='+Rack['PDU177'],'OutSide='+Rack['PDU117']) + '\n'\
              '|+++++++++++++++++++++++++++++++++++|' + '\n'

    Burnin2Map = 'Burnin Room 2 Map- Each Rack Temperature(deg C)\n' + \
              '|++++++++++++++|' + '\n'\
              '|    %s|'%('PDU137='+ Rack['PDU137']) + '\n'\
              '|    %s|'%('PDU107='+ Rack['PDU107']) + '\n'\
              '|    %s|'%('PDU 97=' + Rack['PDU97']) + '\n'\
              '|    %s|'%('PDU197='+ Rack['PDU197']) + '\n'\
              '|++++++++++++++|' + '\n'''


    Burnin1LiveRack=0
    Burnin1Avg=0
    Burnin2LiveRack=0
    Burnin2Avg=0
    for key, value in Rack.iteritems():
        if value != 'XX' :
            if key in ('PDU87','PDU77','PDU67','PDU57','PDU217','PDU207','PDU187','PDU177','PDU157','PDU147','PDU127','PDU117'):
                Burnin1LiveRack += 1
                Burnin1Avg += int(value)
            elif key in ('PDU137','PDU107','PDU97','PDU197'):
                Burnin2LiveRack += 1
                Burnin2Avg += int(value)

    Burnin1Avg = float(Burnin1Avg)/float(Burnin1LiveRack)
    Burnin2Avg = float(Burnin2Avg)/float(Burnin2LiveRack)


    AvgCriteriaDegC = 35
    EachRackCriteriaDegC = 38
    EachRackResult=''
    for key, value in Rack.iteritems():
        if value != 'XX' and int(value) > EachRackCriteriaDegC :
            EachRackResult = EachRackResult + str(key) + ','

    Content = "Hi all,\nPlease refer to the Temperature Monitor Report.\n" +\
              'When over the following Criteria, will send this warning mail.\n' +\
              '\n********************************************************' + \
              '\nTIME : ' + str(currenttime) + \
              '\nAvg Criteria(deg C) < %s'%AvgCriteriaDegC + \
              '\nAvg(deg C) = ' + str(Burnin1Avg) + '\nRoom2 Avg(deg C) = ' + str(Burnin2Avg) + \
              '\n\nEach Rack Criteria(deg C) < %s' % EachRackCriteriaDegC + \
              '\nRack Over Criteria : %s' % EachRackResult + \
              '\n********************************************************\n' + \
              '\n********************************************************\n' + \
              '[XX mean Sesnor is not installed]\n' + \
                Burnin1Map + '\n' + Burnin2Map+ '\n' + \
              '**********************************************************\n'

    if Burnin1Avg > AvgCriteriaDegC or Burnin2Avg > AvgCriteriaDegC or EachRackResult != '':
        Sendmail( Content )
        ShowOutput('Over Criteria , SendMail')

main()
