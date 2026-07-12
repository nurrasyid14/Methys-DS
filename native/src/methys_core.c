#define METHYS_CORE_EXPORTS
#include "methys/core.h"

const char *methys_core_version(void) {
    return "0.1.0";
}

int methys_query_dialect_supported(methys_query_dialect dialect) {
    return dialect == METHYS_QUERY_POSTGRES || dialect == METHYS_QUERY_MONGODB;
}
