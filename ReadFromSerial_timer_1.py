#! /usr/bin/python

#Import ed inizializzazione

import os
ReadFromSerial_timer=os.environ.get('PYTHONSTARTUP')
if ReadFromSerial_timer and os.path.isfile(ReadFromSerial_timer):
    execfile(ReadFromSerial_timer)

from temboo.Library.Google.Spreadsheets import AppendRow
from temboo.core.session import TembooSession
from temboo.core.exception  import TembooError
from temboo.core.exception  import TembooHTTPError
import serial
import time
import subprocess
import threading
import sys
import string



s=0
s1=0
c=0
d=0
count=0
#comando che riavvia la raspberry
command= "/usr/bin/sudo /sbin/shutdown -r now"


#Thread Timer che verifica se la sessione temboo dura troppo. In caso RIAVVIO.

def timer_Temboo():
       print "Riavvio tutto...CIAO!" 
       p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
       output= p.communicate()[0]
       print output
       
#Verifico presenza di Arduino sulla porta seriale
try:
    ser= serial.Serial('/dev/ttyACM0',9600)
except serial.SerialException:
    print "Arduinoooo... dove sei finito???"
    s=s+1
    if s==5:
        p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
        output= p.communicate()[0]
        print output

#LOOP-Leggo messaggio di Arduino e lo invio
while True:
    #data e ora correnti
    tempo=time.strftime("%H:%M:%S")
    data=time.strftime("%d/%m/%Y")
    try:
        read_serial=ser.readline()
    except (serial.SerialException, OSError, NameError):
        print "Arduinoooo... dove sei finito???"
        s1=s1+1
        if s1==5:
            p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
            output= p.communicate()[0]
            print output
        
    

    try:
        print read_serial
    except NameError:
        print "Ardunoooo... se non ci sei non leggo niente!"
        #p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
        #output= p.communicate()[0]
        #print output
        
    print data, tempo
    oggi=string.split(data,"/")
    
    try:    
        StringaDati=string.split(read_serial,",")
    except NameError:
        print "Stringa dati vuota" 
        StringaDati=string.split("0 0 0 0 0 0 0 0 0 0 0")
    
    Informazione="MTR"+","+ data+","+tempo+","+StringaDati[3]+","+StringaDati[4]+","+StringaDati[5]+","+StringaDati[6]+","+StringaDati[7]+","+StringaDati[8]+","+StringaDati[9]+","+StringaDati[10]+","+StringaDati[11]+","+oggi[0]
    # Create a session with your Temboo account details
    t=threading.Timer(120.0, timer_Temboo)
    t.start()
    print "Inizio sessione, timer avviato..."
    session = TembooSession("sperimentaleggp", "myFirstApp", "1akJ2G8w0DhM6TDCyKPFGwXvFgRveiZ6")

    # Instantiate the Choreo
    appendRowChoreo = AppendRow(session)

    # Get an InputSet object for the Choreo
    appendRowInputs = appendRowChoreo.new_input_set()

    # Set the Choreo inputs
    appendRowInputs.set_RowData(Informazione)
    appendRowInputs.set_SpreadsheetTitle("ArduinoLog")
    appendRowInputs.set_RefreshToken("1/aLxhlVr07QMDnS9qYtcMWbAw7KngqO_TIZCbja2Bi88")
    appendRowInputs.set_ClientSecret("ccoAJeO8Yuf33S25AvWocb7b")
    appendRowInputs.set_ClientID("374932964420-dmt8ularkt07p1e6jho1r8ahrsqv32d9.apps.googleusercontent.com")

    count=count+1
    print "Sessione numero: "      
    print count
    # Execute the Choreo
    try:
        print "Eseguo Choreo..."
        appendRowResults = appendRowChoreo.execute_with_results(appendRowInputs)
       
    except (TembooError, TembooHTTPError):
        print 'Oooops!'
        d=d+1
        if d==5:
            p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
            output= p.communicate()[0]
            print output
       
    try:
        # Print the Choreo outputs
        print("NewAccessToken: " + appendRowResults.get_NewAccessToken())
        print("Response: " + appendRowResults.get_Response())
    except NameError:
        print "Temboo non si capisce piu..."
        c=c+1
        if c==5:
            p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
            output= p.communicate()[0]
            print output
    t.cancel()
    print "OK! Timer fermato!"    
