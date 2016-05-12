# doxy2cppref: turn Doxygen XML information into wiki syntax

This project started as an offspring of the "Library in a week" effort at
C++Now 2016. The idea is to use the Doxygen comments spread over the Boost
source code to generate a bunch of wiki pages in the syntax of
http://cppreference.com

Demo usage:

```
./main.py example/xml/index.xml output
```

to read in the `index.xml` generated by Doxygen and write files into the
directory `output`


:warning: The project is still in its early development stage :warning:


## Dependencies

 * jinja2
 * py.test or nosetest