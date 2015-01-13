import pytest
import json
import requests

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

def describe_the_pyvo_client():

    @pytest.fixture
    def client():
        from pyvo import Client
        return Client('2a2c2003c8e45a643ad8af2b066b3e71',
            'https://www.pivotaltracker.com/services/v5/')

    def it_returns_valid_responses(client):
        r1 = client.me.get(return_json=False)
        r2 = client.projects.get(return_json=False)

        assert r1.status_code == r2.status_code == 200

    def it_can_return_json(client):
        r1 = client.me.get()
        assert json.dumps(r1)

    def it_maps_attributes_to_url_segments(client):
        r1 = client.projects(id='1040058').get()
        assert r1['kind'] == 'project'

        r2 = client.projects.labels(project_id='1040058', label_id='81231')
        assert r2

    def it_raises_an_exception_for_404s(client):
        from pyvo import ResourceNotFound
        with pytest.raises(ResourceNotFound):
            r1 = client.zod.get()

    def it_returns_a_resource_key_with_a_successful_response(client):
        r1 = client.projects.get(return_json=False)
        assert r1.resource_key == 'projects'

    def it_produces_standalone_instances(client):
        project = client.projects(id='1040058')

        project_json = project.get(return_json=False)
        assert project_json.status_code == 200

        labels = project.labels.get(return_json=False)
        assert labels.status_code == 200
