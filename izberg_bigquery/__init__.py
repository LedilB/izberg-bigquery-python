# -*- coding: utf-8 -*-
import pkg_resources

from .bigquery_job import BigQueryJob
from .bigquery_result import BigQueryResult
from .bigquery_service import BigQueryService

__all__ = [
    'BigQueryJob',
    'BigQueryResult',
    'BigQueryService',
]
__version__ = pkg_resources.get_distribution(__package__).version
