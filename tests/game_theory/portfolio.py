import os
import pandas as pd

from mango.constants import (
    PROJECT_PATH,
    TESTING_PRECISION
)

from mango.portfolio import Account

csv_path_x = os.path.join(PROJECT_PATH, "sample", "ex_1_x.csv")
data_x = pd.read_csv(csv_path_x)

x = Account(
    name='x',
    events=data_x['event'],
    probs=data_x['probability'],
    losses=data_x['loss']
)


def test_name_x():
    assert x.name == 'x'


def test_el_x():

    assert 1290 == round(
        number=x.expected_loss,
        ndigits=TESTING_PRECISION
    )


def test_variance_x():

    assert 19619900 == round(
        number=x.variance,
        ndigits=TESTING_PRECISION
    )


def test_std_dev_x():
    assert 4429.43562996 == round(
        number=x.std_dev,
        ndigits=TESTING_PRECISION
    )


csv_path_y = os.path.join(PROJECT_PATH, "sample", "ex_1_y.csv")
data_y = pd.read_csv(csv_path_y)

y = Account(
    name='y',
    events=data_y['event'],
    probs=data_y['probability'],
    losses=data_y['loss']
)


def test_name_y():
    assert y.name == 'y'


def test_el_y():

    assert 179 == round(
        number=y.expected_loss,
        ndigits=TESTING_PRECISION
    )


def test_variance_y():

    assert 377959 == round(
        number=y.variance,
        ndigits=TESTING_PRECISION
    )


def test_std_dev_y():
    assert 614.7837018 == round(
        number=y.std_dev,
        ndigits=TESTING_PRECISION
    )
