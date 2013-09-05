Summary:	Transport Independent RPC Library
Name:		libtirpc
Version:	0.2.3
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libtirpc/%{name}-%{version}.tar.bz2
# Source0-md5:	b70e6c12a369a91e69fcc3b9feb23d61
URL:		http://sourceforge.net/projects/libtirpc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains SunLib's implementation of transport-independent
RPC (TI-RPC) documentation. This library forms a piece of the base of
Open Network Computing (ONC), and is derived directly from the Solaris
2.3 source.

%package devel
Summary:	Development files for the TI-RPC library
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package includes header files necessary for developing programs
which use the TI-RPC library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--enable-gss=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/netconfig
%attr(755,root,root) %ghost %{_libdir}/libtirpc.so.1
%attr(755,root,root) %{_libdir}/libtirpc.so.*.*
%{_mandir}/man5/netconfig.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtirpc.so
%{_includedir}/tirpc
%{_pkgconfigdir}/libtirpc.pc
%{_mandir}/man3/*.3t*

