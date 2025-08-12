import unittest
import dataplatform_knmi_api_request

class TestDataplatformKNMIAPIRequest(unittest.TestCase):

    def test_knmi_coll(self) -> None:
        result = dataplatform_knmi_api_request.DataplatformKNMIAPIRequest().knmi_coll('2020-01-01', '2020-12-31', 'Tx1')
        self.assertIsInstance(result, list)

    def test_knmi_obs(self) -> None:
        result = dataplatform_knmi_api_request.DataplatformKNMIAPIRequest().knmi_obs('2020-01-01', '2020-12-31', 'param')
        self.assertIsInstance(result, list)