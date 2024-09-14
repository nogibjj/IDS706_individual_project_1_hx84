import pytest


def test_notebook():
    pytest.main(["--nbval", "../python_ds_project_1.ipynb"])
