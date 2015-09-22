# -*- coding: utf-8 -*-

from bigquery import get_client

from .bigquery_dataset import BigQueryDataset
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

    def dataset(self, dataset):
        return BigQueryDataset(self._client, dataset)
