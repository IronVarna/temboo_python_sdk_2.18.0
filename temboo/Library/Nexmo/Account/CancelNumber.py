# -*- coding: utf-8 -*-

###############################################################################
#
# CancelNumber
# Cancels the specified inbound number subscription.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CancelNumber(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CancelNumber Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CancelNumber, self).__init__(temboo_session, '/Library/Nexmo/Account/CancelNumber')


    def new_input_set(self):
        return CancelNumberInputSet()

    def _make_result_set(self, result, path):
        return CancelNumberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CancelNumberChoreographyExecution(session, exec_id, path)

class CancelNumberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CancelNumber
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(CancelNumberInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(CancelNumberInputSet, self)._set_input('APISecret', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((required, string) 2-digit country code. (e.g.: CA))
        """
        super(CancelNumberInputSet, self)._set_input('Country', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((required, string) Your inbound (MSISDN) number (e.g. 34911067000).)
        """
        super(CancelNumberInputSet, self)._set_input('Number', value)

class CancelNumberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CancelNumber Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Nexmo. A 200 is returned for a successful request.)
        """
        return self._output.get('ResponseStatusCode', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. For a successful request, an empty response body is returned.)
        """
        return self._output.get('Response', None)

class CancelNumberChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CancelNumberResultSet(response, path)
