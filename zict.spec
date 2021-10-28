#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zict
Version  : 2.0.0
Release  : 25
URL      : https://files.pythonhosted.org/packages/af/16/bb5ce16c6f109ced5abee8be13d9454719c8f60a22d518812af059e6c386/zict-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/af/16/bb5ce16c6f109ced5abee8be13d9454719c8f60a22d518812af059e6c386/zict-2.0.0.tar.gz
Summary  : Mutable mapping tools
Group    : Development/Tools
License  : BSD-3-Clause
Requires: zict-license = %{version}-%{release}
Requires: zict-python = %{version}-%{release}
Requires: zict-python3 = %{version}-%{release}
Requires: HeapDict
BuildRequires : HeapDict
BuildRequires : buildreq-distutils3

%description
====
        
        |Build Status|
        
        Mutable Mapping interfaces.  See documentation_.

%package license
Summary: license components for the zict package.
Group: Default

%description license
license components for the zict package.


%package python
Summary: python components for the zict package.
Group: Default
Requires: zict-python3 = %{version}-%{release}

%description python
python components for the zict package.


%package python3
Summary: python3 components for the zict package.
Group: Default
Requires: python3-core
Provides: pypi(zict)
Requires: pypi(heapdict)

%description python3
python3 components for the zict package.


%prep
%setup -q -n zict-2.0.0
cd %{_builddir}/zict-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603409410
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zict
cp %{_builddir}/zict-2.0.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/zict/7d92778d2dc6b5312893e7c25c4b05e3b602ec56
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zict/7d92778d2dc6b5312893e7c25c4b05e3b602ec56

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
