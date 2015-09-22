#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from izberg_bigquery import (
    BigQueryResult,
    BigQueryService,
)


class TestBigQueryService(unittest.TestCase):

    def setUp(self):
        self.client_mock = mock.Mock()
        self.service = BigQueryService(self.client_mock)

    def test_query_returns_a_biquery_result_object(self):
        self.client_mock.query.return_value = [None, None]

        result = self.service.query(mock.sentinel.sql)

        self.assertIsInstance(result, BigQueryResult)
