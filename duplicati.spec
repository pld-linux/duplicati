%include /usr/lib/rpm/macros.mono

# the names of the tags (used in source filenames) are insane
%define tag_code	canary
%define tag_date	2018-12-29

Summary:	Backup client for encrypted online backups
Name:		duplicati
Version:	2.0.4.10
Release:	1
License:	LGPL v2+
Source0:	https://github.com/duplicati/duplicati/releases/download/v%{version}-%{version}_%{tag_code}_%{tag_date}/duplicati-%{version}_%{tag_code}_%{tag_date}.zip
# Source0-md5:	5d5443e04a4a4fe462f24fb2f989ac08
Source1:	duplicati.sh
Source2:	duplicati-cli.sh
Source3:	duplicati-server.sh
Source4:	duplicati.svg
Source5:	duplicati.png
Source6:	duplicati.desktop
Source7:	duplicati.service
Group:		Applications
URL:		http://www.duplicati.com/
BuildRequires:	desktop-file-utils
BuildRequires:	mono-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.596
Requires:	bash
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libappindicator-gtk2
Requires:	mono-addins-gui
Requires:	sqlite3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Duplicati is a free, open source, backup client that securely stores encrypted,
incremental, compressed backups on cloud storage services and remote file
servers. It works with: Amazon S3, OneDrive, Google Drive, Rackspace Cloud
Files, HubiC, Backblaze (B2), Amazon Cloud Drive (AmzCD), Swift / OpenStack,
WebDAV, SSH (SFTP), FTP, and more!

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{_iconsdir}/hicolor/{48x48,scalable}/apps,%{_desktopdir},%{systemdunitdir}}

%{__cp} -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/duplicati
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/duplicati-cli
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/duplicati-server

install -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps
install -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps
install -m644 %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}

#install -m644 %{SOURCE7} $RPM_BUILD_ROOT%{systemdunitdir}

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/OSX*
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/win-tools
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/run-script-example.*

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
%doc *.txt run-script-example.sh
%attr(755,root,root) %{_bindir}/duplicati
%attr(755,root,root) %{_bindir}/duplicati-cli
%attr(755,root,root) %{_bindir}/duplicati-server
%{_desktopdir}/duplicati.desktop
%{_iconsdir}/hicolor/48x48/apps/duplicati.png
%{_iconsdir}/hicolor/scalable/apps/duplicati.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.dll
%{_datadir}/%{name}/*.dll.config
%{_datadir}/%{name}/*.exe
%{_datadir}/%{name}/*.exe.config
%{_datadir}/%{name}/*.txt
%{_datadir}/%{name}/autoupdate.manifest
%{_datadir}/%{name}/SQLite
%{_datadir}/%{name}/SVGIcons
%{_datadir}/%{name}/alphavss
%{_datadir}/%{name}/licenses
%{_datadir}/%{name}/utility-scripts
%{_datadir}/%{name}/webroot
%dir %{_datadir}/%{name}/lvm-scripts
%attr(755,root,root) %{_datadir}/%{name}/lvm-scripts/*.sh
