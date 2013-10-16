# TODO
# - mono packages can be noarch?
# - remove non-linux binaries
%include /usr/lib/rpm/macros.mono
Summary:	Backup client for encrypted online backups
Name:		duplicati
Version:	1.3.4
Release:	0.1
License:	LGPL v2+
Source0:	http://duplicati.googlecode.com/files/Duplicati%20%{version}.tgz?/Duplicati-%{version}.tgz
# Source0-md5:	4980c4f6c373387e4452a983b235f7f3
Group:		Applications
URL:		http://www.duplicati.com/
BuildRequires:	rpmbuild(macros) >= 1.596
Requires:	bash
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir %{_prefix}/lib/%{name}

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
%setup -q -c

# for files/doc declaration:
mv usr/share/doc/duplicati/README .
rm usr/share/doc/duplicati/changelog.Debian.gz
mv usr/share/doc/duplicati/copyright .
mv usr/share/doc/duplicati/changelog.gz .
rmdir usr/share/doc/duplicati usr/share/doc

rm -r install
rm usr/share/pixmaps/duplicati.xpm

gzip -d changelog.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
cp -a usr $RPM_BUILD_ROOT

# refined desktop file
install -d $RPM_BUILD_ROOT%{_desktopdir}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README copyright changelog
%attr(755,root,root) %{_bindir}/duplicati
%attr(755,root,root) %{_bindir}/duplicati-commandline
%{_desktopdir}/duplicati.desktop
%{_pixmapsdir}/duplicati.png
%dir %{_appdir}
%{_appdir}/*.txt
%{_appdir}/*.dll
%{_appdir}/*.exe
%{_appdir}/*.exe.config
%{_appdir}/*.xml
%{_appdir}/SQLite
%{_appdir}/Tools
%{_appdir}/alphavss
%{_appdir}/licenses
%dir %{_appdir}/lvm-scripts
%attr(755,root,root) %{_appdir}/lvm-scripts/*.sh

%lang(de) %{_appdir}/de-DE
%lang(es) %{_appdir}/es-ES
%lang(fr) %{_appdir}/fr-FR
%lang(it) %{_appdir}/it-IT
%lang(pt_BR) %{_appdir}/pt-BR
%lang(ru) %{_appdir}/ru-RU
%lang(tr_TR) %{_appdir}/tr-TR
%lang(zh_CN) %{_appdir}/zh-CN
%lang(zh_HK) %{_appdir}/zh-HK
%lang(da_DK) %{_appdir}/da-DK
