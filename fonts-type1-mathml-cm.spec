%define name fonts-type1-mathml-cm
%define version 1.0
%define release %mkrel 9
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
