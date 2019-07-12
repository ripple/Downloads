# Appveyor

Prepackaged headers, binary libs, and protoc.exe, used to
optimize downloads and caching for Appveyor.com CI builds.

* `rippled_deps17.04.zip`
  * Built using and for Visual Studio 2017 with prebuilt OpenSSL
    libraries, including boost atomic library
  * Includes:
    * protoc 2.5.1
    * Boost 1.67
    * OpenSSL 1.0.2j (64-bit) from http://slproweb.com/products/Win32OpenSSL.html
* Version 17.05 splits the single zip file into several to stay under Github's
  file size limits.
  * Built using and for Visual Studio 2017 with prebuilt OpenSSL
  * `rippled_deps.openssl.1.0.2j.zip`
    * Includes:
      * OpenSSL 1.0.2j (64-bit) from http://slproweb.com/products/Win32OpenSSL.html
  * `rippled_deps.boost.1.70.zip`
    * Includes:
      * Boost 1.70, except for the built library binaries in `stage`
  * `rippled_deps.boost.stage.1.70.zip`
    * Includes:
      * Boost 1.70, only the built library binaries in `stage`
