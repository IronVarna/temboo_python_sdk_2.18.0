from temboo.Library.Google.Spreadsheets import RetrieveRow
from temboo.core.session import TembooSession
from temboo.Library.Google.Spreadsheets import AppendRow
from temboo.Library.Yahoo.Weather import GetWeatherByAddress
import string
import time



while True:
  
  tempo=time.strftime("%H:%M:%S")
  oggi=time.strftime("%d/%m/%Y")
  
  if  tempo=="20:00:00":

    # Create a session with your Temboo account details
    session = TembooSession("sperimentaleggp", "myFirstApp", "1akJ2G8w0DhM6TDCyKPFGwXvFgRveiZ6")

    # Instantiate the Choreo
    retrieveRowChoreo = RetrieveRow(session)

    # Get an InputSet object for the Choreo
    retrieveRowInputs = retrieveRowChoreo.new_input_set()

    # Set the Choreo inputs
    retrieveRowInputs.set_WorksheetId("o5s758g")
    retrieveRowInputs.set_RefreshToken("1/aLxhlVr07QMDnS9qYtcMWbAw7KngqO_TIZCbja2Bi88")
    retrieveRowInputs.set_ClientSecret("ccoAJeO8Yuf33S25AvWocb7b")
    retrieveRowInputs.set_ClientID("374932964420-dmt8ularkt07p1e6jho1r8ahrsqv32d9.apps.googleusercontent.com")
    retrieveRowInputs.set_SpreadsheetKey("1KFdG-6_t5tKRXpSJ2Swxt7LlH5ydUYklCLHthJrxnxc")

    # Execute the Choreo
    retrieveRowResults = retrieveRowChoreo.execute_with_results(retrieveRowInputs)

    # Print the Choreo outputs
    print("RowData: " + retrieveRowResults.get_RowData())
    print("NewAccessToken: " + retrieveRowResults.get_NewAccessToken())

    a=retrieveRowResults.get_RowData()
    b=string.split(a,",")
    i=len(b)
    data_time_h_erba=string.split(b[0])

    if data_time_h_erba[0]==oggi and b[i-1]=="Yes":     

      media_h_erba=(float(b[2])+float(b[3])+float(b[4])+float(b[5])+float(b[6]))/5
      media_h_erba_str=str(media_h_erba)

    else:  
      # Create a session with your Temboo account details
      session = TembooSession("sperimentaleggp", "myFirstApp", "1akJ2G8w0DhM6TDCyKPFGwXvFgRveiZ6")

      # Instantiate the Choreo
      retrieveRowChoreo = RetrieveRow(session)

      # Get an InputSet object for the Choreo
      retrieveRowInputs = retrieveRowChoreo.new_input_set()

      # Set the Choreo inputs
      retrieveRowInputs.set_WorksheetId("od6")
      retrieveRowInputs.set_RefreshToken("1/aLxhlVr07QMDnS9qYtcMWbAw7KngqO_TIZCbja2Bi88")
      retrieveRowInputs.set_ClientSecret("ccoAJeO8Yuf33S25AvWocb7b")
      retrieveRowInputs.set_ClientID("374932964420-dmt8ularkt07p1e6jho1r8ahrsqv32d9.apps.googleusercontent.com")
      retrieveRowInputs.set_SpreadsheetKey("1UqmLnilDatyUZ0gsZyNeW_nFnAgdWW8ppIMJrPUhN2s")

      # Execute the Choreo
      retrieveRowResults = retrieveRowChoreo.execute_with_results(retrieveRowInputs)

      # Print the Choreo outputs
      print("RowData: " + retrieveRowResults.get_RowData())
      print("NewAccessToken: " + retrieveRowResults.get_NewAccessToken())

      a_1=retrieveRowResults.get_RowData()
      b_1=string.split(a_1,",")

      TabellaCrescitaErba_data=b_1[0]
      media_h_erba=(float(b_1[7]))
      media_h_erba_str=b_1[7]

    

    # Create a session with your Temboo account details
    session = TembooSession("sperimentaleggp", "myFirstApp", "1akJ2G8w0DhM6TDCyKPFGwXvFgRveiZ6")

    # Instantiate the Choreo
    getWeatherByAddressChoreo = GetWeatherByAddress(session)

    # Get an InputSet object for the Choreo
    getWeatherByAddressInputs = getWeatherByAddressChoreo.new_input_set()

    # Set the Choreo inputs
    getWeatherByAddressInputs.set_Address("Tranas")

    # Execute the Choreo
    getWeatherByAddressResults = getWeatherByAddressChoreo.execute_with_results(getWeatherByAddressInputs)

    # Print the Choreo outputs
    print("ConditionCode: " + getWeatherByAddressResults.get_ConditionCode())
    print("ConditionText: " + getWeatherByAddressResults.get_ConditionText())
    print("ForecastCode: " + getWeatherByAddressResults.get_ForecastCode())
    print("ForecastText: " + getWeatherByAddressResults.get_ForecastText())
    print("High: " + getWeatherByAddressResults.get_High())
    print("Humidity: " + getWeatherByAddressResults.get_Humidity())
    print("Low: " + getWeatherByAddressResults.get_Low())
    print("Pressure: " + getWeatherByAddressResults.get_Pressure())
    print("Temperature: " + getWeatherByAddressResults.get_Temperature())
    print("Visibility: " + getWeatherByAddressResults.get_Visibility())
    print("WOEID: " + getWeatherByAddressResults.get_WOEID())
    print("Response: " + getWeatherByAddressResults.get_Response())

    risposta=string.split(getWeatherByAddressResults.get_Response(),"&lt;BR /&gt;")


    domani=string.split(risposta[5],"High:")
    domani_temp=string.split(domani[1],"Low:")

    domani_1=string.split(risposta[6],"High:")
    domani_temp_1=string.split(domani_1[1],"Low:")

    domani_2=string.split(risposta[7],"High:")
    domani_temp_2=string.split(domani_2[1],"Low:")

    domani_3=string.split(risposta[8],"High:")
    domani_temp_3=string.split(domani_3[1],"Low:")

    domani_4=string.split(risposta[9],"High:")
    domani_temp_4=string.split(domani_4[1],"Low:")


    massima_oggi=getWeatherByAddressResults.get_High()
    minima_oggi=getWeatherByAddressResults.get_Low()

    t_media_oggi=int((((int(massima_oggi)+int(minima_oggi))/2)-32)/1.8)
    t_media_oggi_str=str(t_media_oggi)

    t_media_domani=int((((int(domani_temp[0])+int(domani_temp[1]))/2)-32)/1.8)
    t_media_domani_str=str(t_media_domani)

    t_media_domani_1=int((((int(domani_temp_1[0])+int(domani_temp_1[1]))/2)-32)/1.8)
    t_media_domani_1_str=str(t_media_domani_1)

    t_media_domani_2=int((((int(domani_temp_2[0])+int(domani_temp_2[1]))/2)-32)/1.8)
    t_media_domani_2_str=str(t_media_domani_2)

    t_media_domani_3=int((((int(domani_temp_3[0])+int(domani_temp_3[1]))/2)-32)/1.8)
    t_media_domani_3_str=str(t_media_domani_3)

    t_media_domani_4=int((((int(domani_temp_4[0])+int(domani_temp_4[1]))/2)-32)/1.8)
    t_media_domani_4_str=str(t_media_domani_4)


    x=0.5*pow((t_media_oggi-20)/5.5,2) #crescita oggi
    previsione=1/pow(2.7,x)
    previsione_str=str(previsione)

    y=0.5*pow((t_media_domani-20)/5.5,2)
    previsione_domani=1/pow(2.7,y)
    previsione_domani_str=str(previsione_domani)

    y_1=0.5*pow((t_media_domani_1-20)/5.5,2)
    previsione_domani_1=1/pow(2.7,y_1)
    previsione_domani_1_str=str(previsione_domani_1)

    y_2=0.5*pow((t_media_domani_2-20)/5.5,2)
    previsione_domani_2=1/pow(2.7,y_2)
    previsione_domani_2_str=str(previsione_domani_2)

    y_3=0.5*pow((t_media_domani_3-20)/5.5,2)
    previsione_domani_3=1/pow(2.7,y_3)
    previsione_domani_3_str=str(previsione_domani_3)

    y_4=0.5*pow((t_media_domani_4-20)/5.5,2)
    previsione_domani_4=1/pow(2.7,y_4)
    previsione_domani_4_str=str(previsione_domani_4)
 

    

    if data_time_h_erba[0]==oggi and b[i-1]=="Yes":
      
      h_erba_1=media_h_erba+previsione_domani #valore misurato oggi + crescita di domani
      h_erba_1_str=str(h_erba_1)
      h_erba_2=h_erba_1+previsione_domani_1
      h_erba_2_str=str(h_erba_2)
      h_erba_3=h_erba_2+previsione_domani_2
      h_erba_3_str=str(h_erba_3)
      h_erba_4=h_erba_3+previsione_domani_3
      h_erba_4_str=str(h_erba_4)
      h_erba_5=h_erba_4+previsione_domani_4
      h_erba_5_str=str(h_erba_5)

      info=oggi +","+ t_media_oggi_str+","+t_media_domani_str+","+t_media_domani_1_str+","+t_media_domani_2_str+","+t_media_domani_3_str+","+t_media_domani_4_str+","+ media_h_erba_str+","+previsione_str +","+ previsione_domani_str +","+ previsione_domani_1_str +","+previsione_domani_2_str+","+ previsione_domani_3_str +","+previsione_domani_4_str +","+h_erba_1_str +","+h_erba_2_str+","+h_erba_3_str+","+h_erba_4_str+","+h_erba_5_str

    else:
      
      if TabellaCrescitaErba_data!=oggi:
      
          media_h_erba=media_h_erba+previsione
          media_h_erba_str=str(media_h_erba)

          h_erba_1=media_h_erba+previsione_domani  # se manca la misura di oggi: valore di ieri + crescita prevista di oggi
          h_erba_1_str=str(h_erba_1)
          h_erba_2=h_erba_1+previsione_domani_1
          h_erba_2_str=str(h_erba_2)
          h_erba_3=h_erba_2+previsione_domani_2
          h_erba_3_str=str(h_erba_3)
          h_erba_4=h_erba_3+previsione_domani_3
          h_erba_4_str=str(h_erba_4)
          h_erba_5=h_erba_4+previsione_domani_4
          h_erba_5_str=str(h_erba_5)
          
          info=oggi +","+ t_media_oggi_str+","+t_media_domani_str+","+t_media_domani_1_str+","+t_media_domani_2_str+","+t_media_domani_3_str+","+t_media_domani_4_str+","+ media_h_erba_str+","+previsione_str +","+ previsione_domani_str +","+ previsione_domani_1_str +","+previsione_domani_2_str+","+ previsione_domani_3_str +","+previsione_domani_4_str+","+h_erba_1_str +","+h_erba_2_str+","+h_erba_3_str+","+h_erba_4_str+","+h_erba_5_str

      else:
         info=a_1

