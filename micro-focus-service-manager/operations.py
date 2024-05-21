""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import requests
import base64
import json
from urllib.parse import urlencode
from connectors.core.connector import ConnectorError, get_logger
from .constants import *

logger = get_logger('micro-focus-service-manager')


def make_rest_call(config, method, endpoint, body, param_header):
    try:
        server_url = config['host'].strip('/')
        if not config['port']:
            config['port'] = 13080
        server_url = '{0}:{1}'.format(server_url, config['port'])
        if not server_url.startswith('http://') and not server_url.startswith('https://'):
            server_url = 'https://' + server_url
        url = '{0}/{1}/{2}'.format(server_url, config.get('path').strip('/'), endpoint)
        logger.info(url)
        usrPass = '{0}:{1}'.format(config['username'], config['password'])
        b64Val = base64.b64encode(usrPass.encode())
        temp = 'Basic {0}'.format(b64Val.decode("utf-8"))

        headers = {
            'Authorization': temp,
            'Content-Type': 'application/json'
        }

        # We are getting headers ONLY for Update RF attachment, and it needs body in string format
        if param_header:
            headers.update(param_header)
            response = requests.request(method=method, url=url, headers=headers, data=body,
                                        verify=config['verify_ssl'])
        else:
            response = requests.request(method=method, url=url, headers=headers, data=json.dumps(body),
                                        verify=config['verify_ssl'])

        if response.ok:
            logger.info('Successfully got response from server')
            if 'json' in response.headers['Content-Type']:
                return response.json()
            else:
                return response.content
        else:
            logger.error(response.content)
            raise ConnectorError({'status_code': response.status_code, 'message': response.content})
    except requests.exceptions.SSLError:
        raise ConnectorError('SSL certificate validation failed')
    except requests.exceptions.ConnectTimeout:
        raise ConnectorError('The request timed out while trying to connect to the server')
    except requests.exceptions.ReadTimeout:
        raise ConnectorError('The server did not send any data in the allotted amount of time')
    except requests.exceptions.ConnectionError:
        raise ConnectorError('Invalid endpoint or credentials')
    except Exception as err:
        raise ConnectorError(str(err))


