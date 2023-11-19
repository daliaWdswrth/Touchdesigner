# GLSL Beginner Notes

GLSL stands for OpenGL Shading Language. A programming language which allows a web application to communicate with a graphics card to display 2D to 3D effects on browser. Browser -> GLSL -> GPU (monitor)

 ## Comments:
* Double slash (single line)
* Slash-asterisk (longer comments)
## Variables & Constants
* Specify the type of data to be stored in variable beforehand
* Constants are the same
## Types
* Int, float, bool
* Characters and strings don’t exist in this language
* Once we have assigned a type to a variable, we can’t change it’s value later w/out a conversionfunction
* Regular operations/arithmetic operators exist
* Vectors & Matrices
        * Similar to objects in object-oriented languages
        * Entities composed of basic types
        * Resources for the math behind these types:
            * Freya Holmér - youtube

### Vectors:
#### Types
    * vic 
        * Vec2, vec3, vec4 - (ex) vec2 represents a vector composed of 2 floats
    * ivec
    * bvec
        * bvec4 - (ex) represents a vector composed of 4 booleans
    * Another way of creating a vector when its components have the same value is to specify value only once
    * Can set values from another vector (bigger or equal to the vector)
    * We can use more than 1 vector values to create a new one