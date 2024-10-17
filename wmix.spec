%define version 3.5
%define release  1
%define name wmix

Summary: Dockapp OSS sound mixer
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Sound
# New release tagged but source archive not released. So, we download tagged git and create archive by hand:
# Source taken from here: https://repo.or.cz/dockapps.git
Source0: %{name}-%{version}.tar.lzma
Source1: %{name}-icons.tar.bz2
URL: https://dockapps.org/file.php/id/58
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xpm)
BuildRequires: glibc-devel
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(alsa)

Recommends:      alsa-oss
Recommends:      ossp 

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
autoreconf --force --install
%configure
%make_build CFLAGS="%optflags" LDFLAGS="%ldflags"

%install
%make_install
install -D -m 644 sample.wmixrc %{buildroot}%{_datadir}/%{name}/sample.wmixrc

%files
%doc AUTHORS BUGS NEWS README 
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sample.wmixrc
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}.1*



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
