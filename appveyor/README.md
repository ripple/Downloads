# Appveyor

Prepackaged headers, binary libs, and protoc.exe, used to
optimize downloads and caching for Appveyor.com CI builds.

* `rippled_deps.zip`
  * Built using and for Visual Studio 2013.
  * Includes:
    * protoc 2.5.1
    * Boost 1.57
    * OpenSSL (unknown version)
* `rippled_deps15.zip`
  * Built using and for Visual Studio 2015.
  * Includes:
    * protoc 2.5.1
    * Boost 1.59
    * OpenSSL 1.0.2d
* `rippled_deps15.01.zip`
  * Built using and for Visual Studio 2015 with prebuilt OpenSSL
    libraries.
  * Includes:
    * protoc 2.5.1
    * Boost 1.59
    * OpenSSL 1.0.2d (64-bit) from http://slproweb.com/products/Win32OpenSSL.html

