%define name esh
%define version 0.7
%define release 1
%define serial 1

Summary: esh, the easy shell.
Name: %{name}
Version: %{version}
Release: %{release}
Serial: %{serial}
Copyright: GPL
Group: Shells
URL: http://esh.netpedia.net
Vendor: Ivan Tkatchev <ivantk@yahoo.com>
Source: %{name}-%{version}.tar.gz
Distribution: Freshmeat RPMs
Packager: Ryan Weaver <ryanw@infohwy.com>
BuildRoot: /tmp/%{name}-%{version}

%description
esh was primarily written out of a need for a simple and lightweight
shell for Unix. As such, it deviates completely from all of the traditional
shells, opting instead for a Lisp-like syntax. This allows exceptionally
small size, both in terms of lines of code and memory consumption, while
retaining remarkable flexibility and programmability.

%prep
%setup -q -n esh

%build
make

cp doc/esh.info .; gzip -9 esh.info

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

install -d $RPM_BUILD_ROOT/bin
install -d $RPM_BUILD_ROOT/usr/info

install -s -m 755 esh $RPM_BUILD_ROOT/bin
install    -m 644 esh.info.gz  $RPM_BUILD_ROOT/usr/info

%post
/sbin/install-info /usr/info/esh.info.gz /usr/info/dir --entry="* esh: (esh).                 esh, the easy shell."

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete /usr/info/esh.info.gz /usr/info/dir --entry="* esh: (esh).                 esh, the easy shell."
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc emacs examples CHANGELOG CREDITS GC_README INSTALL LICENSE READLNE-HACKS TODO
/bin/esh
/usr/info/esh.info.gz

%changelog
* Wed Feb 23 1999 Ryan Weaver <ryanw@infohwy.com>
  [esh-0.7-1]
- Initial RPM Build
- "run" and "run-simple" now return the exit status of the 
  pipeline if the job was launched in the foreground.
- "chop!" and "chop-nl!" now return their arguments.
- Added "begin-last", which is like the "begin" in Scheme.
- Added the "<" and ">" commands.
