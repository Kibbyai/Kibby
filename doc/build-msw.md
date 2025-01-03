Copyright (c) 2024 KibbyAi Developers <br />

Distributed under the MIT/X11 software license, see the accompanying
file license.txt or http://www.opensource.org/licenses/mit-license.php.
This product includes software developed by the OpenSSL Project for use in
the OpenSSL Toolkit (http://www.openssl.org/).  This product includes
cryptographic software written by Eric Young (eay@cryptsoft.com) and UPnP
software written by Thomas Bernard.

<h1>Build Windows</h1>

See readme.md and src for instructions on building your own Ai agent with the samecode, the
graphical user interface.



Dependencies
------------
Libraries you need to download separately and build:

| Library  | License | Default Path | Version Used |
| ------------- | ------------- | ------------- | ------------- |
| <a href="http://www.openssl.org/source/">OpenSSL</a>  | Old BSD license with the problematic advertising requirement | \openssl-1.0.1b-mgw | 1.0.1b |
| <a href="http://www.oracle.com/technology/software/products/berkeley-db/index.html">Berkeley DB</a>  | New BSD license with additional requirement that linked software must be free open source | \db-4.8.30.NC-mgw | 4.8.30.NC |
| <a href="http://www.boost.org/users/download/">Boost</a>  | MIT-like license | \boost-1.47.0-mgw  | 1.47.0 |
| <a href="http://miniupnp.tuxfamily.org/files/">miniupnpc</a> | New (3-clause) BSD license | \miniupnpc-1.6-mgw  | 1.6 |

OpenSSL
-------
MSYS shell:
un-tar sources with MSYS 'tar xfz' to avoid issue with symlinks (OpenSSL ticket 2377) <br />
change 'MAKE' env. variable from 'C:\MinGW32\bin\mingw32-make.exe' to '/c/MinGW32/bin/mingw32-make.exe'

    cd /c/openssl-1.0.1b-mgw
    ./config
    make

Berkeley DB
-----------
MSYS shell:

    cd /c/db-4.8.30.NC-mgw/build_unix
    sh ../dist/configure --enable-mingw --enable-cxx
    make

Boost
-----
DOS prompt:

    downloaded boost jam 3.1.18
    cd \boost-1.47.0-mgw
    bjam toolset=gcc --build-type=complete stage

MiniUPnPc
---------
UPnP support is optional, make with USE_UPNP= to disable it.

MSYS shell:

    cd /c/miniupnpc-1.6-mgw
    make -f Makefile.mingw
    mkdir miniupnpc
    cp *.h miniupnpc/

KibbyAi
-------
DOS prompt:

    cd \KibbyAi\src
    mingw32-make -f makefile.mingw
    strip KibbyAi.exe
