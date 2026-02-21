#
# Conditional build:
%bcond_with	tests	# test suite (requires redis server running)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	redis
Summary:	A Python client for redis
Summary(pl.UTF-8):	Pythonowy klient usługi redis
Name:		python-%{module}
# keep 3.x here for python2 support
Version:	3.5.3
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://files.pythonhosted.org/packages/source/r/redis/redis-%{version}.tar.gz
# Source0-md5:	7a00d4540374f34e152a33faa1fcee5f
URL:		http://github.com/redis/redis-py
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-mock
BuildRequires:	python3-pytest
%endif
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python interface to the Redis key-value store.

%description -l pl.UTF-8
Interfejs Ptyhona do usługi przechowywania danych klucz-wartość Redis.

%package -n python3-%{module}
Summary:	A Python client for redis
Summary(pl.UTF-8):	Pythonowy klient usługi redis
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This is a Python interface to the Redis key-value store.

%description -n python3-%{module} -l pl.UTF-8
Interfejs Ptyhona do usługi przechowywania danych klucz-wartość Redis.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-*.egg-info
