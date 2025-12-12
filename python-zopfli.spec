# Created by pyp2rpm-3.3.3
%global pypi_name zopfli

Name:		python-%{pypi_name}
Version:	0.4.0
Release:	1
Summary:	Zopfli module for python
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/obp/py-zopfli
Source0:	https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	%{_lib}zopfli-devel

%description
pyzopfli is a straight forward wrapper around zopfli's ZlibCompress method.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf src/%{pypi_name}.egg-info/

%build
%py_build

%install
%py_install

%files
%doc README.rst
%dir %{python_sitearch}/%{pypi_name}
%{python_sitearch}/%{pypi_name}/*
%{python_sitearch}/%{pypi_name}-%{version}*.dist-info
