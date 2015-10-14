Name:       libnsbmp
Summary:    A library of functions for decoding BMP image format files
Version:    0.1.1
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.netsurf-browser.org/projects/libnsbmp/
Source0:    http://download.netsurf-browser.org/libnsbmp-%{version}-src.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Libnsbmp is a decoding library for BMP and ICO image file formats, written in C.

%package devel
Summary:    A library of functions for decoding BMP image format files (DEV)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
A library of functions for decoding BMP image format files - Development files.

%prep
%setup -q

%build
./autogen.sh
%configure --prefix=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest libnsbmp.manifest
%license COPYING
%defattr(-,root,root,-)
%{_libdir}/*.so*

%files devel
%manifest libnsbmp.manifest
%defattr(-,root,root,-)
%{_includedir}/*

