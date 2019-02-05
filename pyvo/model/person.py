from base import PivotalResource, Instantiated, fields, OneOf
from metadata import TimeZone
from project import MembershipSummary


class Me(Instantiated, PivotalResource):

    name = fields.StringField()
    initials = fields.StringField()
    username = fields.StringField()
    time_zone = fields.EmbeddedField(TimeZone)
    api_token = fields.StringField()
    has_google_identity = fields.BoolField()
    projects = fields.ListField(MembershipSummary)
    workspace_ids = fields.ListField()
    email = fields.StringField()
    receives_in_app_notifications = fields.BoolField()


class Person(Instantiated, PivotalResource):

    name = fields.StringField(required=True)
    email = fields.StringField(required=True)
    initials = fields.StringField()
    username = fields.StringField()
    kind = fields.StringField()

class ProjectMembership(Instantiated, PivotalResource):

    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()
    person_id = fields.IntField()
    project_id = fields.IntField()
    role = fields.StringField(
        validators=OneOf('owner',
            'member', 'viewer', 'inactive'))
    project_color = fields.StringField()
    favorite = fields.BoolField()
    last_viewed_at = fields.DateTimeField()
    wants_comment_notification_emails = fields.BoolField()
    will_receive_mention_notifications_or_emails = fields.BoolField()
    kind = fields.StringField()
    person = fields.EmbeddedField(Person)