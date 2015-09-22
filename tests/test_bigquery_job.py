#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from izberg_bigquery import BigQueryJob


class TestBigQueryJob(unittest.TestCase):

    def test_wait_checks_for_job_completion(self):
        responses = (r for r in ((False, None), (False, None), (True, None)))
        client_mock = mock.Mock()
        client_mock.check_job.side_effect = lambda jid: next(responses)

        job = BigQueryJob(client_mock, mock.sentinel.job_id)
        job.wait()

        self.assertEqual(client_mock.check_job.call_args_list, [
            mock.call(mock.sentinel.job_id),
            mock.call(mock.sentinel.job_id),
            mock.call(mock.sentinel.job_id),
        ])
