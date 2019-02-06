from error import Error

class ModelNotFound(Exception):
    pass

def generate_resources(response, client=None):
    from person import Me, Person, ProjectMembership
    from project import Project
    from story import Story, Epic, Task
    from metadata import Label

    def generate(resource):
        kind = resource['kind']

        print "generating {}".format(kind)

        resource_class = {
            'project': Project,
            'me': Me,
            'story': Story,
            'epic': Epic,
            'label': Label,
            'error': Error,
            'project_membership': ProjectMembership,
            'person': Person,
            'task': Task
        }.get(kind)

        if resource_class is None:
            raise ModelNotFound("No model found for {}".format(kind))

        return resource_class(**resource)

    response = response.json()

    if isinstance(response, list):
        return (generate(resource) for resource in response)
    else:
        return generate(response)






