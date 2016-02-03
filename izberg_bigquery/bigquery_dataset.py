# -*- coding: utf-8 -*-

from bigquery import JOB_WRITE_TRUNCATE

from .bigquery_job import BigQueryJob


class BigQueryDataset():

    def __init__(self, client, dataset):
        self._client = client
        self._dataset = dataset

    def table_exists(self, table):
        return self._client.check_table(self._dataset, table)

    def table_schema(self, table):
        return self._client.get_table_schema(self._dataset, table)

    def delete_table(self, table):
        return self._client.delete_table(self._dataset, table)

    def create_table(self, table, schema):
        return self._client.create_table(self._dataset, table, schema)

    def update_table(self, table, schema):
        return self._client.update_table(self._dataset, table, schema)

    def write_to_truncated_table(self, sql, table):
        return self.write_to_table(sql, table, JOB_WRITE_TRUNCATE)

    def write_to_table(self, sql, table, write_disposition):
        job = self._client.write_to_table(
            sql,
            self._dataset,
            table,
            write_disposition=write_disposition
        )
        job_id = job['jobReference']['jobId']

        return BigQueryJob(self._client, job_id)
