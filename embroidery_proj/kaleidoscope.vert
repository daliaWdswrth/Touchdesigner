#ifndef PI
#define PI 3.141592653589793
#endif

#ifndef deg2rad
#define deg2rad (PI/180.0)
#endif

uniform float Kaleidonum;
uniform float rotateZ;
uniform float Fullmode;

float aspect = uTD2DInfos[0].res.z / uTD2DInfos[0].res.a;

layout (location = 0) out vec4 fragColor;

vec2 kaleidoscope(vec2 uv, float n) {
  float angle = PI / n;
  
  float r = length( uv*.5 );
  float a = atan( uv.y, uv.x ) / angle;
  
  a = mix( fract( a ), 1.0 - fract( a ), mod( floor( a ), 2.0 ) ) * angle;
  
  return vec2( cos( a ), sin( a ) ) * r;
}

// counter-clockwise rotation
vec2 rotate(vec2 uv, float degree) {
  float theta = -degree*deg2rad;
  return vec2(cos(theta)*uv.x-sin(theta)*uv.y, sin(theta)*uv.x+cos(theta)*uv.y);
}

 void main() {
 	vec2 uv = 2*(vUV.st-vec2(0.5, 0.5));
 	uv.x *= aspect;
 	uv = rotate(uv, rotateZ);
 	uv = kaleidoscope(uv, Kaleidonum);
 	uv = Fullmode != 0.0 ? (uv*2) : uv+vec2(.5, .5);
 	uv.x /= aspect;

    fragColor = texture(sTD2DInputs[0], uv);
 }