from .bigquery_job import BigQueryJob


class BigQueryResult(BigQueryJob):

    def rows(self):
        self.wait()
        return self._client.get_query_rows(self._job_id)

    def first(self):
        return self.rows()[0]
