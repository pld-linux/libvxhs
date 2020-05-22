Summary:	The Veritas HyperScale storage connector library
Summary(pl.UTF-8):	Biblioteka dostępu do danych w przestrzeni Veritas HyperScale
Name:		libvxhs
Version:	1.0
%define	gitref	19255696d892a6d50dd39e803e791feedfdd6a07
%define	snap	20170421
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/VeritasHyperScale/libqnio/releases
Source0:	https://github.com/VeritasHyperScale/libqnio/archive/%{gitref}/libqnio-%{snap}.tar.gz
# Source0-md5:	16830e3c777a73d5d57a87f626c5a2dc
Patch0:		%{name}-types.patch
Patch1:		%{name}-link.patch
URL:		https://github.com/VeritasHyperScale/libqnio
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvxhs is a storage connector library for accessing vdisks on Veritas
HyperScale storage.

%description -l pl.UTF-8
libvxhs to biblioteka połączeniowa służąca do dostępu do dysków
wirtualnych w przestrzeni Veritas HyperScale.

%package devel
Summary:	Header files for libvxhs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvxhs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvxhs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvxhs.

%prep
%setup -q -n libqnio-%{gitref}
%patch0 -p1
%patch1 -p1

%build
%{__make} -C src \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	OPTFLAGS="%{rpmcflags} -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBRARY=%{_libdir} \
	TEST_TARGET_DIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/qnio_client
%attr(755,root,root) %{_bindir}/qnio_server
%attr(755,root,root) %{_libdir}/libvxhs.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/qnio
