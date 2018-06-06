import os

import pytest


@pytest.fixture(params=[
    ('Port of Harwich', '2010-10-10'),
    ('Port of Felixtowe', '2010-10-11'),
    ('Port of Leith', '2019-05-01')
]
)
def date_location(request):
    print('\n--------------------------------------')
    print(f'fixturename     :   {request.fixturename}')
    print(f'scope           :   {request.scope}')
    print(f'function        :   {request.function.__name__}')
    print(f'cls             :   {request.cls}')
    print(f'module          :   {request.module.__name__}')
    print(f'fspath          :   {request.fspath}')
    yield request.param
    os.unlink("/home/lemon/.task-test/pending.data")


@pytest.fixture(params=[
    ('Port of Harwich', '2010-10-10T10:30'),
    ('Port of Felixtowe', '2010-10-11T10:30'),
    ('Port of Leith', '2019-05-01T10:30')
]
)
def date_time_location(request):
    print('\n--------------------------------------')
    print(f'fixturename     :   {request.fixturename}')
    print(f'scope           :   {request.scope}')
    print(f'function        :   {request.function.__name__}')
    print(f'cls             :   {request.cls}')
    print(f'module          :   {request.module.__name__}')
    print(f'fspath          :   {request.fspath}')
    yield request.param
    os.unlink("/home/lemon/.task-test/pending.data")


@pytest.fixture
def date_natural_location():
    yield "20 August 2018"
    os.unlink("/home/lemon/.task-test/pending.data")
