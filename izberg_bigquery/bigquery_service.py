# -*- coding: utf-8 -*-

from bigquery import (
    JOB_WRITE_TRUNCATE,
    get_client,
)

from .bigquery_job import BigQueryJob
from .bigquery_result import BigQueryResult


class BigQueryService(object):

    @classmethod
    def from_private_key_file(cls, project_id, service_account,
                              private_key_file, readonly=False):
        with open(private_key_file, 'r') as fd:
            private_key = fd.read()

        client = get_client(
            project_id,
            service_account=service_account,
            private_key=private_key,
            readonly=readonly
        )

        return cls(client)

    def __init__(self, client):
        self._client = client

    def query(self, sql):
        job_id, _ = self._client.query(sql)

        return BigQueryResult(self._client, job_id)

    def table_exists(self, dataset, table):
        return self._client.check_table(dataset, table)

    def delete_table(self, dataset, table):
        return self._client.delete_table(dataset, table)

    def create_table(self, dataset, table, schema):
        return self._client.create_table(dataset, table, schema)

    def write_to_truncated_table(self, sql, dataset, table):
        return self.write_to_table(sql, dataset, table, JOB_WRITE_TRUNCATE)

    def write_to_table(self, sql, dataset, table, write_disposition):
        job = self._client.write_to_table(
            sql,
            dataset,
            table,
            write_disposition=write_disposition
        )
        job_id = job['jobReference']['jobId']

        return BigQueryJob(self._client, job_id)
