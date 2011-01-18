%define oname	mozvoikko

Summary:	Finnish spell-checking extension for Firefox 3
Name:		firefox-ext-mozvoikko
Version:	1.9.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/WWW
URL:		http://voikko.sourceforge.net/
Source:		http://ap1.pp.fi/mozilla/mozvoikko/%version/%oname-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	voikko-devel
BuildRequires:	xulrunner-devel
BuildRequires:	firefox-devel
# No automatic dependency on libvoikko.so.1 because it is dlopened:
Requires:	%{_lib}voikko1 >= 1.7
Requires:	firefox >= %{firefox_epoch}:%{firefox_version}
Requires:	voikko-fi
Requires:	locales-fi

%description
Finnish spell-checking extension for Firefox web browser. The
spell-checking is provided by the Voikko library.

%prep
%setup -q -n %oname

%build

%make -f Makefile.xulrunner extension-files \
	CFLAGS="%optflags" \
	XULRUNNER_INCLUDES="$(pkg-config --cflags libxul)" \
	XULRUNNER_LIBS="$(pkg-config --libs libxul) -lmozalloc"
	

%install
rm -rf %{buildroot}

make -f Makefile.xulrunner install-unpacked \
	DESTDIR=%{buildroot}%{firefox_extdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%{firefox_extdir}/*
