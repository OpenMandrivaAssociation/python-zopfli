# Created by pyp2rpm-3.3.3
%global pypi_name zopfli

Name:		python-%{pypi_name}
Version:	0.1.7
Release:	2
Summary:	Zopfli module for python
Group:		Development/Python
License:	ASL
URL:		https://github.com/obp/py-zopfli
Source0:	https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

%description
pyzopfli is a straight forward wrapper around zopfli's ZlibCompress method.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf src/*.egg-info/

%build
%py_build

%install
%py_install

%files
%doc README.rst
%dir %{python_sitearch}/%{pypi_name}
%{python_sitearch}/%{pypi_name}/*
%{python_sitearch}/%{pypi_name}-%{version}-py*.egg-info
