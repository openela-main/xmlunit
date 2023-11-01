#!/bin/bash
set -e

name=xmlunit
version="$(sed -n 's/Version:\s*//p' *.spec)"

# RETRIEVE
wget "https://github.com/xmlunit/xmlunit/releases/download/v${version}/${name}-${version}-src.tar.gz" -O "${name}-${version}.orig.tar.gz"

rm -rf tarball-tmp
mkdir tarball-tmp
pushd tarball-tmp
tar xf "../${name}-${version}.orig.tar.gz"

# CLEAN TARBALL
rm */GPATH */GRTAGS */GTAGS

tar -czf "../${name}-${version}.tar.gz" *
popd
rm -r tarball-tmp "${name}-${version}.orig.tar.gz"