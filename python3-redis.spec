#
# Conditional build:
%bcond_with	tests	# test suite (requires redis server running)

%define		module	redis
Summary:	A Python client for redis
Summary(pl.UTF-8):	Pythonowy klient usługi redis
Name:		python3-%{module}
Version:	8.1.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://files.pythonhosted.org/packages/source/r/redis/redis-%{version}.tar.gz
# Source0-md5:	582678e33dbcaaabc7b0e54acd99632f
URL:		https://github.com/redis/redis-py
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
%if %{with tests}
%if "%{py3_ver}" < "3.11.3"
BuildRequires:	python3-async_timeout >= 4.0.3
%endif
BuildRequires:	python3-cryptography >= 36.0.1
BuildRequires:	python3-hiredis >= 3.2.0
BuildRequires:	python3-numpy >= 1.24.0
BuildRequires:	python3-opentelemetry-api >= 1.30.0
BuildRequires:	python3-opentelemetry-exporter-otlp >= 1.30.0
BuildRequires:	python3-opentelemetry-sdk >= 1.30.0
BuildRequires:	python3-pyOpenSSL >= 20.0.1
BuildRequires:	python3-pybreaker >= 1.4.0
BuildRequires:	python3-pyjwt >= 2.9.0
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-asyncio >= 0.24.0
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-pytest-profiling >= 1.8.1
BuildRequires:	python3-pytest-timeout
BuildRequires:	python3-redis-entraid >= 1.0.0
BuildRequires:	python3-requests >= 2.31.0
BuildRequires:	python3-ujson >= 4.2.0
BuildRequires:	python3-uvloop
BuildRequires:	python3-xxhash >= 3.6.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python interface to the Redis key-value store.

%description -l pl.UTF-8
Interfejs Pythona do usługi przechowywania danych klucz-wartość Redis.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/redis
%{py3_sitescriptdir}/redis-%{version}.dist-info
