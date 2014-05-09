Name:           ttfautohint
Version:        1.1
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
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS COPYING NEWS README THANKS TODO *.TXT
%doc doc/img doc/ttfautohint.{html,pdf,txt}
%{_bindir}/ttfautohint

%files gui
%{_pkgdocdir}/
%{_bindir}/ttfautohintGUI

%changelog
* Wed May 07 2014 Christopher Meng <rpm@cicku.me> - 1.1-1
- Update to 1.1

* Sat Mar 22 2014 Christopher Meng <rpm@cicku.me> - 1.00-1
- Update to 1.00

* Wed Nov 13 2013 Christopher Meng <rpm@cicku.me> - 0.97-1
- Update to 0.97
- Share docs between main<->sub package.

* Fri Aug 09 2013 Christopher Meng <rpm@cicku.me> - 0.96-1
- Initial Package.
