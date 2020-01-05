# Created by pyp2rpm-3.3.3
%global pypi_name zopfli

Name:           python-%{pypi_name}
Version:        0.1.7
Release:        %mkrel 1
Summary:        Zopfli module for python
Group:          Development/Python
License:        ASL
URL:            https://github.com/obp/py-zopfli
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.zip

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
pyzopfli is a straight forward wrapper around zopfli's ZlibCompress method.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pyzopfli is a straight forward wrapper around zopfli's ZlibCompress method.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf src/*.egg-info/

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
