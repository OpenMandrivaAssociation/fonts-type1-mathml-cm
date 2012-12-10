%define name fonts-type1-mathml-cm
%define version 1.0
%define release %mkrel 11
%define fontdir %{_datadir}/fonts/type1/mathml-cm

Name:          %{name}
Version:       %{version}
Release:       %{release}
License:       freely distributable
Summary:       PostScript Type1 MathML fonts (Computer Modern)
Group:         System/Fonts/Type1
Source0:       ftp://ftp.dante.de/pub/tex/fonts/cm/ps-type1/bluesky/cmps-unix.tar.bz2
URL:           http://www.ams.org/tex/type1-fonts.html
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}
Requires:      font-tools >= 0.1-5mdk
Obsoletes:     fonts-mathml-cm-type1
Provides:      fonts-mathml-cm-type1
BuildArch:     noarch
BuildRequires: fontconfig

%description
This package contains a subset of PostScript fonts of the Knuth's Computer
Modern family, to be used with Xprint.

%prep
%setup -q -n cmpsfont

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{fontdir}
(cd pfb
install -m 644 cmr10.pfb cmmi10.pfb cmex10.pfb cmsy10.pfb \
	$RPM_BUILD_ROOT%{fontdir}/
)

(cd afm
install -m 644 cmr10.afm cmmi10.afm cmex10.afm cmsy10.afm \
	$RPM_BUILD_ROOT%{fontdir}/
)

cat <<EOF > $RPM_BUILD_ROOT%{fontdir}/fonts.dir
4
cmex10.pfb -bsr-cmex10-medium-r-normal--0-0-0-0-p-0-adobe-fontspecific
cmmi10.pfb -bsr-cmmi10-medium-r-normal--0-0-0-0-p-0-adobe-fontspecific
cmr10.pfb -bsr-cmr10-medium-r-normal--0-0-0-0-p-0-adobe-fontspecific
cmsy10.pfb -bsr-cmsy10-medium-r-normal--0-0-0-0-p-0-adobe-fontspecific
EOF

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%{fontdir} \
    %{buildroot}%_sysconfdir/X11/fontpath.d/type1-mathml-cm:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%dir %{fontdir}
%doc README
%attr(644,root,root) %{fontdir}/*.pfb
%attr(644,root,root) %{fontdir}/*.afm
%attr(644,root,root) %{fontdir}/fonts.dir
%{_sysconfdir}/X11/fontpath.d/type1-mathml-cm:pri=50


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-11mdv2011.0
+ Revision: 675582
- br fontconfig for fc-query used in new rpm-setup-build

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2011.0
+ Revision: 618313
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0-9mdv2010.0
+ Revision: 428855
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2009.0
+ Revision: 240719
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0-6mdv2008.0
+ Revision: 52667
- {build,}requires cleanup
- use standard fontsdir location instead of the xprint tree
  (xprint is not even supported anymore)
- fontpath.d conversion (#31756)

* Mon Jul 09 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0-5mdv2008.0
+ Revision: 50635
- remove chkfontpath requirement (it was not used anywhere)
  (BTW, this package is obsolete, since we don't support
  Xprint anymore)
- Import fonts-type1-mathml-cm



* Wed Aug 30 2005 Giuseppe Ghibò <ghibo@mandriva.com> 1.0-4mdk
- Rebuilt.

* Mon Sep 08 2003 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-3mdk
- Changed fontpath from /usr/X11R6/lib/X11/fonts/MathML/Type1/cm to
  /usr/X11R6/lib/X11/xserver/C/print/fonts/MathML/Type1/cm, and don't
  add the fonts to the system fontpath, so that Type1 fonts are used only
  by xprint (as the same version of the fonts, but in TrueType are provided
  also in package fonts-ttf-latex).

* Mon Aug 25 2003 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-2mdk
- cosmetic changes to %%post scripts.
- Removed XftCache (Xft1) support.

* Fri Feb 21 2003 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-1mdk
- Build fontconfig compliant.
- Package renamed to fonts-type1-...

* Sun Sep 08 2002 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-2mdk
- added missed .afm files.

* Mon Jul 29 2002 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-1mdk
- initial release.
