#ifndef SINGLIST_GLOBAL_H
#define SINGLIST_GLOBAL_H

#include <QtCore/qglobal.h>

#if defined(SINGLIST_LIBRARY)
#  define SINGLIST_EXPORT Q_DECL_EXPORT
#else
#  define SINGLIST_EXPORT Q_DECL_IMPORT
#endif

#endif // SINGLIST_GLOBAL_H
