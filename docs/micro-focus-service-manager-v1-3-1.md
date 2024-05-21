## About the connector
Micro Focus service manager connector helps you to create incident, update incident, list incidents, get incident, get device list and get device
<p>This document provides information about the Micro Focus Service Manager Connector, which facilitates automated interactions, with a Micro Focus Service Manager server using FortiSOAR&trade; playbooks. Add the Micro Focus Service Manager Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Micro Focus Service Manager.</p>

### Version information

Connector Version: 1.3.1


Authored By: SpryIQ.Co

Certified: No
## Release Notes for version 1.3.1
Following enhancements have been made to the Micro Focus Service Manager Connector in version 1.3.1:
<ul>
<li><p>Added the following new actions and its playbooks</p>

<ul>
<li><p>Update Change</p></li>
<li><p>Get RF - Request Fulfillment Ticket</p></li>
<li><p>Create RF - Request Fulfillment Ticket</p></li>
<li><p>Update RF - Request Fulfillment Ticket for an attachment</p></li>
</ul></li>
</ul>
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-micro-focus-service-manager`

## Prerequisites to configuring the connector
- You must have the URL of Micro Focus Service Manager server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Micro Focus Service Manager server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Micro Focus Service Manager</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Host or domain name on which the service is available.<br>
<tr><td>Initial Path<br></td><td>Initial path that is the path of URI for a given deployment. This value should start with /SM/9/rest<br>
<tr><td>Username<br></td><td>Username used to connect to the Micro Focus Service Manager server to which you will connect and perform automated operations<br>
<tr><td>Password<br></td><td>Password used to connect to the Micro Focus Service Manager server to which you will connect and perform automated operations<br>
<tr><td>Port<br></td><td>TCP port number on which service is available.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Create Incident<br></td><td>Creates a new incident on the Micro Focus Service Manager server, based on the input parameters you have specified<br></td><td>create_incident <br/>Investigation<br></td></tr>
<tr><td>Get Incident List<br></td><td>Retrieves a list of incidents from the Micro Focus Service Manager server, based on the query and other input parameters you have specified.<br></td><td>get_incidents <br/>Investigation<br></td></tr>
<tr><td>Get Incident<br></td><td>Retrieves details about a specific incident from the Micro Focus Service Manager server, based on the incident ID you have specified.<br></td><td>get_incidents <br/>Investigation<br></td></tr>
<tr><td>Update Incident<br></td><td>Updates an existing incident on the Micro Focus Service Manager server, based on the input parameters you have specified.<br></td><td>update_incident <br/>Investigation<br></td></tr>
<tr><td>Get Device List<br></td><td>Retrieves a list of devices from the Micro Focus Service Manager server, based on the query and other input parameters you have specified.<br></td><td>get_devices <br/>Investigation<br></td></tr>
<tr><td>Get Device<br></td><td>Retrieves details about a specific device from the Micro Focus Service Manager server, based on the configuration item you have specified.<br></td><td>get_devices <br/>Investigation<br></td></tr>
<tr><td>Create Change<br></td><td>Creates a new change request on the Service Manager server, based on the title, category, primary affected service, and other input parameters you have specified.<br></td><td>create_change <br/>Investigation<br></td></tr>
<tr><td>Get Change List<br></td><td>Retrieves a list of all change requests or specific change requests from the Service Manager server, based on the query and other input parameters you have specified.<br></td><td>get_changes <br/>Investigation<br></td></tr>
<tr><td>Get Change Request<br></td><td>Retrieves details for a specific change request from the Service Manager server, based on the change request ID you have specified<br></td><td>get_changes <br/>Investigation<br></td></tr>
<tr><td>Update Change<br></td><td>Updates an existing change for closure in Service Manager based on the change ID, closure code, phase, and other input parameters you have specified.<br></td><td>update_change <br/>Investigation<br></td></tr>
<tr><td>Create RF - Request Fulfillment Ticket<br></td><td>Creates a new RF - Request Fulfillment Ticket on the MFSM/HPSM Manager server, based on the title, description, category, priority, etc., and other input parameters you have specified.<br></td><td>create_rf <br/>Investigation<br></td></tr>
<tr><td>Get RF - Request Fulfillment Ticket<br></td><td>Retrieves details for a specific RF-Request Fulfillment Ticket from the MFSM/HPSM server, based on the RF ID you have specified.<br></td><td>get_rf <br/>Investigation<br></td></tr>
<tr><td>Update RF - Request Fulfillment Ticket for an attachment<br></td><td>Updates an existing RF-Request Fulfillment Ticket to upload (add) an attachment to that RF in Service Manager based on the RF ID, attachment name, and message body you have specified.<br></td><td>update_rf_attachment <br/>Investigation<br></td></tr>
<tr><td>Retrieve Attachment Information<br></td><td>Request on the Resource Attachment Collection of an incident identified by incident number.<br></td><td>retrieve_attachment_information <br/>Investigation<br></td></tr>
<tr><td>Download Attachment<br></td><td>Download an attachment associated with an incident identified by attachment number and incident number.<br></td><td>download_an_attachment <br/>Investigation<br></td></tr>
<tr><td>Delete Attachment<br></td><td>Delete an attachment associated with an incident identified by attachment number and incident number.<br></td><td>delete_an_attachment <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Create Incident
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Title<br></td><td>Title of the incident that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Description<br></td><td>Description of the incident that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Impact<br></td><td>Impact value to be assigned to the incident that you want to create on the Micro Focus Service Manager server.
You can choose from the following options: Enterprises, Site/Dept, Multiple Users, or User.
By default, this is set as User.<br>
</td></tr><tr><td>Urgency<br></td><td>Urgency value to be assigned to the incident that you want to create on the Micro Focus Service Manager server.
You can choose from the following options: Critical, High, Average, or Low.
By default, this is set as Low.<br>
</td></tr><tr><td>Category<br></td><td>Category to be assigned to the incident that you want to create on the Micro Focus Service Manager server.
For example, Incident, Complaint, etc.
Note: Category values can be added in lowercase.<br>
</td></tr><tr><td>Primary Affected Service<br></td><td>ID of the primary service that has been affected by the incident that you want to create on the Micro Focus Service Manager server.
For example, CI1001020<br>
</td></tr><tr><td>Affected CI<br></td><td>(Optional) ID of the service component(s) that have been affected by the incident that you want to create on the Micro Focus Service Manager server.
For example, CI1000783<br>
</td></tr><tr><td>Subcategory<br></td><td>(Optional) Subcategory to be assigned to the incident that you want to create on the Micro Focus Service Manager server<br>
</td></tr><tr><td>Area<br></td><td>(Optional) Area to be assigned to the incident that you want to create on the Micro Focus Service Manager server.
For example, performance, failure, hardware, access, etc.<br>
</td></tr><tr><td>Assignment Group<br></td><td>(Optional) Assignment Group to whom the incident that you want to create on the Micro Focus Service Manager server should be assigned.
For example, Office Supplies (North America).<br>
</td></tr><tr><td>Source<br></td><td>(Optional) Source of the incident that you want to create on the Micro Focus Service Manager server.
You can choose from the following options: User, Group, Event, Chat, E-mail, or Telephone.
By default, this is set as User.<br>
</td></tr><tr><td>Contact Person<br></td><td>(Optional) Name of the person to contact for information about the incident that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Outage Start Time<br></td><td>(Optional) Start time of the outage due to the incident that you want to create on the Micro Focus Service Manager server.
You must enter the time in the format MM/DD/YY HH:MM:SS
For example, 08/24/18 03:30:00.<br>
</td></tr><tr><td>Outage End Time<br></td><td>(Optional) End time of the outage due to the incident that you want to create on the Micro Focus Service Manager server.
You must enter the time in the format MM/DD/YY HH:MM:SS
For example, 08/24/18 05:30:00.<br>
</td></tr><tr><td>Assignee<br></td><td>(Optional) Name of the assignee of the incident that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Service Recipient<br></td><td>(Optional) Name of the service recipient of the incident that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Location<br></td><td>(Optional) Location where the incident occurred that you want to create on the Micro Focus Service Manager server.For example, Africa, Asia, Europe.<br>
</td></tr><tr><td>Solution<br></td><td>(Optional) Solution (if available) to the incident that occurred and that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Additional Fields<br></td><td>(Optional) Additional fields that you want to add to the incident record that you want to create on the Micro Focus Service Manager server.
You must add the additional fields in the JSON Dictionary format.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Incident": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Service": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "UpdatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "OpenedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Assignee": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Urgency": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Phase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Description": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "UpdatedTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "IncidentID": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Impact": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "OpenTime": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Get Incident List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query<br></td><td>Query (or filter) that you use to specify the search criteria, based on which you want to retrieve incidents from the Micro Focus Service Manager server.
For example, Category = "incident", Title = "Desktop screen out of order"<br>
</td></tr><tr><td>Sort<br></td><td>Sorts the result of the operation, i.e., the list of incidents retrieved from the Micro Focus Service Manager server, based on the sort fields you have specified.
For example, Urgency:ascending,field2:descending<br>
</td></tr><tr><td>Start<br></td><td>Index of the member from which the collection response representation begins<br>
</td></tr><tr><td>Count<br></td><td>Number of collection members to be returned by this operation.<br>
</td></tr><tr><td>View<br></td><td>View of the collection that is returned by this operation.
You can choose from the following options: Summary, Condense, or Expand.
By default, this is set as Expand.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@start": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@totalcount": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ResourceName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "content": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Incident": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Area": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Assignee": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ClosedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ClosedTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ClosureCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Company": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Contact": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Description": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Impact": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "IncidentID": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "JournalUpdates": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "OpenTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "OpenedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Phase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Service": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Solution": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Subarea": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "UpdatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "UpdatedTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Urgency": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Get Incident
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident ID<br></td><td>ID of the incident whose details you want to retrieve from the Micro Focus Service Manager server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": 0,
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Incident": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "UpdatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "SLAAgreementID": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Urgency": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Area": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "OpenTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Location": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ClosedTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Subarea": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Solution": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ClosedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "OpenedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "IncidentID": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Assignee": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Company": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Description": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "TicketOwner": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ProblemType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "UpdatedTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Service": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Impact": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ClosureCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AffectedCI": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Update Incident
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident ID<br></td><td>ID of the incident that you want to update on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Title<br></td><td>(Optional) Title of the incident that you want to update on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Description<br></td><td>(Optional) Description of the incident that you want to update on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Impact<br></td><td>(Optional) Impact value to be assigned to the incident that you want to update on the Micro Focus Service Manager server.
You can choose from the following options: Enterprises, Site/Dept, Multiple Users, or User.
By default, this is set as User.<br>
</td></tr><tr><td>Urgency<br></td><td>(Optional) Urgency value to be assigned to the incident that you want to update on the Micro Focus Service Manager server.
You can choose from the following options: Critical, High, Average, or Low.
By default, this is set as Low.<br>
</td></tr><tr><td>Category<br></td><td>(Optional) Category to be assigned to the incident that you want to update on the Micro Focus Service Manager server.
For example, Incident, Complaint, etc.
Note: Category values can be added in lowercase.<br>
</td></tr><tr><td>Primary Affected Service<br></td><td>(Optional) ID of the primary service that has been affected by the incident that you want to update on the Micro Focus Service Manager server.
For example, CI1001020<br>
</td></tr><tr><td>Affected CI<br></td><td>(Optional) ID of the service component(s) that have been affected by the incident that you want to update on the Micro Focus Service Manager server.
For example, CI1000783<br>
</td></tr><tr><td>Subcategory<br></td><td>(Optional) Subcategory to be assigned to the incident that you want to update on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Area<br></td><td>(Optional) Area to be assigned to the incident that you want to update on the Micro Focus Service Manager server.For example, performance, failure, hardware, access, etc.<br>
</td></tr><tr><td>Assignment Group<br></td><td>(Optional) Assignment Group to whom the incident that you want to update on the Micro Focus Service Manager server should be assigned.
For example, Office Supplies (North America).<br>
</td></tr><tr><td>Source<br></td><td>(Optional) Source of the incident that you want to update on the Micro Focus Service Manager server.
You can choose from the following options: User, Group, Event, Chat, E-mail, or Telephone.
By default, this is set as User.<br>
</td></tr><tr><td>Contact Person<br></td><td>(Optional) Name of the person to contact for information about the incident that you want to update on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Outage Start Time<br></td><td>(Optional) Start time of the outage due to the incident that you want to update on the Micro Focus Service Manager server.
You must enter the time in the format MM/DD/YY HH:MM:SS
For example, 08/24/18 03:30:00.<br>
</td></tr><tr><td>Outage End Time<br></td><td>(Optional) End time of the outage due to the incident that you want to update on the Micro Focus Service Manager server.
You must enter the time in the format MM/DD/YY HH:MM:SS
For example, 08/24/18 05:30:00.<br>
</td></tr><tr><td>Assignee<br></td><td>(Optional) Name of the assignee of the incident that you want to update on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Service Recipient<br></td><td>(Optional) Name of the service recipient of the incident that you want to update on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Location<br></td><td>(Optional) Location where the incident occurred that you want to update on the Micro Focus Service Manager server.
For example, Africa, Asia, Europe.<br>
</td></tr><tr><td>Solution<br></td><td>(Optional) Solution (if available) to the incident that occurred and that you want to update on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Additional Fields<br></td><td>(Optional) Additional fields that you want to add to the incident record that you want to update on the Micro Focus Service Manager server.
You must add the additional fields in the JSON Dictionary format.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Incident": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Area": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Assignee": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Company": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Contact": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Description": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Impact": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "IncidentID": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "OpenTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "OpenedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Phase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Service": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Solution": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Subarea": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "UpdatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "UpdatedTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Urgency": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": ""
</code><code><br>}</code>

### operation: Get Device List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query<br></td><td>Query (or filter) that you use to specify the search criteria, based on which you want to retrieve devices from the Micro Focus Service Manager server.
For example, Status="Available"<br>
</td></tr><tr><td>Sort<br></td><td>Sorts the result of the operation, i.e., the list of devices retrieved from the Micro Focus Service Manager server, based on the sort fields you have specified.
For example, Urgency:ascending,field2:descending<br>
</td></tr><tr><td>Start<br></td><td>Index of the member from which the collection response representation begins.<br>
</td></tr><tr><td>Count<br></td><td>Number of collection members to be returned by this operation.<br>
</td></tr><tr><td>View<br></td><td>View of the collection that is returned by this operation.
You can choose from the following options: Summary, Condense, or Expand.
By default, this is set as Expand.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@totalcount": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ResourceName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "content": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Device": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "DisplayName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "UpdatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ConfigurationItem": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Vendor": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ConfigurationItemSubType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Company": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ConfigurationItemType": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@start": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": ""
</code><code><br>}</code>

### operation: Get Device
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>configuration Item<br></td><td>Configuration item of the device, i.e., the ID of the device, whose details you want to retrieve from the Micro Focus Service Manager server.
For example, CI1000011<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Device": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "DisplayName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "UpdatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ConfigurationItem": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Vendor": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ConfigurationItemSubType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Company": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ConfigurationItemType": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Create Change
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Title<br></td><td>Title of the change request that you want to create in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Description<br></td><td>Description of the change request that you want to create in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Category<br></td><td>Category to be assigned to the change request that you want to create in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Subcategory<br></td><td>Subcategory to be assigned to the change request that you want to create in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Initiated By<br></td><td>Name of the user who has initiated the change request that you want to create in the Micro Focus Service Manager server. <br>
</td></tr><tr><td>Primary Affected Service<br></td><td>ID of the primary service that has been affected by the change request that you want to create in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Affected CI<br></td><td>(Optional) ID of the service component(s) that have been affected by the change request that you want to create in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Change Originator<br></td><td>(Optional) Enter the value of the originator of the change for which you want to create a change request in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Change Coordinator<br></td><td>(Optional) Enter the value of the coordinator of the change for which you want to create a change request in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Reason For Change<br></td><td>(Optional) Enter the reason for which you want to create a change request in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Target Start Time<br></td><td>(Optional) Enter the target start DateTime for the change request that you want to create in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Target End Time<br></td><td>(Optional) Enter the target end DateTime for the change request that you want to create in the Micro Focus Service Manager server. <br>
</td></tr><tr><td>Additional Fields<br></td><td>(Optional) JSON dictionary using which you can add extra input parameters to the change request that you want to create in the Micro Focus Service Manager server.For example, {"AssignmentGroup": "cs"}<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Change": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "close": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ClosureCode": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "header": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Open": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Phase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Reason": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Company": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ChangeID": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "PlannedEnd": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ChangeModel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "DateEntered": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "InitiatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Subcategory": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "PlannedStart": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ApprovalStatus": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ChangeCoordinator": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "middle": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Service": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "CustomerVisible": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description.structure": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Description": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ChangeOriginator": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": ""
</code><code><br>}</code>

### operation: Get Change List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query<br></td><td>Query (or filter) that you use to specify the search criteria, based on which you want to retrieve change requests from the Micro Focus Service Manager server<br>
</td></tr><tr><td>Sort<br></td><td>Sorts the result of the operation, i.e., the list of change requests retrieved from the Micro Focus Service Manager server are sorted based on the sort fields you have specified. 
For example, Urgency:ascending,field2:descending<br>
</td></tr><tr><td>Start<br></td><td>Index of the member from which the collection response representation begins.<br>
</td></tr><tr><td>Count<br></td><td>Number of collection members to be returned by this operation.<br>
</td></tr><tr><td>View<br></td><td>View of the collection that is returned by this operation. 
You can choose from the following options: Summary, Condense, or Expand. 
By default, this is set as Expand.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@start": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "content": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Change": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "close": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "ClosureCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "ClosingComments": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "header": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Open": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Phase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Reason": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Company": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "ChangeID": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "CloseTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "PlannedEnd": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "ChangeModel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "DateEntered": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "InitiatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Subcategory": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "PlannedStart": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "ApprovalStatus": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "BackoutDuration": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "ChangeCoordinator": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "middle": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "Service": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "CustomerVisible": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "description.structure": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "Description": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "OoredooChangeOriginator": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@totalcount": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ResourceName": ""
</code><code><br>}</code>

### operation: Get Change Request
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Change Request Number<br></td><td>ID of the change request whose details you want to retrieve from the Micro Focus Service Manager server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Change": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "close": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ClosureCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ClosingComments": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "header": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Open": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Phase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Reason": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Company": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ChangeID": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "CloseTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "AssignedTo": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "PlannedEnd": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ChangeModel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "DateEntered": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "InitiatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Subcategory": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "PlannedStart": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ApprovalStatus": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "BackoutDuration": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ChangeCoordinator": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "middle": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Service": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "CustomerVisible": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description.structure": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Description": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "BackoutMethod": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ChangeOriginator": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": ""
</code><code><br>}</code>

### operation: Update Change
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Change ID<br></td><td>Specify the ID of the change request that you want to update for closure in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Closure Code<br></td><td>Specify the closure code that you want to apply to the change request that you want to update for closure in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>SubClosure Code<br></td><td>Specify the sub-closure code that you want to apply to the change request that you want to update for closure in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Closing Comments<br></td><td>Specify the closing comments that you want to add to the change request that you want to update for closure in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Phase<br></td><td>Specify the phase of the change request that you want to update for closure in the Micro Focus Service Manager server. You can specify phases such as logging, approve, close, etc.<br>
</td></tr><tr><td>Actual Start Time<br></td><td>(Optional) Select the actual start DateTime of the change request that you want to update for closure in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Actual End Time<br></td><td>(Optional) Enter the actual end DateTime of the change request that you want to update for closure in the Micro Focus Service Manager server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "SubClosureCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Change": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "close": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ClosureCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ClosingComments": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "header": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Open": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Phase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Reason": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Company": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ChangeID": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "CloseTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "PlannedEnd": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ChangeModel": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "DateEntered": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "InitiatedBy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Subcategory": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "PlannedStart": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ApprovalStatus": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "AssignmentGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ChangeCoordinator": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "middle": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Service": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "CustomerVisible": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description.structure": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Description": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "OoredooChangeOriginator": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": ""
</code><code><br>}</code>

### operation: Create RF - Request Fulfillment Ticket
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Title or Brief Description<br></td><td>Title or brief description of the Request Fulfillment Ticket (RF) that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Description<br></td><td>Description of the Request Fulfillment Ticket (RF) that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Category<br></td><td>Category to be assigned to the RF that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Subcategory<br></td><td>Subcategory to be assigned to the RF that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Assigned To<br></td><td>Name of the user to whom you want to assign the RF that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Assigned Group<br></td><td>The ID of the group to which you want to assign the RF that you want to create on the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Impact<br></td><td>Impact number to be assigned to the RF that you want to create on the Micro Focus Service Manager server. For example, 4 is 'No Service Impact'.<br>
</td></tr><tr><td>Priority<br></td><td>Priority value to be assigned to the RF that you want to create on the Micro Focus Service Manager server. For example, 4 is 'Low'.<br>
</td></tr><tr><td>Urgency<br></td><td>Urgency value to be assigned to the RF that you want to create on the Micro Focus Service Manager server. For example, 4 is 'Low'.<br>
</td></tr><tr><td>Product Type<br></td><td>Product Type to be assigned to the RF that you want to create on the Micro Focus Service Manager server. For example, other.<br>
</td></tr><tr><td>Requester Name<br></td><td>Name of the Requester, who has raised the RF that you want to create on the Micro Focus Service Manager server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Request": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Open": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Impact": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Number": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Urgency": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "SlaBreach": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AssignedTo": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "SubmitDate": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "UpdateDate": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "CustVisible": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Description": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ProductType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Subcategory": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AgreementIds": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "CurrentPhase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "DeliveryDate": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AssignedGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "RequestorName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ApprovalStatus": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "BriefDescription": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": ""
</code><code><br>}</code>

### operation: Get RF - Request Fulfillment Ticket
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>RF - Request Fulfillment Ticket Number<br></td><td>The ID of the Request Fulfillment Ticket whose details you want to retrieve from the Micro Focus Service Manager server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Request": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Open": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Impact": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Number": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Urgency": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "SlaBreach": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AssignedTo": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "SubmitDate": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "UpdateDate": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "CustVisible": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Description": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ProductType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Subcategory": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AgreementIds": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "CurrentPhase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "DeliveryDate": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "AssignedGroup": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "RequestorName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "ApprovalStatus": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "BriefDescription": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": ""
</code><code><br>}</code>

### operation: Update RF - Request Fulfillment Ticket for an attachment
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>RF-Request Fulfillment Ticket ID <br></td><td>The ID of the Request Fulfillment Ticket to which you want to add the attachment in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Attachment Name<br></td><td>The name of the attachment name that you want to add to the specified RF in the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Message Body<br></td><td>The content of the file to be uploaded to the specified RF in the Micro Focus Service Manager server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ResourceName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "content": []
</code><code><br>}</code>

### operation: Retrieve Attachment Information
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident ID<br></td><td>ID of the incident whose details you want to retrieve from the Micro Focus Service Manager server.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@start": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "@totalcount": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ResourceName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ReturnCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "content": []
</code><code><br>}</code>

### operation: Download Attachment
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident ID<br></td><td>ID of the incident associated with the Attachment which you want to download from the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Attachment ID<br></td><td>ID of the attachment which you want to download from the Micro Focus Service Manager server.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Delete Attachment
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Incident ID<br></td><td>ID of the incident associated with the Attachment which you want to delete from the Micro Focus Service Manager server.<br>
</td></tr><tr><td>Attachment ID<br></td><td>ID of the attachment which you want to delete from the Micro Focus Service Manager server.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
## Included playbooks
The `Sample - micro-focus-service-manager - 1.3.1` playbook collection comes bundled with the Micro Focus Service Manager connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Micro Focus Service Manager connector.

- Change: Create Change
- Change: Get Change List
- Change: Get Change Request
- Create RF
- Device: Get Device
- Device: Get Device List
- Get RF
- Incident: Create Incident
- Incident: Get Incident
- Incident: Get Incident List
- Incident: Update Incident
- Update Change
- Update RF

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
