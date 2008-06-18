
%define oname	mozvoikko
%define name	firefox-ext-mozvoikko
%define version	0.9.5
%define rel	1

%define firefox_ver %(rpm -q --qf %%{version} %{_lib}firefox-devel 2>/dev/null || echo 0)

Summary:	Finnish spell-checking extension for Firefox 3
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPLv2+
Group:		Networking/WWW
URL:		http://voikko.sourceforge.net/
Source:		%oname-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	voikko-devel
BuildRequires:	%{_lib}firefox-devel >= 3
# No automatic dependency on libvoikko.so.1 because it is dlopened:
Requires:	%{_lib}voikko1 >= 1.7
Requires:	firefox = %{firefox_ver}
Requires:	voikko-fi
Requires:	locales-fi

%description
Finnish spell-checking extension for Firefox 3 web browser. The
spell-checking is provided by the Voikko library.

%prep
%setup -q -n %oname-%version

%build

%make -f Makefile.xulrunner extension-files \
	CFLAGS="%optflags" \
	XULRUNNER_SDK="%{_libdir}/firefox-devel-%{firefox_ver}" \
	NSPR_INCLUDES=

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

