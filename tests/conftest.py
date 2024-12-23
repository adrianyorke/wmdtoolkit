from collections.abc import Generator
from pathlib import Path

import pytest
from pyspark.sql import SparkSession

from wmdtoolkit.core.application_metadata import ApplicationMetadata

TEST_ROOT = Path(__file__).parent

@pytest.fixture
def spark() -> Generator:
    spark = SparkSession.builder.master("local[1]").appName("unit-tests").getOrCreate()
    yield spark
    spark.stop()
