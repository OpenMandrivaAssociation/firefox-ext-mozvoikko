%define oname	mozvoikko

Summary:	Finnish spell-checking extension for Firefox 3
Name:		firefox-ext-mozvoikko
Version:	1.0
Release:	%mkrel 14
License:	GPLv2+
Group:		Networking/WWW
URL:		http://voikko.sourceforge.net/
Source:		http://downloads.sourceforge.net/voikko/%oname-%version.tar.gz
Patch0:		mozvoikko-1.0-xulrunner-1.9.2.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	voikko-devel
BuildRequires:	xulrunner-devel
BuildRequires:	firefox-devel
# No automatic dependency on libvoikko.so.1 because it is dlopened:
Requires:	%{_lib}voikko1 >= 1.7
Requires:	firefox = %{firefox_epoch}:%{firefox_version}
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
	DESTDIR=%{buildroot}%{firefox_mozillapath}/extensions

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%{firefox_mozillapath}/extensions/{*-*}

