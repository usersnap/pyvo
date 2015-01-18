# -*- coding: utf-8 -*-

import datetime
import pytest

from pyvo.model.base import ValidationError
from pyvo.model.project import Project, MembershipSummary
from pyvo.model.person import Me

project_input = {
    u'version': 166,
    u'velocity_averaged_over': 3,
    u'updated_at': u'2015-01-13T05:48:40Z',
    u'iteration_length': 1,
    u'enable_tasks': True,
    u'id': 1040058,
    u'week_start_day': u'Monday',
    u'point_scale_is_custom': False,
    u'atom_enabled': False,
    u'public': False,
    u'account_id': 490825,
    u'bugs_and_chores_are_estimatable': False,
    u'automatic_planning': True,
    u'start_time': u'2014-09-22T04:00:00Z',
    u'enable_following': True,
    u'initial_velocity': 10,
    u'number_of_done_iterations_to_show': 12,
    u'kind': u'project',
    u'name': u'design chores',
    u'enable_incoming_emails': True,
    u'current_iteration_number': 17,
    u'point_scale': u'0,1,2,4,8',
    u'time_zone': {
        u'olson_name': u'America/New_York',
        u'kind': u'time_zone',
        u'offset': u'-05:00'
    },
    u'has_google_domain': False,
    u'created_at': u'2014-03-18T18:03:55Z'
}

me_input = {u'username': u'bourke', u'kind': u'me', u'has_google_identity': False, u'name': u'Michael Bourke', u'updated_at': u'2015-01-16T23:27:23Z', u'created_at': u'2013-02-08T03:31:37Z', u'time_zone': {u'olson_name': u'America/New_York', u'kind': u'time_zone', u'offset': u'-05:00'}, u'email': u'michael@iter8ve.com', u'receives_in_app_notifications': True, u'api_token': u'2a2c2003c8e45a643ad8af2b066b3e71', u'id': 914193, u'projects': [{u'kind': u'membership_summary', u'project_name': u'Globurg 1', u'project_color': u'91a400', u'last_viewed_at': u'2013-11-19T17:29:31Z', u'role': u'owner', u'project_id': 756957, u'id': 2819161}, {u'kind': u'membership_summary', u'project_name': u'Marco Polo', u'project_color': u'74a4d7', u'last_viewed_at': u'2013-05-04T14:12:44Z', u'role': u'owner', u'project_id': 816071, u'id': 3056727}, {u'kind': u'membership_summary', u'project_name': u'Globurg Forward', u'project_color': u'71be00', u'last_viewed_at': u'2013-06-24T18:22:57Z', u'role': u'owner', u'project_id': 818429, u'id': 3067627}, {u'kind': u'membership_summary', u'project_name': u'Event search', u'project_color': u'ac3f65', u'last_viewed_at': u'2014-12-02T15:31:52Z', u'role': u'owner', u'project_id': 973294, u'id': 3750076}, {u'kind': u'membership_summary', u'project_name': u'design chores', u'project_color': u'555555', u'last_viewed_at': u'2014-12-12T21:57:30Z', u'role': u'owner', u'project_id': 1040058, u'id': 4058924}, {u'kind': u'membership_summary', u'project_name': u'Website', u'project_color': u'8100ea', u'last_viewed_at': u'2014-08-04T14:00:51Z', u'role': u'owner', u'project_id': 1137686, u'id': 4515778}, {u'kind': u'membership_summary', u'project_name': u'Search Tool', u'project_color': u'e46642', u'last_viewed_at': u'2014-08-04T13:26:45Z', u'role': u'owner', u'project_id': 1137688, u'id': 4515782}, {u'kind': u'membership_summary', u'project_name': u'ALG', u'project_color': u'ce9f00', u'last_viewed_at': u'2015-01-16T17:06:07Z', u'role': u'owner', u'project_id': 1138154, u'id': 4516928}], u'initials': u'MSB'}

def describe_project_schema():

    def it_loads_json():
        project = Project(**project_input)
        assert project.name == "design chores"

    def it_requires_name_on_post():
        project = Project(point_scale='0,1,2,4,8', public=False)
        with pytest.raises(ValidationError) as excinfo:
            project.validate_on_post()
        assert "Value required on POST operation." in excinfo.value

def describe_me_resource():

    def it_loads_json():
        me = Me(**me_input)
        assert me.username == "bourke"
        for mship in me.projects:
            assert isinstance(mship, MembershipSummary)
            assert isinstance(mship.last_viewed_at, datetime.datetime)