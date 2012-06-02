Summary:	Python 'interface' concept implementation
Summary(pl.UTF-8):	Implementacja interfejsów dla języka Python
Name:		Zope-Interface
Version:	4.0.1
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz
# Source0-md5:	d171f8f8a6997409c7680f1dbb3b7e45
URL:		http://www.zope.org/Products/ZopeInterface/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
# set this requirement explicitly, so people know where %py_sitedir/zope
# can be found
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
export CFLAGS="%{rpmcflags}"
%{__python} ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
rm $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/*.c
rm -r $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/common/tests
rm -r $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/tests

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
