Summary:	Python 'interface' concept implementation
Summary(pl.UTF-8):	Implementacja interfejsów dla języka Python
Name:		Zope-Interface
Version:	3.4.0
Release:	3
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://download.zope.org/distribution/zope.interface-%{version}.tar.gz
# Source0-md5:	0be9fd80b7bb6bee520e56eba7d29c90
URL:		http://www.zope.org/Products/ZopeInterface/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
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
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
rm $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/*.{txt,c}
rm -r $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/common/tests
rm -r $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt src/zope/interface/{README,human}.txt
%lang(ru) %doc src/zope/interface/{README,human}.ru.txt
%dir %{py_sitedir}/zope
%dir %{py_sitedir}/zope/interface
%{py_sitedir}/zope/interface/*.cfg
%{py_sitedir}/zope/interface/*.py[co]
%attr(755,root,root) %{py_sitedir}/zope/interface/_zope_interface_coptimizations.so
%{py_sitedir}/zope/interface/common
%{py_sitedir}/zope.interface-*.egg-info
%{py_sitedir}/zope.interface-*-nspkg.pth
