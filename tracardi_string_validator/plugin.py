from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result

from tracardi_string_validator.model.configuration import Configuration
from tracardi_string_validator.service.validator import Validator


class StringValidatorAction(ActionRunner):
    def __init__(self, **kwargs):
        self.config = Configuration(**kwargs)
        self.validator = Validator(self.config)

    async def run(self, payload):
        if self.validator.check():
            return Result(port='payload', value=True)
        else:
            return Result(port='payload', value=False)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_string_validator.plugin',
            className='StringValidatorAction',
            inputs=["payload"],
            outputs=["payload"],
            init={
                'validation_name': None,
                'data': None
            },
            version='0.1.1',
            license="MIT",
            author="Patryk Migaj"

        ),
        metadata=MetaData(
            name='String validator',
            desc='Validates data such as: email, url, ipv4, date, time,int,float, phone number, ean code',
            type='flowNode',
            width=200,
            height=100,
            icon='validator',
            group=["Validators"]
        )
    )
