Summary:	Python 'interface' concept implementation
Summary(pl.UTF-8):	Implementacja interfejsów dla języka Python
Name:		Zope-Interface
Version:	3.4.0
Release:	1
License:	ZPL 2.1
Group:		Development/Tools
Source0:	http://download.zope.org/distribution/zope.interface-%{version}.tar.gz
# Source0-md5:	0be9fd80b7bb6bee520e56eba7d29c90
URL:		http://www.zope.org/Products/ZopeInterface/
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
Provides:		ZopeInterface
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 'interface' concept implementation.

%description -l pl.UTF-8
Implementacja interfejsów (abstrakcyjnych reprezentacji klas) dla języka
Python.

%prep
%setup -q -n zope.interface-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%{py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitedir}/zope/interface
%{py_sitedir}/zope*egg*
%{py_sitedir}/zope*pth
