%define version 3.2
%define release  8
%define name wmix

Summary: Dockapp OSS sound mixer
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Sound
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}-icons.tar.bz2
URL: http://dockapps.org/file.php/id/58
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xpm)

%description
* This is a complete dockapp mixer utilizing the OSS mixer API
* Has a nice On-Screen-Display to visualize current volume levels
* Can adjust main volume, balance, recording status, and mute/unmute channels
* Supports mousewheel to adjust the volume settings
* Supports user specified signals to adjust the volume remotely
* User configuration file can be used to set options

%prep
%setup -q -n %{name}-%{version}

%build
make CFLAGS="%optflags" LDFLAGS="%ldflags"

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_miconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_iconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_liconsdir}
tar xOjf %SOURCE1 %{name}-16x16.xpm > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.xpm
tar xOjf %SOURCE1 %{name}-32x32.xpm > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.xpm
tar xOjf %SOURCE1 %{name}-48x48.xpm > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.xpm

mkdir -p $RPM_BUILD_ROOT%{_usr}/bin/
install -m 755 %{name} $RPM_BUILD_ROOT%{_usr}/bin/

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
gunzip -c wmix.1x.gz | bzip2 -9 -c - > $RPM_BUILD_ROOT%{_mandir}/man1/wmix.1.bz2


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=WMix
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;Audio / Midi / Mixer / Sequencer / Tuner / Audio;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr (-,root,root)
%doc AUTHORS README BUGS NEWS
%{_bindir}/%{name}
%attr(644,root,man) %{_mandir}/man1/*
%{_liconsdir}/%{name}.xpm
%{_miconsdir}/%{name}.xpm
%{_iconsdir}/%{name}.xpm
%{_usr}/share/applications/mandriva-%{name}.desktop



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 3.2-6mdv2011.0
+ Revision: 634817
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 3.2-5mdv2010.0
+ Revision: 434860
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 3.2-4mdv2009.0
+ Revision: 262055
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 3.2-3mdv2009.0
+ Revision: 256186
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 3.2-1mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import wmix


* Thu Jul 18 2006 Franck Villaume <fvill@mandriva.org> 3.2-1mdv2007.0
- new version
- xdg menu

* Mon Apr 11 2005 Franck Villaume <fvill@mandrake.org> 3.1-1mdk
- new version

* Thu Jun 12 2003 Marcel Pol <mpol@gmx.net> 3.0-2mdk
- rebuild for rpm 4.2

* Fri Jun 08 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 3.0-1mdk
- updated to revision 3.0
- fixed owner of %%{_mandir}/man1/*

* Thu May 31 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 2.20-1mdk
- Initial release.