##      # Create a session with your Temboo account detail
##      session = TembooSession("sperimentaleggp", "myFirstApp", "1akJ2G8w0DhM6TDCyKPFGwXvFgRveiZ6")
##
##      # Instantiate the Choreo
##      appendRowChoreo = AppendRow(session)
##
##      # Get an InputSet object for the Choreo
##      appendRowInputs = appendRowChoreo.new_input_set()
##
##      # Set the Choreo inputs
##      aggiornamento=oggi+" "+tempo+","+oggi+" "+tempo+","+media_h_erba_str+","+media_h_erba_str +","+media_h_erba_str +","+media_h_erba_str +","+media_h_erba_str +","+ "Algorithm prevision"     
##      appendRowInputs.set_RowData(aggiornamento)       
##                
##      appendRowInputs.set_SpreadsheetTitle("Tranas (Responses)")
##      appendRowInputs.set_RefreshToken("1/aLxhlVr07QMDnS9qYtcMWbAw7KngqO_TIZCbja2Bi88")
##      appendRowInputs.set_ClientSecret("ccoAJeO8Yuf33S25AvWocb7b")
##      appendRowInputs.set_ClientID("374932964420-dmt8ularkt07p1e6jho1r8ahrsqv32d9.apps.googleusercontent.com")
##
##          
##      appendRowResults = appendRowChoreo.execute_with_results(appendRowInputs)


      

    # Create a session with your Temboo account detail
    session = TembooSession("sperimentaleggp", "myFirstApp", "1akJ2G8w0DhM6TDCyKPFGwXvFgRveiZ6")

    # Instantiate the Choreo
    appendRowChoreo = AppendRow(session)

    # Get an InputSet object for the Choreo
    appendRowInputs = appendRowChoreo.new_input_set()

    # Set the Choreo inputs
        
    appendRowInputs.set_RowData(info)       
            
    appendRowInputs.set_SpreadsheetTitle("TabellaCrescitaErba")
    appendRowInputs.set_RefreshToken("1/aLxhlVr07QMDnS9qYtcMWbAw7KngqO_TIZCbja2Bi88")
    appendRowInputs.set_ClientSecret("ccoAJeO8Yuf33S25AvWocb7b")
    appendRowInputs.set_ClientID("374932964420-dmt8ularkt07p1e6jho1r8ahrsqv32d9.apps.googleusercontent.com")

      
    appendRowResults = appendRowChoreo.execute_with_results(appendRowInputs)
       
    # Print the Choreo outputs
    print("NewAccessToken: " + appendRowResults.get_NewAccessToken())
    print("Response: " + appendRowResults.get_Response())

