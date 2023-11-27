# GLSL Notes 2

## Shaders
A shader is a program written in GLSL. There are two types:
* vertex shader
    * every object in 3D (point, text, shape) has number of vertices
    * role is to take care of positioning every vertex
    * code must be type in function named "main"
        * This function will be executed for each of the vertices (if there are 3 vertices then execute 3 times)
* fragment shader
    * role is to colorize vertices in the meshes they form after positioned by vertex shader
    * code must be set in body of main function
        * must also specify a special built-in variable: gl_FragColor
            * where the color of one fragment is stored 
            * values between 0 and 1



