import os

import pytest

from tests.consts import examples_path
from valohai_yaml import parse


def _load_config(filename, roundtrip):
    with open(os.path.join(examples_path, filename), 'r') as infp:
        config = parse(infp)
    if roundtrip:
        config = parse(config.serialize())
    return config


def config_fixture(name):
    @pytest.fixture(params=[False, True])
    def _config_fixture(request):
        return _load_config(name, request.param)

    return _config_fixture
