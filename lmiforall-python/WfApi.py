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


class WfApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def getFilterNames(self, **kwargs):
        """Get a list of all available filter names.

        Args:
            
        Returns: list[str]
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFilterNames" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wf/filters'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[str]')
        return responseObject
        
        
    def getAllFiltersInfo(self, **kwargs):
        """Get a list of all available filters and their codings.

        Args:
            
        Returns: list[LFSFilterInfo]
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllFiltersInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wf/filters/all'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[LFSFilterInfo]')
        return responseObject
        
        
    def getFilterInfo(self, name, **kwargs):
        """Get more information about a certain filter.

        Args:
            name, str: The name of the filter. (required)
            
        Returns: LFSFilterInfo
        """

        allParams = ['name']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getFilterInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wf/filters/info/{name}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('name' in params):
            replacement = str(self.apiClient.toPathValue(params['name']))
            resourcePath = resourcePath.replace('{' + 'name' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'LFSFilterInfo')
        return responseObject
        
        
    def predictEmployment(self, soc, **kwargs):
        """Get a Working Futures prediction about a job: how many people will be employed in this job?

        Args:
            soc, int: The job's SOC code. (required)
            minYear, int: Minimum year to predict (2014-2020) (optional)
            maxYear, int: Maximum year to predict (2014-2020) (optional)
            
        Returns: WFPrediction
        """

        allParams = ['soc', 'minYear', 'maxYear']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method predictEmployment" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wf/predict'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('soc' in params):
            queryParams['soc'] = self.apiClient.toPathValue(params['soc'])
        if ('minYear' in params):
            queryParams['minYear'] = self.apiClient.toPathValue(params['minYear'])
        if ('maxYear' in params):
            queryParams['maxYear'] = self.apiClient.toPathValue(params['maxYear'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'WFPrediction')
        return responseObject
        
        
    def predictEmploymentBreakdown(self, soc, filter, **kwargs):
        """Get a Working Futures prediction about a job and break it down across a filter.

        Args:
            soc, int: The job's SOC code. (required)
            minYear, int: Minimum year to predict (2014-2020) (optional)
            maxYear, int: Maximum year to predict (2014-2020) (optional)
            filter, str: Break prediction down across one of the filters. (required)
            
        Returns: WFBreakdownPrediction
        """

        allParams = ['soc', 'minYear', 'maxYear', 'filter']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method predictEmploymentBreakdown" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wf/predict/breakdown/{filter}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('soc' in params):
            queryParams['soc'] = self.apiClient.toPathValue(params['soc'])
        if ('minYear' in params):
            queryParams['minYear'] = self.apiClient.toPathValue(params['minYear'])
        if ('maxYear' in params):
            queryParams['maxYear'] = self.apiClient.toPathValue(params['maxYear'])
        if ('filter' in params):
            replacement = str(self.apiClient.toPathValue(params['filter']))
            resourcePath = resourcePath.replace('{' + 'filter' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'WFBreakdownPrediction')
        return responseObject
        
        
    

