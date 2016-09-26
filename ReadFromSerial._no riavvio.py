from temboo.Library.Google.Spreadsheets import AppendRow
from temboo.core.session import TembooSession
from temboo.core.exception  import TembooError
from temboo.core.exception  import TembooHTTPError
import serial
import time
import subprocess


s=0
c=0
#command= "/usr/bin/sudo /sbin/shutdown -r now"


try:
    ser= serial.Serial('/dev/ttyACM0',9600)
except serial.SerialException:
    print "Arduinoooo... dove sei finito???"
    #s=s+1
    #if s==5:
    #    p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
     #   output= p.communicate()[0]
     #   print output

#s= [0,1]
while True:
    try:
        read_serial=ser.readline()
    except (serial.SerialException, OSError, NameError):
        print "Arduinoooo... dove sei finito???"
      #  s=s+1
       # if s==5:
      #      p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
       #     output= p.communicate()[0]
       #     print output

        
    #data e ora correnti
    tempo=time.strftime("%H:%M:%S")
    data=time.strftime("%d/%m/%Y")
    try:
        print read_serial
    except NameError:
        print "Ardunoooo... se non ci sei non leggo niente!"
        #p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
        #output= p.communicate()[0]
        #print output
        
    print data, tempo
    #stringa dati
    #dati=macchina+","+data+","+tempo+","+read_serial+","+data+tempo
    
    # Create a session with your Temboo account details
    session = TembooSession("sperimentaleggp", "myFirstApp", "1akJ2G8w0DhM6TDCyKPFGwXvFgRveiZ6")

    # Instantiate the Choreo
    appendRowChoreo = AppendRow(session)

    # Get an InputSet object for the Choreo
    appendRowInputs = appendRowChoreo.new_input_set()

    # Set the Choreo inputs
    appendRowInputs.set_RowData("DueBerry,20/7/2016,8:4:46,0,26.00,41.75,3,46.00, , ,0.00")
    appendRowInputs.set_SpreadsheetTitle("ArduinoLog")
    appendRowInputs.set_RefreshToken("1/aLxhlVr07QMDnS9qYtcMWbAw7KngqO_TIZCbja2Bi88")
    appendRowInputs.set_ClientSecret("ccoAJeO8Yuf33S25AvWocb7b")
    appendRowInputs.set_ClientID("374932964420-dmt8ularkt07p1e6jho1r8ahrsqv32d9.apps.googleusercontent.com")

    # Execute the Choreo
    try:
        appendRowResults = appendRowChoreo.execute_with_results(appendRowInputs)
    except (TembooError, TembooHTTPError):
        print 'Oooops!'
    try:
        # Print the Choreo outputs
        print("NewAccessToken: " + appendRowResults.get_NewAccessToken())
        print("Response: " + appendRowResults.get_Response())
    except NameError:
        print "Temboo non si capisce piu..."
       # c=c+1
       # if c==5:
         #   p=subprocess.Popen(command.split(),stdout=subprocess.PIPE)
         #   output= p.communicate()[0]
         #   print output
