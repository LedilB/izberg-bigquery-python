import unittest
import mock

from izberg_bigquery import BigQueryResult


class TestBigQueryResult(unittest.TestCase):

    def test_first_returns_the_first_result(self):
        client_mock = mock.Mock()
        client_mock.check_job.return_value = (True, None)
        client_mock.get_query_rows.return_value = ['foo', 'bar']

        result = BigQueryResult(client_mock, None).first()

        self.assertEqual(result, 'foo')
