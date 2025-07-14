#
Summary:	Application to get and manage software
Name:		apper
Version:	0.7.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.dropbox.com/u/37314029/%{name}-%{version}.tar.bz2
# Source0-md5:	712b52dd9bd9eda7368d0820404d50f8
Patch0:		%{name}-crash_fix.patch
URL:		http://dantti.wordpress.com/
BuildRequires:	PackageKit-qt2-devel >= 0.6.17
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application to get and manage software.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apper
%dir %{_libdir}/apper
%attr(755,root,root) %{_libdir}/apper/libapper.so
%attr(755,root,root) %{_libdir}/kde4/kcm_apper.so
%attr(755,root,root) %{_libdir}/kde4/kded_apperd.so
%attr(755,root,root) %{_libdir}/kde4/libexec/apper-sentinel
%{_desktopdir}/kde4/apper.desktop
%{_datadir}/apps/apper
%dir %{_datadir}/apps/ApperSentinel
%{_datadir}/apps/ApperSentinel/ApperSentinel.notifyrc
%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service
%{_datadir}/dbus-1/services/org.kde.ApperSentinel.service
%{_datadir}/kde4/services/kded/apperd.desktop
%{_datadir}/kde4/services/kcm_apper.desktop
