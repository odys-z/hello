using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.Text;
using System.Threading.Tasks;

namespace lession2.frame.protocol {

    class DataContractSurrogate : IDataContractSurrogate {
        public Type GetDataContractType(Type type) {
            return type;
        }
        public Object GetObjectToSerialize(Object obj, Type targetType) {
            if (obj is A) {
                ((A)obj)._b = Convert.ToBase64String(((A)obj).b);
            }
            return obj;
        }
        public Object GetDeserializedObject(Object obj, Type targetType) {
            if (obj is A) {
                ((A)obj).b = Convert.FromBase64String(((A)obj)._b);
            }
            return obj;
        }
        public Type GetReferencedTypeOnImport(string typeName, string typeNamespace, Object customData) {
            return null;
        }
        public System.CodeDom.CodeTypeDeclaration ProcessImportedType(System.CodeDom.CodeTypeDeclaration typeDeclaration, System.CodeDom.CodeCompileUnit compileUnit) {
            return typeDeclaration;
        }
        public Object GetCustomDataToExport(Type clrType, Type dataContractType) {
            return null;
        }
        public Object GetCustomDataToExport(System.Reflection.MemberInfo memberInfo, Type dataContractType) {
            return null;
        }
        public void GetKnownCustomDataTypes(Collection<Type> customDataTypes) {
        }
    }

    class Zson {
        // here it is necessary include the Type because "obj" could be null
        public static String toJson(Object obj, Type t) {
            DataContractJsonSerializerSettings settings = new DataContractJsonSerializerSettings();
            settings.DateTimeFormat = new DateTimeFormat("yyyy-MM-ddTHH:mm:ss.fffzzz");
            settings.DataContractSurrogate = new DataContractSurrogate();
            DataContractJsonSerializer j = new DataContractJsonSerializer(t, settings);
            using (MemoryStream m = new MemoryStream()) {
                j.WriteObject(m, obj);
                return Encoding.UTF8.GetString(m.ToArray());
            }
        }
        public static Object fromJson(String s, Type t) {
            DataContractJsonSerializerSettings settings = new DataContractJsonSerializerSettings();
            settings.DateTimeFormat = new DateTimeFormat("yyyy-MM-ddTHH:mm:ss.fffzzz");
            settings.DataContractSurrogate = new DataContractSurrogate();
            DataContractJsonSerializer j = new DataContractJsonSerializer(t, settings);
            using (MemoryStream m = new MemoryStream(Encoding.UTF8.GetBytes(s))) {
                return j.ReadObject(m);
            }
        }
        static void Main() {
            A a = new A();
            a.b = new byte[] { 65, 66, 67, 68 };
            a.s = "xyz";
            a.i = 12345;
            a.d = DateTime.Now;
            String s = toJson(a, typeof(A));
            Console.WriteLine(s);
            A a2 = (A)fromJson(s, typeof(A));
            Console.WriteLine(a2.s + " " + a2.i + " " + a2.b[0] + " " + a2.b[1] + " " +
                                          a2.b[2] + " " + a2.b[3] + " " + a2.d);
        }
    }

}
