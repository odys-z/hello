attribute vec4 a_position;
attribute vec3 a_normal;
attribute vec2 a_texCoord0;

uniform vec3 CameraPos;
uniform mat4 ModelWorld;
uniform mat4 vpMatrix;

uniform float mRefractionRatio;
uniform float mFresnelBias;
uniform float mFresnelScale;
uniform float mFresnelPower;

varying vec3 vReflect;
varying vec3 vRefract[3];
varying float vReflectionFactor;

// varying vec3 normDiff;
varying vec3 cent;

void main() {
/* 28 - 34 FPS */
	//vec4 mwPosition = ModelWorld * vec4( a_position, 1.0 );
	cent = ModelWorld[3].xyz;
	vec4 worldPosition = ModelWorld * vec4( a_position );

	vec3 worldNormal = normalize( mat3( ModelWorld[0].xyz, ModelWorld[1].xyz, ModelWorld[2].xyz ) * a_normal );

	//normDiff = worldNormal - a_normal;

	vec3 I = worldPosition.xyz - CameraPos;

	vReflect = reflect( normalize( I ), worldNormal );
	vRefract[0] = refract( normalize( I ), worldNormal, mRefractionRatio );
	vRefract[1] = refract( normalize( I ), worldNormal, mRefractionRatio * 0.99 );
	vRefract[2] = refract( normalize( I ), worldNormal, mRefractionRatio * 0.98 );
	vReflectionFactor = mFresnelBias + mFresnelScale * pow( 1.0 + dot( normalize( I ), worldNormal ), mFresnelPower );

	gl_Position = vpMatrix * worldPosition;
	//gl_Position.z = ModelWorld[3].z;

/* 34-35 FPS
	vec4 mvPosition = modelViewMatrix * vec4( position, 1.0 );
	vec4 worldPosition = modelMatrix * vec4( position, 1.0 );

	vec3 worldNormal = normalize( mat3( modelMatrix[0].xyz, modelMatrix[1].xyz, modelMatrix[2].xyz ) * normal );

	vec3 I = normalize(worldPosition.xyz - cameraPosition);

	vReflect = reflect( I, worldNormal );
	vRefract[0] = refract( I, worldNormal, mRefractionRatio );
	vRefract[1] = refract( I, worldNormal, mRefractionRatio * 0.99 );
	vRefract[2] = refract( I, worldNormal, mRefractionRatio * 0.98 );
	vReflectionFactor = mFresnelBias + mFresnelScale * pow( 1.0 + dot( I, worldNormal ), mFresnelPower );

	gl_Position = projectionMatrix * mvPosition;
*/
}

