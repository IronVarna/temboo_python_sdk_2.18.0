# -*- coding: utf-8 -*-

###############################################################################
#
# GetThumbnail
# Retrieves a thumbnail for a specified image.
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

class GetThumbnail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetThumbnail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetThumbnail, self).__init__(temboo_session, '/Library/Dropbox/FilesAndMetadata/GetThumbnail')


    def new_input_set(self):
        return GetThumbnailInputSet()

    def _make_result_set(self, result, path):
        return GetThumbnailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetThumbnailChoreographyExecution(session, exec_id, path)

class GetThumbnailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetThumbnail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetThumbnailInputSet, self)._set_input('AccessToken', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetThumbnailInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(GetThumbnailInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(GetThumbnailInputSet, self)._set_input('AppSecret', value)
    def set_ImageFormat(self, value):
        """
        Set the value of the ImageFormat input for this Choreo. ((optional, string) The thumbnail format to return for the specified image. Accepted values are: jpeg (default) or png.)
        """
        super(GetThumbnailInputSet, self)._set_input('ImageFormat', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The path to the file that you want to generate a thumbnail for (i.e. /RootFolder/SubFolder/MyFile.txt).)
        """
        super(GetThumbnailInputSet, self)._set_input('Path', value)
    def set_Root(self, value):
        """
        Set the value of the Root input for this Choreo. ((optional, string) Defaults to "auto" which automatically determines the root folder using your app's permission level. Other options are "sandbox" (App Folder) and "dropbox" (Full Dropbox).)
        """
        super(GetThumbnailInputSet, self)._set_input('Root', value)
    def set_Size(self, value):
        """
        Set the value of the Size input for this Choreo. ((optional, string) The size of the thumbnail to generate. Accepted values are: small, medium, s, m, l, xl. See Choreo documentation for exact dimensions. Defaults to "small".)
        """
        super(GetThumbnailInputSet, self)._set_input('Size', value)

class GetThumbnailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetThumbnail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The base64 encoded image content of the thumbnail.)
        """
        return self._output.get('Response', None)

class GetThumbnailChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetThumbnailResultSet(response, path)
