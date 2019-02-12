from jsonmodels import models, fields
from jsonmodels.validators import ValidationError


class PivotalResource(models.Base):
    @classmethod
    def with_client(cls, client, **data):
        resource = cls(**data)
        resource.client = client
        return resource

    kind = fields.StringField()

    def validate_on_post(self):
        for _, field in self:
            for postval in [v for v in field.validators
                    if isinstance(v, PostValidators)]:
                for val in postval.validators:
                    value = field.__get__(self)
                    try:
                        val.validate(value)
                    except AttributeError:
                        val(value)


class Instantiated(object):
    id = fields.IntField(required=True)
    created_at = fields.DateTimeField()
    # Creation time. This field is read only.
    updated_at = fields.DateTimeField()
    # Time of last update. This field is read only.

    def __str__(self):
        return "id='{}'".format(self.id)


class OneOf(object):
    """Ensure StringField value belongs to a given enum"""
    def __init__(self, *args):
        super(OneOf, self).__init__()
        self.args = args

    def validate(self, value):
        if value is not None and value not in self.args:
            raise ValidationError("Value must be one of %s" %
                ", ".join(map(str, self.args)))


class RequiredOnPost(object):
    """Ensure value is present during a POST operation"""
    def validate(self, value):
        if value is None:
            raise ValidationError("Value required on POST operation.")


class PostValidators(object):
    def __init__(self, *args):
        self.validators = args

    def validate(self, value):
        pass
