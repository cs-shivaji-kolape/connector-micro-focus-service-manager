"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""


error_dict = {
    '400': 'Invalid Input',
    '401': 'Unauthorized error',
    '403': 'Forbidden error',
    '404': 'Resource not found',
    '405': 'Method not allowed',
    '500': 'Requested Input/URL invalid or not found',
    '600': 'Internal Server Error'
}

view_dict = {
    'Summary': 'summary',
    'Condense': 'condense',
    'Expand': 'expand'
}

impact_dict = {
    'Enterprises': 1,
    'Site/Dept': 2,
    'Multiple Users': 3,
    'User': 4
}

urgency_dict = {
    'Critical': 1,
    'High': 2,
    'Average': 3,
    'Low': 4
}

source_dict = {
    'User': 1,
    'Group': 2,
    'Event': 3,
    'Chat': 4,
    'E-mail': 5,
    'Telephone': 6
}