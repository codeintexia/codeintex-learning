import os

from .dev import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get(
            "CODEINTEX_TEST_DB_NAME",
            "codeintex_learning_test",
        ),
        "USER": os.environ.get(
            "CODEINTEX_TEST_DB_USER",
            "codeintex_test",
        ),
        "PASSWORD": os.environ.get(
            "CODEINTEX_TEST_DB_PASSWORD",
            "",
        ),
        "HOST": os.environ.get(
            "CODEINTEX_TEST_DB_HOST",
            "localhost",
        ),
        "PORT": os.environ.get(
            "CODEINTEX_TEST_DB_PORT",
            "5432",
        ),
    }
}
