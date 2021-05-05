using System;
using System.CodeDom;
using System.Collections.ObjectModel;
using System.IO;
using System.Reflection;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Json;
using System.Text;

namespace lession2.frame.protocol {

    class DataContractSurrogate : IDataContractSurrogate {
        public Type GetDataContractType(Type type) {
            return type;
        }
        public Object GetObjectToSerialize(Object obj, Type targetType) {
            if (obj is ZObj) {
                ((ZObj)obj)._name = Convert.ToBase64String(((ZObj)obj).zname);
            }
            return obj;
        }
        public Object GetDeserializedObject(Object obj, Type targetType) {
            if (obj is ZObj) {
                ((ZObj)obj).zname = Convert.FromBase64String(((ZObj)obj)._name);
            }
            return obj;
        }
        public Type GetReferencedTypeOnImport(string typeName, string typeNamespace, Object customData) {
            return null;
        }
        public CodeTypeDeclaration ProcessImportedType(CodeTypeDeclaration typeDeclaration, CodeCompileUnit compileUnit) {
            return typeDeclaration;
        }
        public Object GetCustomDataToExport(Type clrType, Type dataContractType) {
            return null;
        }
        public Object GetCustomDataToExport(MemberInfo memberInfo, Type dataContractType) {
            return null;
        }
        public void GetKnownCustomDataTypes(Collection<Type> customDataTypes) {
        }
    }

    public class Zson {
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
    }

    [DataContract]
    abstract public class ZObj {
        [DataMember]
        public string _name;
        public byte[] zname;
    }


    [DataContract]
    public class EchoPayload : ZObj {
        [DataMember]
        public DateTime localTime;
        [DataMember]
        public DateTime remoteTime;

        [DataMember]
        public string msg;

        public EchoPayload (string msg) {
            localTime = new DateTime();
            this.msg = msg;
        }

        public override string ToString() {
            return string.Format("local {0}, remote {1}, msg {2}", localTime, remoteTime, msg);
        }
    }
}
