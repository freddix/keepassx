Summary:	Free, open source, light-weight and easy-to-use password manager
Name:		keepassx
Version:	0.4.3
Release:	1
License:	GPL v2 and other
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/keepassx/%{name}-%{version}.tar.gz
# Source0-md5:	1df67bb22b2e08df49f09e61d156f508
Patch0:		%{name}-include.patch
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt-qmake
BuildRequires:	xorg-libXtst-devel
Requires(post,postun):	shared-mime-info
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KeePass is a free open source password manager, which helps you
to manage your passwords in a secure way. You can put all your
passwords in one database, which is locked with one master key or
a key file. So you only have to remember one single master password
or select the key file to unlock the whole database. The databases
are encrypted using the best and most secure encryption algorithms
currently known (AES and Twofish).

%prep
%setup -q
%patch0 -p1

%build
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/keepassx.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database

%postun
%update_mime_database
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc COPYING changelog
%attr(755,root,root) %{_bindir}/keepassx
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/mime/packages/keepassx.xml
%{_desktopdir}/keepassx.desktop
%{_pixmapsdir}/keepassx.xpm

%dir %{_datadir}/%{name}/i18n
%lang(de) %{_datadir}/%{name}/i18n/keepassx-de_DE.qm
%lang(pl) %{_datadir}/%{name}/i18n/keepassx-pl_PL.qm

