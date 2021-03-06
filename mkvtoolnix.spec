#
# spec file for RPM-based distributions
#

Name: mkvtoolnix
URL: https://www.bunkus.org/videotools/mkvtoolnix/
Version: 7.6.0
Release: 1
Summary: Tools to create, alter and inspect Matroska files
Source: %{name}-%{version}.tar.xz

BuildRequires: fdupes, file-devel, flac, flac-devel, libcurl-devel, libogg-devel, libstdc++-devel, libvorbis-devel, make, pkgconfig

%if 0%{?centos} && 0%{?centos} < 7
BuildRequires: devtoolset-1.1-gcc-c++ >= 4.6.3
%else
BuildRequires: boost-devel >= 1.46.0, gcc-c++ >= 4.6.3, ruby >= 1.9
%endif

%if 0%{?suse_version}
Group: Productivity/Multimedia/Other
License: GPL-2.0
BuildRequires:  gettext-tools, wxWidgets-devel
%endif

%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
Group: Applications/Multimedia
License: GPLv2
BuildRequires: gettext-devel, wxGTK-devel
%endif

%if 0%{?fedora} >= 19
BuildRequires: rubypick
%endif

%if 0%{?fedora}
BuildRequires: pugixml-devel
%endif

%description
Tools to create and manipulate Matroska files (extensions .mkv and
.mka), a new container format for audio and video files. Includes
command line tools mkvextract, mkvinfo, mkvmerge, mkvpropedit and a
graphical frontend for them, mkvmerge-gui.

Authors:
--------
    Moritz Bunkus <moritz@bunkus.org>

%prep
%setup

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"

%if 0%{?centos} && 0%{?centos} < 7
export CC=/opt/centos/devtoolset-1.1/root/usr/bin/gcc
export CXX=/opt/centos/devtoolset-1.1/root/usr/bin/g++
export EXTRA_CONFIGURE_ARGS="--with-boost=/opt/boost"
%endif

%configure --prefix=%{_prefix} --without-build-timestamp $EXTRA_CONFIGURE_ARGS

%build
./drake
./drake apps:strip
%if 0%{?suse_version}
sed -i -e 's/^Exec=mmg/Exec=mkvmerge-gui/' share/desktop/mkvmergeGUI.desktop
%endif

%install
%if 0%{?suse_version}
./drake DESTDIR=$RPM_BUILD_ROOT MMG_BIN=mkvmerge-gui install
%else
./drake DESTDIR=$RPM_BUILD_ROOT install
%endif
%fdupes -s %buildroot/%_mandir
%fdupes -s %buildroot/%_prefix

%files
%defattr (-,root,root)
%doc AUTHORS COPYING README.md ChangeLog TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/doc/mkvtoolnix
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/mime/packages/*.xml
%lang(ca) %{_datadir}/locale/ca/*/*.mo
%lang(cs) %{_datadir}/locale/cs/*/*.mo
%lang(de) %{_datadir}/locale/de/*/*.mo
%lang(es) %{_datadir}/locale/es/*/*.mo
%lang(eu) %{_datadir}/locale/eu/*/*.mo
%lang(fr) %{_datadir}/locale/fr/*/*.mo
%lang(it) %{_datadir}/locale/it/*/*.mo
%lang(ja) %{_datadir}/locale/ja/*/*.mo
%lang(lt) %{_datadir}/locale/lt/*/*.mo
%lang(nl) %{_datadir}/locale/nl/*/*.mo
%lang(pl) %{_datadir}/locale/pl/*/*.mo
%lang(pt) %{_datadir}/locale/pt/*/*.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/*/*.mo
%lang(ru) %{_datadir}/locale/ru/*/*.mo
%lang(sr) %{_datadir}/locale/sr/*/*.mo
%lang(tr) %{_datadir}/locale/tr/*/*.mo
%lang(uk) %{_datadir}/locale/uk/*/*.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/*/*.mo
%lang(zh_TW) %{_datadir}/locale/zh_TW/*/*.mo
%{_datadir}/man/man1/*
%{_datadir}/man/de
%{_datadir}/man/ja
%{_datadir}/man/nl
%{_datadir}/man/uk
%{_datadir}/man/zh_CN

%changelog -n mkvtoolnix
* Sat Nov 15 2014 Moritz Bunkus <moritz@bunkus.org> 7.3.0-1
- Serious reorganization & fixes for rpmlint complaints
