uniform mat4 u_projTrans;
uniform mat4 modelWorld;

attribute vec4 a_position;
attribute vec4 a_color;
attribute vec2 a_texCoord0;
attribute vec3 a_normal;

varying vec4 v_color;
varying vec2 v_texCoord;

void main() {
	gl_Position = u_projTrans * modelWorld * a_position;
	//gl_Position = u_projTrans * a_position;
	v_texCoord = a_texCoord0;
	v_color = a_color;
}