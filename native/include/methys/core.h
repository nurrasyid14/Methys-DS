#ifndef METHYS_CORE_H
#define METHYS_CORE_H

#ifdef _WIN32
#  ifdef METHYS_CORE_EXPORTS
#    define METHYS_API __declspec(dllexport)
#  else
#    define METHYS_API __declspec(dllimport)
#  endif
#else
#  define METHYS_API __attribute__((visibility("default")))
#endif

/** Return the semantic version of the native Methys API. */
METHYS_API const char *methys_core_version(void);

/** Database dialects accepted by the native inline-query API. */
typedef enum methys_query_dialect {
    METHYS_QUERY_POSTGRES = 1,
    METHYS_QUERY_MONGODB = 2
} methys_query_dialect;

/**
 * Report whether a dialect is recognised by this build.
 *
 * Driver-backed execution will be added behind this C API. Connection strings,
 * credentials, and result ownership are deliberately not exposed to Python.
 */
METHYS_API int methys_query_dialect_supported(methys_query_dialect dialect);

#endif
