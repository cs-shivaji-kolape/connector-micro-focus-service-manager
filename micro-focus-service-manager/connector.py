""" Copyright start
  Copyright (C) 2008 - 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import operations, _check_health

logger = get_logger('micro-focus-service-manager')


class MicroFocusServiceManager(Connector):
    def execute(self, config, operation, params, **kwargs):
        action = operations.get(operation)
        logger.info('executing {}'.format(action))
        return action(config, params)

    def check_health(self, config):
        try:
            logger.info('executing check health')
            return _check_health(config)
        except Exception as err:
            logger.exception(str(err))
            raise ConnectorError(str(err))



