%define name mandriva-background-project
%define version 2010.1
%define release %mkrel 1

Summary:	Artwork by the Mandriva Community
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{name}-%{version}.tar.bz2
License:	CC-BY-SA
Group:		Graphics
URL:		http://forum.mandriva.com/viewtopic.php?t=91640
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Artwork made by the Mandriva Community. 
If you would like to contribute artwork, 
please post it here: http://forum.mandriva.com/viewtopic.php?t=91640

%package 4x3
Summary:	Artwork by the Mandriva Community
Group:		Graphics
%description 4x3
A collection of pictures made by the Mandriva community for desktop 
backgrounds. This package is specifically for 4:3 aspect ratios, 
ie 1024x768, please use the one that matches your screen size, 
or the KDE4 package if you use KDE4.

%package 5x4
Summary:	Artwork by the Mandriva Community
Group:		Graphics
%description 5x4
A collection of pictures made by the Mandriva community for desktop 
backgrounds. This package is specifically for 5:4 aspect ratios, 
ie 1280x1024, please use the one that matches your screen size, 
or the KDE4 package if you use KDE4.

%package 16x10
Summary:	Artwork by the Mandriva Community
Group:		Graphics
%description 16x10
A collection of pictures made by the Mandriva community for desktop 
backgrounds. This package is specifically for 16:10 aspect ratios, 
ie 1280x800, please use the one that matches your screen size, 
or the KDE4 package if you use KDE4.

%package screensaver
Summary:	Artwork by the Mandriva Community
Group:		Graphics
%description screensaver
Artwork made by the Mandriva community to complement the standard 
Mandriva screensaver.

%package KDE4
Summary:	Artwork by the Mandriva Community
Group:		Graphics
%description KDE4
Artwork made by the Mandriva community for desktop backgrounds. 
This package is specifically for KDE4, there are 3 others 
for use with the other Desktops.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/mdk/backgrounds
cp --recursive -f  4x3/ $RPM_BUILD_ROOT/%{_datadir}/mdk/backgrounds
cp --recursive -f 5x4/ $RPM_BUILD_ROOT/%{_datadir}/mdk/backgrounds
cp --recursive -f 16x10/ $RPM_BUILD_ROOT/%{_datadir}/mdk/backgrounds
install -d $RPM_BUILD_ROOT/%{_datadir}/mdk/screensaver
cp --recursive -f screensaver/* $RPM_BUILD_ROOT/%{_datadir}/mdk/screensaver
install -d $RPM_BUILD_ROOT/%{_datadir}/wallpapers
cp --recursive -f KDE4/* $RPM_BUILD_ROOT/%{_datadir}/wallpapers

%clean
rm -rf ${RPM_BUILD_ROOT}

%files 4x3 
%defattr(-,root,root)
%dir %{_datadir}/mdk/backgrounds/4x3
%{_datadir}/mdk/backgrounds/*

%files 5x4
%defattr(-,root,root)
%dir %{_datadir}/mdk/backgrounds/5x4
%{_datadir}/mdk/backgrounds/5x4/*

%files 16x10
%defattr(-,root,root)
%dir %{_datadir}/mdk/backgrounds/16x10
%{_datadir}/mdk/backgrounds/16x10/*

%files screensaver
%defattr(-,root,root)
%dir %{_datadir}/mdk/screensaver
%{_datadir}/mdk/screensaver

%files KDE4
%defattr(-,root,root)
%dir %{_datadir}/wallpapers
%{_datadir}/wallpapers/*

