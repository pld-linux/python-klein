%define		module	klein
Summary:	Klein, a Web Micro-Framework
Name:		python-%{module}
Version:	0.2.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/k/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	0aec7a0c1e373ea3e994b1266cf5281f
URL:		https://github.com/twisted/klein
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-TwistedCore >= 12.1
Requires:	python-werkzeug
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Klein is a micro-framework for developing production-ready web
services with Python. It is 'micro' in that it has an incredibly small
API similar to Bottle and Flask. It is not 'micro' in that it depends
on things outside the standard library. This is primarily because it
is built on widely used and well tested components like Werkzeug and
Twisted.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
%{__rm} -r %{module}.egg-info

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
