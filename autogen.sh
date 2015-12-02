#!/bin/sh

aclocal
autoconf
autoheader
libtoolize
touch NEWS README AUTHORS ChangeLog
automake --add-missing --gnu --copy --no-force
