%define name pavuk
%define version 0.9.35
%define release %mkrel 1

Summary: Pavuk WWW grabber
Name: %name
Version: %version
Release: %release
License: GPL
Group: Networking/WWW
Source: %name-%version.tar.bz2
BuildRoot: %_tmppath/%name-buildroot
URL: http://pavuk.sourceforge.net/

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


(cd $RPM_BUILD_ROOT
mkdir -p ./usr/lib/menu
cat > ./usr/lib/menu/%{name} <<EOF
?package(%{name}):\
command="/usr/bin/pavuk -X"\
title="Pavuk"\
longtitle="WWW file grabber"\
needs="x11"\
icon="www_section.png"\
section="Internet/Other"
EOF
)
 
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
#%_datadir/pixmaps/*.xpm
%_menudir/*
#%_datadir/gnome/apps/Internet/pavuk.desktop
