Summary:	Python 'interface' concept implementation
Summary(pl.UTF-8):	Implementacja interfejsów dla języka Python
Name:		Zope-Interface
Version:	4.0.3
Release:	2
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz
# Source0-md5:	1ddd308f2c83703accd1696158c300eb
URL:		http://docs.zope.org/zope.interface/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
# set this requirement explicitly, so people know where %py_sitedir/zope can be found
Requires:	Zope-dirs
Provides:	ZopeInterface
Obsoletes:	ZopeInterface
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 'interface' concept implementation.

%description -l pl.UTF-8
Implementacja interfejsów (abstrakcyjnych reprezentacji klas) dla
języka Python.

%prep
%setup -q -n zope.interface-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/*.c
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/common/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt
%dir %{py_sitedir}/zope/interface
%{py_sitedir}/zope/interface/*.py[co]
%attr(755,root,root) %{py_sitedir}/zope/interface/_zope_interface_coptimizations.so
%{py_sitedir}/zope/interface/common
%{py_sitedir}/zope.interface-*.egg-info
%{py_sitedir}/zope.interface-*-nspkg.pth
