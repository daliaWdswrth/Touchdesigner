# GLSL Notes 1 - Syntax

GLSL stands for OpenGL Shading Language. A programming language which allows a web application to communicate with a graphics card to display 2D to 3D effects on browser. Browser -> GLSL -> GPU (monitor)

 ## Comments:
* Double slash (single line)
* Slash-asterisk (longer comments)
## Variables & Constants
* Specify the type of data to be stored in variable beforehand
* Constants are the same as w/ basically any language
## Types
* Int, float, bool
* Characters and strings don’t exist in this language
* Once we have assigned a type to a variable, we can’t change it’s value later w/out a conversion function
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
* Can set values of one vector from another vector (bigger or equal to the vector)
* We can use more than 1 vector values to create a new one

```glsl
        vec4 vect = vec4(1.0, 2.0, 3.0, 4.0);
        // a1 == a2 == a3 == 1.0
        float a1 = vect.x;
        float a2 = vect.r;
        float a3 = vect.s;

        //Similar process for all components w/ floats a.1 through d.3 (4.0)
```

* If you are working w/ vertices it makes more sense to use x, y, z
* If you are working w/ colors then use r, g, b
* s, t, p if working w/ textures

* Can access more than one component at the same time

```glsl
        //Example:
        vec3 vectA = vec3(1.0, 2.0, 3.0);
        //vectB value is: vec2(1.0, 3.0)
        vect2 vectB = vectA.xz;
```
* Can repeat and take values in different order in vectors

### Matrices
Elements are set in col-major order. To access components, use brackets notation. 

* Can create vectors out of columns of matrix. 
* Unlike a vector, a matrix can have different types of values at the same time

```glsl
        //Example
        //matA value is mat2(1.0, 1.0, 0.0, 0.0)
        mat2 matA = mat2(1, 1, false, false);

        mat3 matB = mat3(7.0, 4.0, 5.0, 0.0, 2.0, 5.0, 1.0, 3.0, 7.0);
        //vectC1 value is: vec3(7.0, 4.0, 5.0)
        vec3 vectC1 = matB[0];
        //replaces 7.0 by 100.0
        matB[2][2] = 100.0;
```

## Samplers
Another type of variable. Stores image data. 
* sampler2D
* samplerCube

## Data Structures 

* Arrays (similar to C and JS)
* Structs
    * Allow you to create your own types

## Storage Qualifiers
* const -> const type variable_identifier = value;
* attribute -> attribute type variable_identifier;
* uniform -> uniform type variable_identifier;
* varying -> varying type variable_identifier;

Attribute and uniform variables receive data from outside of GLSL code (from outside of JS code, more precisely). Differences between the two:
* attribute variable holds data that is different from a vertex (point) to another one
    * ex. vertices of a triangle should each be passed as an attribute because each has different set of coordinates
    * time should be passed as a uniform variable b/c a set of placed vertices share the same time
* the number of attribute variables allotted is less than the number of uniforms
* attribute variables can be used only in the vertex shader/ uniforms are allowed in vertex and fragment shaders
* varying variable stores information about how it'll be interpolated between vertices

## Precision Qualifiers
Represent a way to optimize the resource consumption and manage memory usage more precisley 

* lowp
    * less consuming however must choose right precision because this type can give incorrect results 
* mediump
* highp

```glsl
        //example
        precision_qualifier type variable_identifier;
        exp: mediump float f;

        //set precision for entire type of variables
        precision precision_qualifier type;
        exp: precision highp vec2;
```



## Misc.
* Control flow is similar to other languages
* Functions are also similar in syntax (make sure to specify return type before declaration)
* GLSL has no concept of "main" function like C++ or Java
* See Shaderific.com for built-in function documentation


