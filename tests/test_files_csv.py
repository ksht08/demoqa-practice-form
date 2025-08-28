import os
import pytest
import csv
from pprint import pprint

# pytest tests/test_files_csv.py --noconftest  -v -s

TMP_DIR = os.path.join(os.path.dirname(__file__), '..', 'TMP')
CSV_FILE = "users.csv"
CSV_FILE_PATH = os.path.join(TMP_DIR, CSV_FILE)
AGE_OF_ADULT = 18

@pytest.fixture()
def user_list():
    """
    Read CSV data and return a list of users.
    """
    with open(CSV_FILE_PATH) as csv_file:
        users = list(csv.DictReader(csv_file, delimiter=';'))
    return users

@pytest.fixture()
def workers_list(user_list):
    """
    Create a list of workers from the users list.
    """
    workers = []
    for user in user_list:
        if user["status"] == "worker":
           workers.append(user)
    return workers

def worker_adult(worker):
    return int(worker["age"]) >= AGE_OF_ADULT


def test_workers_are_adult(workers_list):
    """
    Testing what workers are adults.
    """
    for worker in workers_list:
        assert worker_adult(worker), f"Worker {worker['name']} is not an adult."
