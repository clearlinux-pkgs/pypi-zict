#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zict
Version  : 2.2.0
Release  : 36
URL      : https://files.pythonhosted.org/packages/96/ed/c4f036bf588841d18b49a97a7df65604461206b044dc1373c3fa25431c1d/zict-2.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/96/ed/c4f036bf588841d18b49a97a7df65604461206b044dc1373c3fa25431c1d/zict-2.2.0.tar.gz
Summary  : Mutable mapping tools
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-zict-license = %{version}-%{release}
Requires: pypi-zict-python = %{version}-%{release}
Requires: pypi-zict-python3 = %{version}-%{release}
Requires: pypi(heapdict)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(heapdict)

%description
Zict
====
|Build Status| |Linting|
Mutable Mapping tools.  See documentation_.
.. _documentation: http://zict.readthedocs.io/en/latest/
.. |Build Status| image:: https://github.com/dask/zict/actions/workflows/test.yml/badge.svg
:target: https://github.com/dask/zict/actions/workflows/test.yml
.. |Linting| image:: https://github.com/dask/zict/actions/workflows/pre-commit.yml/badge.svg
:target: https://github.com/dask/zict/actions/workflows/pre-commit.yml

%package license
Summary: license components for the pypi-zict package.
Group: Default

%description license
license components for the pypi-zict package.


%package python
Summary: python components for the pypi-zict package.
Group: Default
Requires: pypi-zict-python3 = %{version}-%{release}

%description python
python components for the pypi-zict package.


%package python3
Summary: python3 components for the pypi-zict package.
Group: Default
Requires: python3-core
Provides: pypi(zict)
Requires: pypi(heapdict)

%description python3
python3 components for the pypi-zict package.


%prep
%setup -q -n zict-2.2.0
cd %{_builddir}/zict-2.2.0
pushd ..
cp -a zict-2.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656360111
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zict
cp %{_builddir}/zict-2.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zict/e4e3a49b903643223d20583fc15b06778c418ff9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zict/e4e3a49b903643223d20583fc15b06778c418ff9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
