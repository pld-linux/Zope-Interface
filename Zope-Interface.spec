Summary:	zope.interface package used in Zope 3
Summary(pl):	Modu³ interface u¿ywany w Zope 3
Name:		ZopeInterface
Version:	3.0.1
Release:	2
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://www.zope.org/Products/ZopeInterface/%{version}final/%{name}-%{version}.tgz
# Source0-md5:	114f302c2b132d43ad4e01d108b4d192
URL:		http://www.zope.org/Products/ZopeInterface/
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zope.interface package used in Zope 3.

%description -l pl
Modu³ interface u¿ywany w Zope 3.

%prep
%setup -q -n %{name}-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/zope
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/zope

find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT/%{py_sitedir}/zope/README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitedir}/zope/*.cfg
%dir %{py_sitedir}/zope
%{py_sitedir}/zope/*.py[co]
%dir %{py_sitedir}/zope/interface
%{py_sitedir}/zope/interface/*.py[co]
%{py_sitedir}/zope/interface/*.cfg
%{py_sitedir}/zope/interface/*.so
%{py_sitedir}/zope/interface/*.txt
%dir %{py_sitedir}/zope/interface/common
%{py_sitedir}/zope/interface/common/*.py[co]
%dir %{py_sitedir}/zope/interface/common/tests
%{py_sitedir}/zope/interface/common/tests/*.py[co] 
%dir %{py_sitedir}/zope/interface/tests
%{py_sitedir}/zope/interface/tests/*.py[co] 
%{py_sitedir}/zope/interface/tests/*.txt
%dir %{py_sitedir}/zope/testing
%{py_sitedir}/zope/testing/*.py[co]
