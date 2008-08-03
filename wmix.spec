%define version 3.2
%define release %mkrel 4
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
BuildRequires: X11-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

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
CFLAGS="$RPM_OPT_FLAGS" make

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

