
%define oname	mozvoikko
%define name	firefox-ext-mozvoikko
%define version	0.9.5
%define rel	5

%define firefox_ver %(rpm -q --whatprovides mozilla-firefox --queryformat %{VERSION})
%define firefox_epoch %(rpm -q --whatprovides mozilla-firefox --queryformat %{EPOCH})

Summary:	Finnish spell-checking extension for Firefox 3
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPLv2+
Group:		Networking/WWW
URL:		http://voikko.sourceforge.net/
Source:		%oname-%version.tar.gz
Patch0:		mozvoikko-0.9.5-add-inc.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	voikko-devel
BuildRequires:	xulrunner-devel
BuildRequires:	mozilla-firefox
# No automatic dependency on libvoikko.so.1 because it is dlopened:
Requires:	%{_lib}voikko1 >= 1.7
Requires:	firefox = %{firefox_epoch}:%{firefox_ver}
Requires:	voikko-fi
Requires:	locales-fi

%description
Finnish spell-checking extension for Firefox 3 web browser. The
spell-checking is provided by the Voikko library.

%prep
%setup -q -n %oname-%version
%patch0 -p0

%build

%make -f Makefile.xulrunner extension-files \
	CFLAGS="%optflags"

%install
rm -rf %{buildroot}

%make -f Makefile.xulrunner install-unpacked \
	DESTDIR=%{buildroot}%{_libdir}/firefox-%{firefox_ver}/extensions

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/firefox-%{firefox_ver}/extensions/{*-*}

