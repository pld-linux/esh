Summary:	esh, the easy shell
Summary(pl):	esh, prosta pow³oka
Name:		esh
Version:	0.8
Release:	2
License:	GPL
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
Vendor:		Ivan Tkatchev <ivantk@yahoo.com>
Source0:	http://esh.netpedia.net/%{name}-%{version}.tar.gz
URL:		http://esh.netpedia.net/
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
esh zosta³ napisany w pierwszej kolejno¶ci z potrzeby posiadania
prostej i ma³ej pow³oki Unixowej. Jako taki ró¿ni siê od wszystkich
innych shelli, przyjmuj±c sk³adniê podobn± do Lisp'a. To pozwala na
uzyskaæ wyj±tkowo ma³e rozmiary, w rozmiarach kodu jak i w zu¿yciu
pamiêci przy zachowaniu du¿ej elastyczno¶ci i programowalno¶ci.

%prep
%setup -q -n esh

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir}}

install esh $RPM_BUILD_ROOT%{_bindir}
install doc/esh.info $RPM_BUILD_ROOT%{_infodir}

gzip -nf9 emacs/* examples/* CHANGELOG CREDITS GC_README INSTALL LICENSE READLNE-HACKS TODO

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html emacs/*.gz examples/*.gz
%attr(755,root,root) %{_bindir}/esh
%{_infodir}/esh.info.gz
