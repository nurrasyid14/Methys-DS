#ifndef METHYS_DATABASE_H
#define METHYS_DATABASE_H

#include "methys/core.h"

typedef enum methys_database_dialect {
    METHYS_DATABASE_POSTGRES = 1,
    METHYS_DATABASE_MONGODB = 2
} methys_database_dialect;

typedef enum methys_database_status {
    METHYS_DATABASE_OK = 0,
    METHYS_DATABASE_INVALID_ARGUMENT = 1,
    METHYS_DATABASE_NOT_IMPLEMENTED = 2,
    METHYS_DATABASE_CONNECTION_ERROR = 3,
    METHYS_DATABASE_QUERY_ERROR = 4
} methys_database_status;

typedef struct methys_database_connection methys_database_connection;
typedef struct methys_database_result methys_database_result;

/**
 * Connect with a backend-specific URI and return an opaque native handle.
 * Credentials must remain in the host application, never frontend blocks.
 */
METHYS_API methys_database_status methys_database_connect(
    methys_database_dialect dialect,
    const char *connection_uri,
    methys_database_connection **out_connection
);

/**
 * Execute a parameterised query. parameters_json is a UTF-8 JSON object and
 * will be decoded and bound by the backend adapter, never interpolated.
 */
METHYS_API methys_database_status methys_database_query(
    methys_database_connection *connection,
    const char *statement,
    const char *parameters_json,
    methys_database_result **out_result
);

METHYS_API void methys_database_result_free(methys_database_result *result);
METHYS_API void methys_database_close(methys_database_connection *connection);

#endif
