Summary:	esh, the easy shell
Name:		esh
Version:	0.8
Release:	1
License:	GPL
Group:		Shells
Group(pl):	Pow³oki
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

%prep
%setup -q -n esh

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir}}

install -s esh $RPM_BUILD_ROOT%{_bindir}
install esh.info $RPM_BUILD_ROOT%{_infodir}

%post
%fix_info_dir

%postun
%fix_info_dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc emacs examples CHANGELOG CREDITS GC_README INSTALL LICENSE READLNE-HACKS TODO
%attr(755,root,root) %{_bindir}/esh
%{_infodir}/esh.info.gz
