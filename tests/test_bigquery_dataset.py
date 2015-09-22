#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from bigquery import JOB_WRITE_TRUNCATE

from izberg_bigquery import (
    BigQueryJob,
    BigQueryService,
)


class TestBigQueryDataset(unittest.TestCase):

    def setUp(self):
        self.client_mock = mock.Mock()

        self.client_mock.write_to_table.return_value = {
            'jobReference': {
                'jobId': mock.sentinel.job_id
            }
        }

        self.service = BigQueryService(self.client_mock)

    def test_write_to_table_returns_a_biquery_job_object(self):
        dataset = self.service.dataset(mock.sentinel.dataset)

        result = dataset.write_to_table(
            mock.sentinel.sql,
            mock.sentinel.table,
            mock.sentinel.write_disposition
        )

        self.assertIsInstance(result, BigQueryJob)

    def test_write_to_truncated_table_returns_uses_job_write_truncate(self):
        dataset = self.service.dataset(mock.sentinel.dataset)

        dataset.write_to_truncated_table(
            mock.sentinel.sql,
            mock.sentinel.table
        )

        self.client_mock.write_to_table.assert_called_with(
            mock.sentinel.sql,
            mock.sentinel.dataset,
            mock.sentinel.table,
            write_disposition=JOB_WRITE_TRUNCATE
        )
