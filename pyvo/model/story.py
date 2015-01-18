from base import PivotalResource, Instantiated, TimeZone, fields, \
    OneOf, PostValidators, RequiredOnPost


class Story(Instantiated, PivotalResource):
    name = fields.StringField()
    description = fields.StringField(validators=PostValidators(RequiredOnPost()))
    story_type = fields.StringField(
        validators=OneOf('feature', 'bug', 'chore', 'release')
    )
    current_state = fields.StringField(
        validators=OneOf('accepted', 'delivered', 'finished',
            'started', 'rejected', 'planned', 'unstarted', 'unscheduled')
    )
    estimate = fields.FloatField()
    accepted_at = fields.DateTimeField()
    deadline = fields.DateTimeField()
    requested_by_id = fields.IntField()
    owned_by_id = fields.IntField()
    owner_ids = fields.ListField()
    label_ids = fields.ListField()
    task_ids = fields.ListField()
    follower_ids = fields.ListField()
    comment_ids = fields.ListField()
    before_id = fields.IntField()
    after_id = fields.IntField()
    integration_id = fields.IntField()
    external_id = fields.StringField()
    url = fields.StringField()


class Task(Instantiated, PivotalResource):
    story_id = fields.IntField()
    description = fields.StringField(validators=PostValidators(RequiredOnPost()))
    complete = fields.BoolField()
    position = fields.IntField()
