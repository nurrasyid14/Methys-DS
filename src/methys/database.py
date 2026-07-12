"""Database query definitions passed to the native Methys engine."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class QueryDialect(str, Enum):
    """Databases supported by Methys inline-query definitions."""

    POSTGRES = "postgres"
    MONGODB = "mongodb"


@dataclass(frozen=True)
class InlineQuery:
    """An immutable query definition for native execution.

    `statement` is SQL for PostgreSQL. For MongoDB it is a document-shaped
    query payload (for example a filter or aggregation specification). The
    native layer will own connection handling, parameter binding, execution,
    and result memory; this Python object only describes a request.
    """

    dialect: QueryDialect
    statement: str
    parameters: dict[str, Any] | None = None

    @classmethod
    def postgres(
        cls, statement: str, parameters: dict[str, Any] | None = None
    ) -> "InlineQuery":
        """Create a parameterised PostgreSQL query definition."""
        return cls(QueryDialect.POSTGRES, statement, parameters)

    @classmethod
    def mongodb(
        cls, document: str, parameters: dict[str, Any] | None = None
    ) -> "InlineQuery":
        """Create a MongoDB filter or aggregation query definition."""
        return cls(QueryDialect.MONGODB, document, parameters)
