class InvalidMetadataAttributeException(Exception):
    """Invalid metadata attribute exception class."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class ApplicationMetadata:
    """ApplicationMetadata class used to store environment, application name, task name and ds/do group."""

    VALID_ENVIRONMENTS = [
        "dev",
        "test",
        "dsws",
        "prod",
    ]

    def __init__(
        self,
        environment,
        application,
        task_name,
        ds_do_group,
    ) -> None:
        """Class constructor.

        Parameters
        ----------
        environment : str
            OPDP/Databricks/Cloud Environment (dev, test, dsws or prod).
        application : str
            Application name.
        task_name : str
            Task name in Databricks job.
        ds_do_group : str
            Data Science or DataOps group.

        Raises
        ------
        InvalidMetadataAttributeException
            If a metadata attribute is missing or not a valid string type.
        """

        if environment is None or not isinstance(environment, str) or environment not in self.VALID_ENVIRONMENTS:
            raise InvalidMetadataAttributeException(
                f"Invalid value '{application}' for 'application' metadata attribute."
            )
        if application is None or not isinstance(application, str):
            raise InvalidMetadataAttributeException(
                f"Invalid value '{application}' for 'application' metadata attribute."
            )
        if environment is None or not isinstance(environment, str):
            raise InvalidMetadataAttributeException(
                f"Invalid value '{application}' for 'application' metadata attribute."
            )
        if environment is None or not isinstance(environment, str):
            raise InvalidMetadataAttributeException(
                f"Invalid value '{application}' for 'application' metadata attribute."
            )

        self.environment = environment
        self.application = application
        self.task_name = task_name
        self.ds_do_group = ds_do_group
