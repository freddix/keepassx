%define		pre alpha6

Summary:	Free, open source, light-weight and easy-to-use password manager
Name:		keepassx
Version:	2.0
Release:	0.%{pre}.1
License:	GPL v2 and other
Group:		X11/Applications
#Source0:	http://downloads.sourceforge.net/keepassx/%{name}-%{version}.tar.gz
Source0:	https://github.com/keepassx/keepassx/archive/master.zip
# Source0-md5:	42dcd0931c7c1ad8766f109e887d46e2
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	libgcrypt-devel
BuildRequires:	xorg-libXtst-devel
BuildRequires:	zlib-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
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
%setup -qn %{name}-master

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_VERBOSE_MAKEFILE=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/keepassx.desktop

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
%doc CHANGELOG COPYING LICENSE*
%attr(755,root,root) %{_bindir}/keepassx

%dir %{_libdir}/keepassx
%attr(755,root,root) %{_libdir}/keepassx/libkeepassx-autotype-x11.so

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_desktopdir}/keepassx.desktop
%{_iconsdir}/hicolor/*/apps/keepassx.png
%{_iconsdir}/hicolor/*/apps/keepassx.svgz

