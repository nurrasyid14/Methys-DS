#define METHYS_CORE_EXPORTS
#include "methys/database.h"

/*
 * This file establishes the stable driver-independent ABI. PostgreSQL (libpq)
 * and MongoDB (mongoc) adapters are deliberately deferred until their external
 * libraries are added to the build and deployment toolchain.
 */
struct methys_database_connection {
    methys_database_dialect dialect;
};

struct methys_database_result {
    unsigned int reserved;
};

methys_database_status methys_database_connect(
    methys_database_dialect dialect,
    const char *connection_uri,
    methys_database_connection **out_connection
) {
    if (connection_uri == 0 || out_connection == 0) {
        return METHYS_DATABASE_INVALID_ARGUMENT;
    }
    if (dialect != METHYS_DATABASE_POSTGRES && dialect != METHYS_DATABASE_MONGODB) {
        return METHYS_DATABASE_INVALID_ARGUMENT;
    }
    *out_connection = 0;
    return METHYS_DATABASE_NOT_IMPLEMENTED;
}

methys_database_status methys_database_query(
    methys_database_connection *connection,
    const char *statement,
    const char *parameters_json,
    methys_database_result **out_result
) {
    (void)parameters_json;
    if (connection == 0 || statement == 0 || out_result == 0) {
        return METHYS_DATABASE_INVALID_ARGUMENT;
    }
    *out_result = 0;
    return METHYS_DATABASE_NOT_IMPLEMENTED;
}

void methys_database_result_free(methys_database_result *result) {
    (void)result;
}

void methys_database_close(methys_database_connection *connection) {
    (void)connection;
}
