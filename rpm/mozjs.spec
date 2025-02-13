Name:           mozjs
Version:        1.8.5
Release:        1
Summary:        SpiderMonkey JavaScript and WebAssembly library
Url:            https://ftp.mozilla.org/pub/js
Source0:        %{name}-%{version}.tar.bz2
Patch1:         0001-build-sailfishos.patch
License:        MPLv1.1
BuildRequires:  autoconf
BuildRequires:  python
BuildRequires:  zip

%description
SpiderMonkey (mozjs) is the JavaScript and WebAssembly implementation library of the Mozilla Firefox web browser. The implementation behaviour is defined by the ECMAScript and WebAssembly specifications.

%package devel
Summary:        SpiderMonkey development package
Requires:       %{name} = %{version}

%description devel
Development headers and libraries for SpiderMonkey (mozjs), the JavaScript and WebAssembly implementation library of the Mozilla Firefox web browser. The implementation behaviour is defined by the ECMAScript and WebAssembly specifications.

%prep
%autosetup -p2 -n %{name}-%{version}/js-1.8.5

%build
cd js/src
%configure \
    --host=%{_target} \
    --build=%{_target} \
    --target=%{_target} \
    --disable-static \
    --disable-methodjit \
    --disable-monoic \
    --disable-polyic \
    --disable-tracejit \
    --disable-yarrjit \
    --libdir=%{_libdir}

%make_build

%install
cd js/src
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
#%license README.html
%{_bindir}/js-config
%{_libdir}/libmozjs185.so.1.0.0

%files devel
%defattr(-,root,root)
%{_libdir}/libmozjs185.so
%{_libdir}/libmozjs185.so.1.0
%{_libdir}/pkgconfig/mozjs185.pc
%dir %{_includedir}/js
%{_includedir}/js/*.h
%{_includedir}/js/*.tbl
%{_includedir}/js/*.msg

