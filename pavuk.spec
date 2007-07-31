%define name pavuk
%define version 0.9.35
%define release %mkrel 1

Summary:	Pavuk WWW grabber
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Networking/WWW
Source:		%name-%version.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	gtk2-devel
URL:		http://pavuk.sourceforge.net/

%description
WWW graber used to mirror files located on HTTP, HTTPS, FTP, Gopher servers.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build

%configure --with-x

%make

%install

make DESTDIR=$RPM_BUILD_ROOT install

%{__mkdir} -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
Comment="WWW file grabber"
Exec=%{_bindir}/%{name} -X
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Internet-FileTransfer;
EOF

%find_lang %name
 
%post
%update_menus
  
%postun
%clean_menus  

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL BUGS TODO CREDITS 
%doc pavukrc.sample pavuk_authinfo.sample pavuk.spec pavuk.desktop MAILINGLIST wget-pavuk.HOWTO button_icons/
%_bindir/*
%_datadir/icons/*.xpm
%_mandir/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
