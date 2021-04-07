#ifdef GL_ES
#define LOWP lowp
precision mediump float;
#else
#define LOWP
#endif

uniform vec2 u_step;
uniform vec2 u_cnt;
//uniform vec2 u_size;

uniform sampler2D u_texture;
uniform float u_lower;
uniform float u_upper;

varying LOWP vec4 v_color;
varying vec2 v_texCoord;

varying vec4 v_pos;

void main() {
/*
    float dist = texture2D(u_texture, v_texCoord).a;
   	float alpha = smoothstep(u_lower, u_upper, dist);
    gl_FragColor = vec4(v_color.rgb, alpha);
	//gl_FragColor = vec4(alpha); -- working without blending enabled
    //gl_FragColor = vec4(texture2D(u_texture, v_texCoord).rgb, alpha);
  */

    vec2 idx = round(v_pos.xy / u_step);
    vec4 uuvv = texture2D(u_paras, idx / u_cnt);
    vec4 color = texture2D(u_texture, uuvv);
    gl_FragColor = color;
   	// float alpha = smoothstep(u_lower, u_upper, color.a);
    // gl_FragColor = vec4(texture2D(u_texture, uuvv.xz).rgb, alpha);
}

void bisheng() {
    vec4 colCoord = texture2D(u_texture0, v_texCoord);
    ivec2 paras = floor(colCoord.ba * 10.0);
    float dist = texture2D(u_texture1, colCoord.xy).a;
   	float alpha = smoothstep(u_lower, u_upper, dist);
    gl_FragColor = vec4(v_color.rgb, alpha);
}