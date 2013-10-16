Summary:	Backup client for encrypted online backups
Name:		duplicati
Version:	1.3.4
Release:	0.1
License:	LGPL v2+
URL:		http://www.duplicati.com
#Source0:	http://duplicati.googlecode.com/files/Duplicati%20%{version}.tgz
Source0:	Duplicati %{version}.tgz

Requires:	bash
Requires:	desktop-file-utils
Requires:	mono(System)
Requires:	mono(System.Web)
Requires:	mono(System.Windows.Forms)

# we don't want automatic dependencies generation because
# precompiled binaries generates weird ones:
%global __requires_exclude ^mono.*$


%description
Duplicati is a free backup client that securely stores encrypted,
incremental, compressed backups on cloud storage services and remote
file servers. It supports targets like Amazon S3, Windows Live
SkyDrive, Rackspace Cloud Files or WebDAV, SSH, FTP (and many more).

Duplicati has built-in AES-256 encryption and backups be can signed
using GNU Privacy Guard. A built-in scheduler makes sure that backups
are always up-to-date. Last but not least, Duplicati provides various
options and tweaks like filters, deletion rules, transfer and
bandwidth options to run backups for specific purposes.

%prep
%setup -q -c -n %{name}-%{version}-bin


%build
# binary package, nothing to build

%install
rm -rf $RPM_BUILD_ROOT
rm -rf install/
rm -rf usr/share/pixmaps/duplicati.xpm

#for files/doc declaration:
mv usr/share/doc/duplicati/README .
rm usr/share/doc/duplicati/changelog.Debian.gz
mv usr/share/doc/duplicati/copyright .
mv usr/share/doc/duplicati/changelog.gz .
rmdir usr/share/doc/duplicati/ usr/share/doc/
mv usr/ $RPM_BUILD_ROOT

# refined desktop file
cat <<EOF > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
[Desktop Entry]
Categories=System;Archiving;FileTools;Filesystem;
Type=Application
Name=Duplicati
GenericName= Backup tool
GenericName[es]= Copias de respaldo
Comment= Create and maintain local and remote backup copies of your data
Comment[es]= Cree y mantenga copias de seguridad locales y remotas
Exec=duplicati
Icon=duplicati
Terminal=false
StartupNotify=true
EOF

desktop-file-install $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop


%post
/bin/%update_icon_cache_post hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%postun
/bin/%update_icon_cache_post hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%posttrans
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README copyright changelog.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_libdir}/*
