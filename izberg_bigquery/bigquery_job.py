class BigQueryJob(object):

    def __init__(self, client, job_id):
        self._client = client
        self._job_id = job_id

    def wait(self):
        complete = False

        while not complete:
            complete, row_count = self._client.check_job(self._job_id)
