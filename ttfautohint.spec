Name:           ttfautohint
Version:        1.8.1
Release:        2%{?dist}
Summary:        Automated hinting utility for TrueType fonts
License:        FTL or GPLv2
URL:            http://www.freetype.org/ttfautohint
Source0:        http://download.savannah.gnu.org/releases/freetype/%{name}-%{version}.tar.gz
BuildRequires:  gcc gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  pkgconfig
BuildRequires:  qt4-devel
Provides:       bundled(gnulib)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
This is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%package        gui
Summary:        GUI for %{name} based on Qt4
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    gui
%{name} is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

This is a GUI of %{name} based on Qt4. 

%package        libs
Summary:        Library for %{name}

%description    libs
lib%{name} is a library which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%package        devel
Summary:        Development files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
lib%{name} is a library which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.


%prep
%setup -q

%build
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%doc AUTHORS NEWS README THANKS TODO *.TXT
%doc doc/img doc/ttfautohint.{html,pdf,txt}
%license COPYING
%{_bindir}/ttfautohint

%files gui
%license COPYING
%{_pkgdocdir}/
%{_bindir}/ttfautohintGUI

%files libs
%license COPYING
%{_libdir}/libttfautohint.so.1*

%files devel
%license COPYING
%{_includedir}/ttfautohint*.h
%{_libdir}/libttfautohint.so
%{_libdir}/pkgconfig/ttfautohint.pc

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 1.8.1-1
- new version (#1531029)
- add shared library

* Tue Nov 14 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 1.7-1
- new version (#1485670)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 1.6-1
- new version (#1400320)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 31 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.5-1
- new version (#1268839)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Christopher Meng <rpm@cicku.me> - 1.3-1
- Update to 1.3

* Sat Oct 11 2014 Christopher Meng <rpm@cicku.me> - 1.2-1
- Update to 1.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Christopher Meng <rpm@cicku.me> - 1.1-1
- Update to 1.1

* Sat Mar 22 2014 Christopher Meng <rpm@cicku.me> - 1.00-1
- Update to 1.00

* Wed Nov 13 2013 Christopher Meng <rpm@cicku.me> - 0.97-1
- Update to 0.97
- Share docs between main<->sub package.

* Fri Aug 09 2013 Christopher Meng <rpm@cicku.me> - 0.96-1
- Initial Package.
