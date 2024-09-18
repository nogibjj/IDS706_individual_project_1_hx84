import pytest
"""
Deprecated. Now test jupyter notebook with `make test`.
"""

def test_notebook():
    pytest.main(["--nbval", "../python_ds_project_1.ipynb"])
