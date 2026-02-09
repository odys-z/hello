#pragma once

#include <nlohmann/json.hpp>
#include "anson.h"
#include <entt/meta/meta.hpp>
#include <entt/entt.hpp>
#include <entt/meta/container.hpp>
#include <string>
#include "jprotocol.h"

namespace anson {

inline ostream& serialize_recursive(const entt::meta_any &instance, std::ostream &os);

inline ostream& serialize_kvs(const entt::meta_type &type, const entt::meta_any &instance, std::ostream &os, bool &first) {
    // // 1. First, handle base classes (Recursive)
    // for (auto [id, base] : type.base()) {
    //     serialize_object_fields(base.type(), instance, os, first);
    // }

    // 2. Then, handle fields of the current class
    for (auto [id, data] : type.data()) {
        if (!first) os << ", ";
        first = false;

        // Use .name() from your meta_factory registration
        os << "\"" << data.name() << "\": ";

        // Pass the instance to data.get() to extract the value
        // if (type.is_enum()) ; else
        serialize_recursive(data.get(instance), os);
    }
    return os;
}

inline ostream& serialize_object(const entt::meta_type &type, const entt::meta_any &instance, std::ostream &os) {
    // 1. First, handle base classes (Recursive)
    bool first{true};
    os << "{";

    for (auto [id, base] : type.base())
        serialize_kvs(base, instance, os, first);

    serialize_kvs(type, instance, os, first);

    os << "}";
    return os;
}

inline ostream& serialize_recursive(const entt::meta_any &instance, std::ostream &os) {
    if (!instance) return os;

    auto type = instance.type();

    // 1. Dereference pointers (shared_ptr<EchoReq> -> EchoReq)
    if (type.is_pointer() || type.is_pointer_like()) {
        auto deref = *instance;
        serialize_recursive(deref, os);
        return os;
    }

    // 1. Strings (Specific check before sequence)
    if (auto s = instance.try_cast<std::string>()) {
        os << "\"" << *s << "\"";
        return os;
    }

    // 2. Enums
    if (type.is_enum()) {
        // This will use your overloaded operator<< for anson::Port
        if (auto p = instance.try_cast<anson::Port>()) os << *p;
        return os;
    }

    // 3. Sequence Containers (std::vector, etc.)
    // We use the meta_type to get the sequence view
    if (type.is_sequence_container()) {
        auto view = instance.as_sequence_container();
        // If as_sequence() still fails here, use the explicit version:
        // auto view = entt::meta_sequence_view{instance};
        os << "[";
        bool first = true;
        for (auto element : view) {
            if (!first) os << ", ";
            serialize_recursive(element, os);
            first = false;
        }
        os << "]";
        return os;
    }

    // 4. Associative Containers (std::map)
    if (type.is_associative_container()) {
        auto view = instance.as_associative_container();
        os << "{";
        bool first = true;
        for (auto [key, value] : view) {
            if (!first) os << ", ";
            serialize_recursive(key, os);
            os << ": ";
            serialize_recursive(value, os);
            first = false;
        }
        os << "}";
        return os;
    }

    // 5. Handling std::any for UserReq::data
    if (auto a = instance.try_cast<std::any>()) {
        // Check for shared_ptr<Anson> as requested
        if (a->has_value() && a->type() == typeid(std::shared_ptr<anson::Anson>)) {
            serialize_object(type, instance, os);
        }
        return os;
    }

    // 6. General Objects (Reflection)
    return serialize_object(type, instance, os);
}

inline string serialize_json(const entt::meta_any &instance) {
    if (!instance)  return string(nullptr);

    std::stringstream ss;
    serialize_recursive(instance, ss);
    return ss.str();
}

template<typename T>
class EnTTSaxParser : public nlohmann::json_sax<nlohmann::json> {
private:
    std::vector<entt::meta_any> stack;
    entt::id_type active_key{0};

    inline entt::meta_data find_data_recursive(entt::meta_type type, entt::id_type id) {
        if (!type) return {};

        // Look in current type
        if (auto data = type.data(id)) return data;

        // Look in bases
        for (auto [base_id, base_type] : type.base()) {
            if (auto data = find_data_recursive(base_type, id)) {
                return data;
            }
        }
        return {};
    }

    // Helper to set values on the current object in the stack
    template<typename V>
    void set_value(V&& val) {
        if (!stack.empty() && active_key != 0) {
            auto ref_instance = stack.back().as_ref();
            auto instance = *ref_instance ? (*ref_instance).as_ref() : ref_instance;
            auto data = instance.type().data(active_key);
            // auto data = find_data_recursive(instance.type(), active_key);

            // debug
            // auto curr_type = instance.type();
            // std::cout << "Current type: " << (curr_type ? curr_type.info().name() : "null") << endl;
            // std::cout << "Found data for key " << active_key << ": "
            //           << (data ? "YES" : "NO") << "  name = "
            //           << (data ? data.name() : "n/a") << "\n";

            if (data) {
                // cout << "Anson.type before: " << instance.cast<anson::Anson&>().type << endl;
                data.set(instance, std::forward<V>(val));
                // cout << "Anson.type after: " << instance.cast<anson::Anson&>().type << endl;
            }
        }
    }

public:
    EnTTSaxParser(T& envlop) {
        stack.push_back(&envlop);
    }

    bool start_object(std::size_t size) override {
        if (active_key != 0 && !stack.empty()) {
            auto instance = stack.back().as_ref();
            auto data = instance.type().data(active_key);
            if (data) {
                // Push the member itself onto the stack
                stack.push_back(data.get(instance));
            }
        }
        return true;
    }

    bool key(string_t& val) override {
        active_key = entt::hashed_string{val.c_str()};
        return true;
    }

    bool end_object() override {
        if (stack.size() > 1) stack.pop_back();
        active_key = 0;
        return true;
    }

    // 2. Data Type Handling
    bool number_float(number_float_t val, const string_t&) override {
        set_value(static_cast<float>(val));
        return true;
    }

    bool number_integer(number_integer_t val) override {
        set_value(static_cast<int>(val));
        return true;
    }

    bool string(string_t& val) override {
        set_value(val);
        return true;
    }

    bool boolean(bool val) override {
        set_value(val);
        return true;
    }

    // 3. Boilerplate requirements
    bool null() override { return true; }
    bool number_unsigned(number_unsigned_t val) override { set_value(static_cast<int>(val)); return true; }
    bool binary(binary_t&) override { return true; }
    bool start_array(std::size_t) override { return true; }
    bool end_array() override { return true; }
    bool parse_error(std::size_t, const std::string&, const nlohmann::detail::exception&) override { return false; }

    // Root Management
    void set_root(entt::meta_any instance) { stack.push_back(instance); }
};

}
