from base import PivotalResource, Instantiated, fields, \
    OneOf, PostValidators, RequiredOnPost
from metadata import TimeZone, Label



class Story(Instantiated, PivotalResource):
    name = fields.StringField()
    description = fields.StringField(validators=PostValidators(RequiredOnPost()))
    story_type = fields.StringField(validators=OneOf('feature', 'bug', 'chore', 'release'))
    current_state = fields.StringField(
        validators=OneOf('accepted', 'delivered', 'finished',
                         'started', 'rejected', 'planned', 'unstarted', 'unscheduled')
    )
    estimate = fields.FloatField()
    accepted_at = fields.DateTimeField()
    deadline = fields.DateTimeField()
    requested_by_id = fields.IntField()
    owned_by_id = fields.IntField()
    owner_ids = fields.ListField(int)
    label_ids = fields.ListField(int)
    task_ids = fields.ListField(int)
    follower_ids = fields.ListField(int)
    comment_ids = fields.ListField(int)
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


class Epic(Instantiated, PivotalResource):
    project_id = fields.IntField()
    name = fields.StringField(validators=PostValidators(RequiredOnPost()))
    label_id = fields.IntField()
    label = fields.EmbeddedField(Label)
    description = fields.StringField()
    comment_ids = fields.ListField()
    follower_ids = fields.ListField()
    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()
    after_id = fields.IntField()
    before_id = fields.IntField()
    past_done_story_estimates = fields.FloatField()
    past_done_stories_count = fields.IntField()
    past_done_stories_no_point_count = fields.IntField()
    url = fields.StringField()

class FileAttachment(Instantiated, PivotalResource):
    filename = fields.StringField()
    created_at = fields.DateTimeField()
    uploader_id = fields.IntField()
    thumbnailable = fields.BoolField()
    height = fields.IntField()
    width = fields.IntField()
    size = fields.IntField()
    download_url = fields.StringField()
    content_type = fields.StringField()
    uploaded = fields.BoolField()
    big_url = fields.StringField()
    thumbnail_url = fields.StringField()
    kind = fields.StringField()

class Comment(Instantiated, PivotalResource):
    story_id = fields.IntField()
    epic_id = fields.IntField()
    text = fields.StringField()
    person_id = fields.IntField()
    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()
    file_attachment_ids = fields.ListField(int)
    google_attachment_ids = fields.ListField()
    attachment_ids = fields.ListField()
    commit_identifier = fields.StringField()
    commit_type = fields.StringField()
    kind = fields.StringField()
