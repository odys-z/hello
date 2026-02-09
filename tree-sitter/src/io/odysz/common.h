#include <string>
#include <map>

namespace anson {
using namespace std;

#define JavaConstr string

template<typename T>
class JavaConsts {
public:
    T v;
    map<string, T> nmp;

    JavaConsts(T v) : nmp(), v(v) {}
    /**
     * Returns the string representation of this share flag,
     * mimicking Java's Enum.name()
     */
    virtual const T& name() { return nmp[v]; }
};

}
