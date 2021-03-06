from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi.domain.profile_traits import ProfileTraits
from tracardi_plugin_sdk.service.plugin_runner import run_plugin
from tracardi_string_validator.plugin import StringValidatorAction


def test_string_validator_plugin():
    payload = {"data": "my@email.com"}
    init = {
        'validation_name': 'email',
        'data': "payload@data"
    }

    plugin = run_plugin(StringValidatorAction, init, payload)

    valid, invalid = plugin.output
    assert invalid.value is None


def test_string_validator_plugin_fails():
    init = {"data": "event@id",
            "validation_name": "time"}
    payload = {}
    profile = Profile(id="profile-id", traits=ProfileTraits(public={"test": "new test"}))
    event = Event(id="event-id",
                  type="event-type",
                  profile=profile,
                  session=Session(id="session-id"),
                  source=Entity(id="source-id"),
                  context=Context())
    plugin = run_plugin(StringValidatorAction, init, payload,
                        profile, None, event)
    valid, invalid = plugin.output
    assert valid.value is None
