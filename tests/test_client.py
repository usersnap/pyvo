import pytest
import json
import requests

from pyvo.client import ResponseType

'''
describe the Pyvo client
    it returns valid responses
    it can return json
    it can return the underlying Requests response
    it maps attributes to URL segments
    it raises an exception for 404s
    it returns a resource key with a successful response
    it produces standalone instances
    --TODO--
    it reads an API token from the environment
    it helps implementers manage oauth
'''

@pytest.mark.client
def describe_the_pyvo_client():

    @pytest.fixture
    def client():
        from pyvo import Client
        return Client('2a2c2003c8e45a643ad8af2b066b3e71',
            'https://www.pivotaltracker.com/services/v5/')

    def it_returns_valid_responses(client):
        r1 = client.me.get(response_type=ResponseType.RAW)
        r2 = client.projects.get(response_type=ResponseType.RAW)

        assert r1.status_code == r2.status_code == 200

    def it_can_return_json(client):
        r1 = client.me.get(response_type=ResponseType.JSON)
        assert json.dumps(r1)

    def it_maps_attributes_to_url_segments(client):
        r1 = client.projects(id='1040058').get(response_type=ResponseType.JSON)
        assert r1['kind'] == 'project'

        r2 = client.projects.labels(project_id='1040058', label_id='81231')
        assert r2

    def it_raises_an_exception_for_404s(client):
        from pyvo import ResourceNotFound
        with pytest.raises(ResourceNotFound):
            r1 = client.zod.get(response_type=ResponseType.JSON)

    def it_produces_standalone_instances(client):
        project = client.projects(id='1040058')

        project_json = project.get(response_type=ResponseType.RAW)
        assert project_json.status_code == 200

        labels = project.labels.get(response_type=ResponseType.RAW)
        assert labels.status_code == 200

    @pytest.mark.resource
    def it_produces_resource_entities(client):
        from pyvo.model.project import Project
        from pyvo.model.metadata import Label
        from pyvo.model.story import Story

        project = client.projects(id='1040058')

        p = project.get()
        assert isinstance(p, Project)

        labels = project.labels.get()
        for label in labels:
            assert isinstance(label, Label)
            assert label.project_id == 1040058

        stories = project.stories.get()
        for story in stories:
            assert isinstance(story, Story)
            assert story.story_type in ('feature', 'bug', 'chore', 'release')

