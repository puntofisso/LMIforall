#!/usr/bin/env python
"""
WordAPI.py
Copyright 2012 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *


class OnetApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def getImportance(self, soc, **kwargs):
        """Get O*NET skill importance for an occupation by score and ranking.

        Args:
            soc, int: SOC code of the occupation. (required)
            
        Returns: ONETInfo
        """

        allParams = ['soc']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getImportance" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/onet/importance/{soc}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('soc' in params):
            replacement = str(self.apiClient.toPathValue(params['soc']))
            resourcePath = resourcePath.replace('{' + 'soc' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ONETInfo')
        return responseObject
        
        
    def getLevels(self, soc, **kwargs):
        """Get O*NET required proficiency levels for an occupation by score and ranking.

        Args:
            soc, int: SOC code of the occupation. (required)
            
        Returns: ONETInfo
        """

        allParams = ['soc']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLevels" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/onet/levels/{soc}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('soc' in params):
            replacement = str(self.apiClient.toPathValue(params['soc']))
            resourcePath = resourcePath.replace('{' + 'soc' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ONETInfo')
        return responseObject
        
        
    def getSkills(self, **kwargs):
        """Return a list of available O*NET skills and their descriptions.

        Args:
            
        Returns: list[Map[string, string]]
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSkills" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/onet/skills'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[Map[string, string]]')
        return responseObject
        
        
    