def _create_temp_dict(params):
    try:
        temp_dict = {
            "Title": params.get('title'),
            "Description": params.get('description'),
            "Impact": impact_dict.get(params.get('impact')),
            "Category": params.get('category'),
            "Service": params.get('service'),
            "Service_recipient": params.get('service_recipient'),
            "AffectedCI": params.get('affected_ci'),
            "Subcategory": params.get('subcategory'),
            "Area": params.get('area'),
            "AssignmentGroup": params.get('assignment_group'),
            "Source": source_dict.get(params.get('source')),
            "ContactPerson": params.get('contact_person'),
            "OutageStartTime": params.get('outage_start_time'),
            "OutageEndTime": params.get('outage_end_time'),
            "Solution": params.get('solution'),
            "Assignee": params.get('assignee'),
            "Location": params.get('location'),
            "Urgency": urgency_dict.get(params.get('urgency'))
        }
        return temp_dict
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def create_incident(config, params):
    try:
        temp_dict = _create_temp_dict(params)
        json_input = {}
        if params.get('json_input'):
            if type(params.get('json_input')) == dict:
                json_input = params.get('json_input')
            else:
                logger.error('Additional Fields should be in dictionary format')
                raise ConnectorError('Additional Fields should be in dictionary format')
        temp_dict.update(json_input)
        params_dict = {'Incident': temp_dict}
        url = 'incidents'
        return make_rest_call(config, 'post', url, params_dict, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def _create_temp_dict_for_change(params):
    temp_dict = {
        "header": {
            "Title": params.get('Title'),
            "ChangeCoordinator": params.get('ChangeCoordinator'),
            "Reason": params.get('ReasonForChange'),
            "InitiatedBy": params.get('InitiatedBy'),
            "Subcategory": params.get('Subcategory'),
            "Category": params.get('Category'),
            "AffectedCI": params.get('AffectedCI'),
            "PlannedStart": params.get('PlannedStart'),
            "PlannedEnd": params.get('PlannedEnd')
        },
        "description.structure": {
            "Description": params.get('Description')
        },
        "ChangeOriginator": params.get('ChangeOriginator'),
        "Service": params.get('Service')
    }
    return temp_dict


def create_change(config, params):
    try:
        temp_dict = _create_temp_dict_for_change(params)
        json_input = {}
        if params.get('json_input'):
            json_input = params.get('json_input')
        temp_dict['header'].update(json_input)
        params_dict = {'Change': temp_dict}
        url = 'changes'
        return make_rest_call(config, 'post', url, params_dict, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def update_incident(config, params):
    try:
        temp_dict = _create_temp_dict(params)
        temp_dict = {k: v for k, v in temp_dict.items() if v is not None and v != ''}
        json_input = {}
        if params.get('json_input'):
            if type(params.get('json_input')) == dict:
                json_input = params.get('json_input')
            else:
                logger.error('Additional Fields should be in dictionary format')
                raise ConnectorError('Additional Fields should be in dictionary format')
        temp_dict.update(json_input)
        params_dict = {'Incident': temp_dict}
        url = 'incidents/{}'.format(params.get('incident_id'))
        return make_rest_call(config, 'put', url, params_dict, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def _get_params(params):
    params_dict = {}
    params_dict['query'] = params.get('query')
    params_dict['sort'] = params.get('sort')
    params_dict['start'] = params.get('start')
    params_dict['count'] = params.get('count')
    params_dict['view'] = view_dict.get(params.get('view'))
    params_dict = {k: v for k, v in params_dict.items() if v is not None and v != ''}
    return params_dict


def list_incidents(config, params):
    try:
        params_dict = _get_params(params)
        url = 'incidents?{}'.format(urlencode(params_dict))
        return make_rest_call(config, 'get', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def list_changes(config, params):
    try:
        params_dict = _get_params(params)
        params_dict = {k: v for k, v in params_dict.items() if v is not None and v != ''}
        url = 'changes?{}'.format(urlencode(params_dict))
        return make_rest_call(config, 'get', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def get_incident(config, params):
    try:
        incident_id = params.get('incident_id')
        url = 'incidents/{}'.format(incident_id)
        return make_rest_call(config, 'get', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def get_change_request(config, params):
    try:
        change_request_id = params.get('change_request_id')
        url = 'changes/{}'.format(change_request_id)
        return make_rest_call(config, 'get', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def get_device_list(config, params):
    try:
        params_dict = _get_params(params)
        url = 'devices?{}'.format(urlencode(params_dict))
        return make_rest_call(config, 'get', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def get_device(config, params):
    try:
        url = 'devices/{}'.format(params.get('config_item'))
        return make_rest_call(config, 'get', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def _check_health(config):
    try:
        res = make_rest_call(config, 'get', 'incidents', {'count': 1}, {})
        return True
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def get_rf_request(config, params):
    try:
        change_rf_id = params.get('rf_id')
        url = 'requests/{}'.format(change_rf_id)
        return make_rest_call(config, 'get', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def create_rf(config, params):
    try:
        payload_request = {}
        fields = ['Impact', 'Urgency', 'Priority', 'Category', 'Subcategory', 'BriefDescription', 'AssignedTo',
                  'AssignedGroup', 'RequestorName', 'ProductType']
        for field in fields:
            payload_request[field] = str(params.get(field))

        payload_request['Description'] = ([params.get('Description')])

        params_dict = {'Request': payload_request}
        url = 'requests'
        return make_rest_call(config, 'post', url, params_dict, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def update_rf_attachment(config, params):
    try:
        param_attachment_name = params.get('attachment_name')
        body = params.get('msg_body')
        url = 'requests/{}/attachments/cid:{}'.format(params.pop('rf_id'), param_attachment_name)

        extra_header = {
            'Content-Disposition': 'attachment;filename=' + param_attachment_name,
            'Content-Type': 'application/vnd.ms-outlook'
        }
        return make_rest_call(config, 'post', url, body, extra_header)

    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def update_change(config, params):
    try:
        payload = dict()
        payload['SubClosureCode'] = str(params.get('SubClosureCode'))

        if params.get('PlannedStart') and params.get('PlannedEnd'):
            payload['header'] = {'Phase': params.get('Phase'), 'PlannedStart': params.get('PlannedStart'),
                                 'PlannedEnd': params.get('PlannedEnd')}
        else:
            payload['header'] = {'Phase': params.get('Phase')}
        payload_close = {'ClosureCode': params.get('ClosureCode'), 'ClosingComments': [params.get('ClosingComments')]}
        payload['close'] = payload_close

        url = 'changes/{}'.format(params.pop('change_id'))

        params_dict = {'Change': payload}

        return make_rest_call(config, 'post', url, params_dict, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def retrieve_attachment_information(config, params):
    try:
        incident_id = params.get('incident_id')
        url = 'incidents/{}/attachments'.format(incident_id)
        return make_rest_call(config, 'get', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def download_an_attachment(config, params):
    try:
        incident_id = params.get('incident_id')
        attachment_id = params.get('attachment_id')
        url = 'incidents/{}/attachments/{}'.format(incident_id, attachment_id)
        return make_rest_call(config, 'get', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def delete_an_attachment(config, params):
    try:
        incident_id = params.get('incident_id')
        attachment_id = params.get('attachment_id')
        url = 'incidents/{}/attachments/{}'.format(incident_id, attachment_id)
        return make_rest_call(config, 'delete', url, {}, {})
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


operations = {
    'create_incident': create_incident,
    'update_incident': update_incident,
    'list_incidents': list_incidents,
    'get_incident': get_incident,
    'get_device_list': get_device_list,
    'get_device': get_device,
    'create_change': create_change,
    'get_change_request': get_change_request,
    'list_changes': list_changes,
    'get_rf': get_rf_request,
    'create_rf': create_rf,
    'update_rf_attachment': update_rf_attachment,
    'update_change': update_change,
    'retrieve_attachment_information': retrieve_attachment_information,
    'download_an_attachment': download_an_attachment,
    'delete_an_attachment': delete_an_attachment

}
