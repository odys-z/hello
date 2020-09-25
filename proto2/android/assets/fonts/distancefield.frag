#ifdef GL_ES
#define LOWP lowp
precision mediump float;
#else
#define LOWP
#endif

uniform sampler2D u_texture;
uniform float u_lower;
uniform float u_upper;

varying LOWP vec4 v_color;
varying vec2 v_texCoord;

vec4 bisheng() {
    float dist = texture2D(u_texture, v_texCoord.xy).a;
   	float alpha = smoothstep(u_lower, u_upper, dist);
    return vec4(v_color.rgb, alpha);
}

void main() {
    gl_FragColor = bisheng();
}
