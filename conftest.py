# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests


@pytest.fixture(scope='session')
def capabilities(capabilities):
    capabilities.setdefault('tags', []).append('oneanddone')
    return capabilities


@pytest.fixture
def persona_test_user():
    return requests.get('http://personatestuser.org/email').json()


@pytest.fixture(scope='function')
def new_user(persona_test_user):
    return {
        'email': persona_test_user['email'],
        'password': persona_test_user['pass'],
        'name': persona_test_user['email'].split('@')[0],
        'username': persona_test_user['email'].split('@')[0],
        'url': 'http://www.mozilla.org/'
    }
