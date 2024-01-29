import platform
import requests

from zou import __version__

from zou.app.models.organisation import Organisation
from zou.app.models.person import Person

from zou.app.services import stats_service

from zou.app import config


def send_main_infos():
    """
    Send main usage informations to the CGWire website.

    These infos are used to estimate the size of the Kitsu user community.
    """

    organisation = Organisation.query.first()
    stats = stats_service.get_main_stats()
    nb_active_users = Person.query.filter_by(active=True).count()

    data = {
        "organisation_id": str(organisation.id),
        "nb_active_users": nb_active_users,
        "nb_movie_previews": stats["number_of_video_previews"],
        "nb_picture_previews": stats["number_of_picture_previews"],
        "nb_model_previews": stats["number_of_model_previews"],
        "nb_comments": stats["number_of_comments"],
        "api_version": __version__,
        "python_version": platform.python_version(),
    }

    if config.DEBUG:
        url = "http://localhost:8000/api/selfhosted/telemetry/new/"
    else:
        url = "https://account.cg-wire.com/api/selfhosted/telemetry/new/"

    requests.post(url, json=data)
