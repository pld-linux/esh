Summary:	esh, the easy shell
Summary(pl):	esh, prosta pow�oka
Name:		esh
Version:	0.8.5
Release:	1
License:	GPL
Group:		Applications/Shells
Vendor:		Ivan Tkatchev <ivantk@yahoo.com>
#Source0:	http://esh.netpedia.net/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	b59022b88bae24420156d25869b8be54
#URL:		http://esh.netpedia.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

%description
esh was primarily written out of a need for a simple and lightweight
shell for Unix. As such, it deviates completely from all of the
traditional shells, opting instead for a Lisp-like syntax. This allows
exceptionally small size, both in terms of lines of code and memory
consumption, while retaining remarkable flexibility and
programmability.

%description -l pl
esh zosta� napisany w pierwszej kolejno�ci z potrzeby posiadania
prostej i ma�ej pow�oki Unixowej. Jako taki r�ni si� od wszystkich
innych shelli, przyjmuj�c sk�adni� podobn� do Lisp'a. To pozwala na
uzyska� wyj�tkowo ma�e rozmiary, w rozmiarach kodu jak i w zu�yciu
pami�ci przy zachowaniu du�ej elastyczno�ci i programowalno�ci.

%prep
%setup -q -n esh

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir}}

install esh $RPM_BUILD_ROOT%{_bindir}
install doc/esh.info $RPM_BUILD_ROOT%{_infodir}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS GC_README INSTALL READLNE-HACKS TODO doc/*.html emacs examples
%attr(755,root,root) %{_bindir}/esh
%{_infodir}/esh.info*
