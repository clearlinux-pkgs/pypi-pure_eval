#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pure_eval
Version  : 0.2.2
Release  : 2
URL      : https://files.pythonhosted.org/packages/97/5a/0bc937c25d3ce4e0a74335222aee05455d6afa2888032185f8ab50cdf6fd/pure_eval-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/97/5a/0bc937c25d3ce4e0a74335222aee05455d6afa2888032185f8ab50cdf6fd/pure_eval-0.2.2.tar.gz
Summary  : Safely evaluate AST nodes without side effects
Group    : Development/Tools
License  : MIT
Requires: pypi-pure_eval-license = %{version}-%{release}
Requires: pypi-pure_eval-python = %{version}-%{release}
Requires: pypi-pure_eval-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# `pure_eval`
[![Build Status](https://travis-ci.org/alexmojaki/pure_eval.svg?branch=master)](https://travis-ci.org/alexmojaki/pure_eval) [![Coverage Status](https://coveralls.io/repos/github/alexmojaki/pure_eval/badge.svg?branch=master)](https://coveralls.io/github/alexmojaki/pure_eval?branch=master) [![Supports Python versions 3.5+](https://img.shields.io/pypi/pyversions/pure_eval.svg)](https://pypi.python.org/pypi/pure_eval)

%package license
Summary: license components for the pypi-pure_eval package.
Group: Default

%description license
license components for the pypi-pure_eval package.


%package python
Summary: python components for the pypi-pure_eval package.
Group: Default
Requires: pypi-pure_eval-python3 = %{version}-%{release}

%description python
python components for the pypi-pure_eval package.


%package python3
Summary: python3 components for the pypi-pure_eval package.
Group: Default
Requires: python3-core
Provides: pypi(pure_eval)

%description python3
python3 components for the pypi-pure_eval package.


%prep
%setup -q -n pure_eval-0.2.2
cd %{_builddir}/pure_eval-0.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643042862
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pure_eval
cp %{_builddir}/pure_eval-0.2.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pure_eval/44c582803d7005baacb1ad03bcc5ad393cbdd95f
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pure_eval/44c582803d7005baacb1ad03bcc5ad393cbdd95f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
