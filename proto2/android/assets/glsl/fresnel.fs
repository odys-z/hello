uniform samplerCube tCube;
uniform vec3 CameraPos;

varying vec3 vReflect;
varying vec3 vRefract[3];
varying float vReflectionFactor;

//varying vec3 normDiff;
varying vec3 cent;

void main() {
	vec4 reflectedColor = textureCube( tCube, vec3( -vReflect.x, vReflect.yz ) );
	reflectedColor.r = 1.0;
	vec4 refractedColor = vec4( 1.0 );

	refractedColor.r = textureCube( tCube, vec3( -vRefract[0].x, vRefract[0].yz ) ).r;
	refractedColor.g = textureCube( tCube, vec3( -vRefract[1].x, vRefract[1].yz ) ).g;
	refractedColor.b = textureCube( tCube, vec3( -vRefract[2].x, vRefract[2].yz ) ).b;

	gl_FragColor = mix( refractedColor, reflectedColor, clamp( 2. * vReflectionFactor, 0.0, 1.0 ) );
	//gl_FragColor = mix( refractedColor, reflectedColor, 1.0);
	//gl_FragColor = vec4(normalize(normDiff), 1.);

	// ES 2.0 don't support this
	// http://stackoverflow.com/questions/25708715/rendering-object-depth-in-opengl-es-2-0
	//gl_FragDepth = length(cent - CameraPos);
}

