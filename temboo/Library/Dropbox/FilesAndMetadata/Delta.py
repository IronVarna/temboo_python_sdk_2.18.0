# -*- coding: utf-8 -*-

###############################################################################
#
# Delta
# Allows you keep up with changes to files and folders in a user's Dropbox.
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

class Delta(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Delta Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Delta, self).__init__(temboo_session, '/Library/Dropbox/FilesAndMetadata/Delta')


    def new_input_set(self):
        return DeltaInputSet()

    def _make_result_set(self, result, path):
        return DeltaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeltaChoreographyExecution(session, exec_id, path)

class DeltaInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Delta
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(DeltaInputSet, self)._set_input('AccessToken', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(DeltaInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(DeltaInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(DeltaInputSet, self)._set_input('AppSecret', value)
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) A string that is used to keep track of your current state. On the next call pass in this value to return delta entries that have been recorded since the cursor was returned.)
        """
        super(DeltaInputSet, self)._set_input('Cursor', value)
    def set_IncludeMediaInfo(self, value):
        """
        Set the value of the IncludeMediaInfo input for this Choreo. ((optional, boolean) If set to true, each file will include a photo_info dictionary for photos and a video_info dictionary for videos with additional media info.)
        """
        super(DeltaInputSet, self)._set_input('IncludeMediaInfo', value)
    def set_Locale(self, value):
        """
        Set the value of the Locale input for this Choreo. ((optional, string) The metadata returned will have its size field translated based on the given locale.)
        """
        super(DeltaInputSet, self)._set_input('Locale', value)
    def set_PathPrefix(self, value):
        """
        Set the value of the PathPrefix input for this Choreo. ((optional, string) Filters the response to only include entries at or under the specified path.)
        """
        super(DeltaInputSet, self)._set_input('PathPrefix', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(DeltaInputSet, self)._set_input('ResponseFormat', value)

class DeltaResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Delta Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class DeltaChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeltaResultSet(response, path)
