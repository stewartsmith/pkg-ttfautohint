Name:           ttfautohint
Version:        1.5
Release:        1%{?dist}
Summary:        Automated hinting utility for TrueType fonts
License:        FTL or GPLv2
URL:            http://www.freetype.org/ttfautohint
Source0:        http://download.savannah.gnu.org/releases/freetype/%{name}-%{version}.tar.gz
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  qt4-devel
Provides:       bundled(gnulib)

%description
This is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%package        gui
Summary:        GUI for %{name} based on Qt4

%description    gui
%{name} is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

This is a GUI of %{name} based on Qt4. 

%prep
%setup -q

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%doc AUTHORS NEWS README THANKS TODO *.TXT
%doc doc/img doc/ttfautohint.{html,pdf,txt}
%license COPYING
%{_bindir}/ttfautohint

%files gui
%license COPYING
%{_pkgdocdir}/
%{_bindir}/ttfautohintGUI

%changelog
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
