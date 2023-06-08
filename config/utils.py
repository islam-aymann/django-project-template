from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"

    @classmethod
    def _missing_(cls, value: str) -> "Environment":
        if "dev" in value:
            return cls.DEVELOPMENT

        elif "test" in value or "qa" in value:
            return cls.TESTING

        elif "stag" in value or "stg" in value:
            return cls.STAGING

        elif "pro" in value:
            return cls.PRODUCTION

    @property
    def is_development(self) -> bool:
        return self == self.DEVELOPMENT

    @property
    def is_testing(self) -> bool:
        return self == self.TESTING

    @property
    def is_staging(self) -> bool:
        return self == self.STAGING

    @property
    def is_production(self) -> bool:
        return self == self.PRODUCTION

    @property
    def is_local(self) -> bool:
        return self.is_development or self.is_testing
