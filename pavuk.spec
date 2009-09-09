%define name pavuk
%define version 0.9.35
%define release %mkrel 5

Summary:	Pavuk WWW grabber
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Networking/WWW
Source:		http://nchc.dl.sourceforge.net/sourceforge/pavuk/%name-%version.tar.bz2
Patch0:		pavuk-0.9.35-fix-desktop-file.patch
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	gtk2-devel
URL:		http://pavuk.sourceforge.net/

%description
WWW graber used to mirror files located on HTTP, HTTPS, FTP, Gopher servers.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q
%patch0 -p0

%build
%configure --with-x
%make

%install
%makeinstall_std

install -D pavuk.desktop %buildroot/%_datadir/applications/%{name}.desktop

%find_lang %name
 
%if %mdkversion < 200900
%post
%update_menus
%endif
  
%if %mdkversion < 200900
%postun
%clean_menus  
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README BUGS TODO CREDITS 
%doc pavukrc.sample pavuk_authinfo.sample MAILINGLIST wget-pavuk.HOWTO button_icons/
%_bindir/*
%_datadir/icons/*.xpm
%_mandir/man1/*
%{_datadir}/applications/%{name}.desktop
