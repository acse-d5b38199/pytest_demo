import pytest
import sys
from functions import myp1
sys.path.insert(0, '/Users/jz2222/Desktop/ICL/MPM-test')


class TestFunctions(object):

    @pytest.mark.parametrize('xin, xout', [(1, 2), (3, 4), (6, 7), (8, 9)])
    def test_myp1(self, xin, xout):
        result = myp1(xin)
        assert result == xout

    def test_myp1_single(self):
        result = myp1(2)
        assert result == 3
