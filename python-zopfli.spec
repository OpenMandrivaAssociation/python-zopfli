%define module zopfli

Name:		python-zopfli
Version:	0.4.1
Release:	1
Summary:	Zopfli  for python
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/obp/py-zopfli
Source0:	https://files.pythonhosted.org/packages/source/z/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	%{_lib}zopfli-devel

%description
pyzopfli is a straight forward wrapper around zopfli's ZlibCompress method.

%prep -a
# Remove bundled egg-info
rm -rf src/%{module}.egg-info/

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%doc README.rst
%dir %{python_sitearch}/%{module}
%{python_sitearch}/%{module}/*
%{python_sitearch}/%{module}-%{version}*.dist-info
