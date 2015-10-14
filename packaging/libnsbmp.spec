Name:       libnsbmp
Summary:    A library of functions for manipulating BMP image format files
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


%prep
%setup -q

%build

./autogen.sh
./configure --prefix=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest libnsbmp.manifest
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_includedir}/*

