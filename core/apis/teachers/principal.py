from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema
principal_teachers_resources = Blueprint("principal_teachers_resources", __name__)


@principal_teachers_resources.route("/teachers", methods=["GET"], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """List all teachers"""
    teachers = Teacher.query.all()
    teachers_dump = TeacherSchema(many=True).dump(teachers)
    return APIResponse.respond(data=teachers_dump)
