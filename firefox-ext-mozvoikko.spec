%define oname	mozvoikko

Summary:	Finnish spell-checking extension for Firefox
Name:		firefox-ext-mozvoikko
Version:	1.9.0
Release:	%mkrel 7
License:	GPLv2+
Group:		Networking/WWW
URL:		https://voikko.sourceforge.net/
Source:		http://ap1.pp.fi/mozilla/mozvoikko/%version/%oname-%version.tar.bz2
# Patch to build against newest xulrunner
Patch0:         mozvoikko-dict.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	voikko-devel
BuildRequires:	xulrunner-devel
BuildRequires:	firefox-devel
# No automatic dependency on libvoikko.so.1 because it is dlopened:
Requires:	%{_lib}voikko1 >= 1.7
Requires:	firefox >= %{firefox_version}
Requires:	voikko-fi
Requires:	locales-fi

%description
Finnish spell-checking extension for Firefox web browser. The
spell-checking is provided by the Voikko library.

%prep
%setup -q -n %oname
%patch0 -p1

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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-4mdv2011.0
+ Revision: 664309
- mass rebuild

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 1.9.0-3
+ Revision: 640062
- rebuild

* Tue Jan 18 2011 Funda Wang <fwang@mandriva.org> 1.9.0-2
+ Revision: 631489
- update summary

* Tue Jan 18 2011 Funda Wang <fwang@mandriva.org> 1.9.0-1
+ Revision: 631483
- New version 1.9.0

* Mon Jul 26 2010 Thomas Backlund <tmb@mandriva.org> 1.0.1-3mdv2011.0
+ Revision: 560877
- rebuild for new firefox

* Mon Jun 28 2010 Thomas Backlund <tmb@mandriva.org> 1.0.1-2mdv2010.1
+ Revision: 549314
- rebuild for firefox 3.6.6

* Wed Apr 28 2010 Anssi Hannula <anssi@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 540550
- new version
- drop xulrunner-1.9.2.patch (one hunk fixed upstream, other one added as
  a variable in make call instead

* Tue Apr 27 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.0-15mdv2010.1
+ Revision: 539578
- rebuild so that shared libraries are properly stripped again

* Tue Apr 27 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.0-14mdv2010.1
+ Revision: 539577
- rebuild so that shared libraries are properly stripped again

* Wed Apr 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-13mdv2010.1
+ Revision: 532786
- revert the last change

* Wed Apr 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-12mdv2010.1
+ Revision: 532635
- don't provide empty debug package

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 1.0-11mdv2010.1
+ Revision: 531076
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 1.0-10mdv2010.1
+ Revision: 526989
- rebuild

* Sat Jan 23 2010 Funda Wang <fwang@mandriva.org> 1.0-9mdv2010.1
+ Revision: 495182
- build with ff 3.6

* Wed Dec 16 2009 Funda Wang <fwang@mandriva.org> 1.0-8mdv2010.1
+ Revision: 479189
- rebuild for new ff

* Sun Nov 08 2009 Funda Wang <fwang@mandriva.org> 1.0-7mdv2010.1
+ Revision: 462795
- rebuild for new ff

* Wed Sep 16 2009 Funda Wang <fwang@mandriva.org> 1.0-6mdv2010.0
+ Revision: 443379
- fix BR
- rebuild for new ff

* Tue Aug 18 2009 Gustavo De Nardin <gustavodn@mandriva.com> 1.0-5mdv2010.0
+ Revision: 417658
- buildrequiring xulrunner-devel seems enough for firefox 3.5 / xulrunner 1.9.1
- make use of the firefox package macros
- rebuild for firefox 3.5.2

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 1.0-4mdv2010.0
+ Revision: 410507
- rebuild for new ff

* Fri Jul 31 2009 Funda Wang <fwang@mandriva.org> 1.0-3mdv2010.0
+ Revision: 405031
- rebuild for new ff

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 1.0-2mdv2010.0
+ Revision: 385775
- rebuild for new ff

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1.0-1mdv2010.0
+ Revision: 369612
- New version 1.0

* Sat Mar 28 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.9.6-2mdv2009.1
+ Revision: 361852
- rebuild for firefox 3.0.8

* Thu Mar 12 2009 Funda Wang <fwang@mandriva.org> 0.9.6-1mdv2009.1
+ Revision: 354100
- BR ff
- BR unstable
- New version 0.9.6

* Wed Feb 04 2009 Funda Wang <fwang@mandriva.org> 0.9.5-7mdv2009.1
+ Revision: 337340
- rebuild for new ff

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.9.5-6mdv2009.1
+ Revision: 318910
- rebuild for new firefox

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 0.9.5-5mdv2009.1
+ Revision: 303684
- rebuild for new FF

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 0.9.5-4mdv2009.0
+ Revision: 289186
- rebuild for new FF

* Sat Sep 27 2008 Anssi Hannula <anssi@mandriva.org> 0.9.5-3mdv2009.0
+ Revision: 288949
- rebuild for new firefox

* Wed Aug 20 2008 Funda Wang <fwang@mandriva.org> 0.9.5-2mdv2009.0
+ Revision: 274319
- add inc dir
- rebuild for new xulrunner

* Wed Jun 18 2008 Anssi Hannula <anssi@mandriva.org> 0.9.5-1mdv2009.0
+ Revision: 226061
- initial Mandriva release

