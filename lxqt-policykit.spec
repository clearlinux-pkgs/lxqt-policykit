#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE793007AD22DF7E (tsujan2000@gmail.com)
#
Name     : lxqt-policykit
Version  : 0.15.0
Release  : 7
URL      : https://github.com/lxqt/lxqt-policykit/releases/download/0.15.0/lxqt-policykit-0.15.0.tar.xz
Source0  : https://github.com/lxqt/lxqt-policykit/releases/download/0.15.0/lxqt-policykit-0.15.0.tar.xz
Source1  : https://github.com/lxqt/lxqt-policykit/releases/download/0.15.0/lxqt-policykit-0.15.0.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: lxqt-policykit-bin = %{version}-%{release}
Requires: lxqt-policykit-data = %{version}-%{release}
Requires: lxqt-policykit-license = %{version}-%{release}
Requires: lxqt-policykit-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : liblxqt-dev
BuildRequires : lxqt-build-tools
BuildRequires : pkg-config
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : polkit-qt-dev
BuildRequires : qtbase-dev
BuildRequires : qttools-dev

%description
# lxqt-policykit
## Overview
lxqt-policykit is the polkit authentification agent of LXQt.

%package bin
Summary: bin components for the lxqt-policykit package.
Group: Binaries
Requires: lxqt-policykit-data = %{version}-%{release}
Requires: lxqt-policykit-license = %{version}-%{release}

%description bin
bin components for the lxqt-policykit package.


%package data
Summary: data components for the lxqt-policykit package.
Group: Data

%description data
data components for the lxqt-policykit package.


%package license
Summary: license components for the lxqt-policykit package.
Group: Default

%description license
license components for the lxqt-policykit package.


%package man
Summary: man components for the lxqt-policykit package.
Group: Default

%description man
man components for the lxqt-policykit package.


%prep
%setup -q -n lxqt-policykit-0.15.0
cd %{_builddir}/lxqt-policykit-0.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598907290
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1598907290
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-policykit
cp %{_builddir}/lxqt-policykit-0.15.0/LICENSE %{buildroot}/usr/share/package-licenses/lxqt-policykit/7fab4cd4eb7f499d60fe183607f046484acd6e2d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-policykit-agent

%files data
%defattr(-,root,root,-)
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_ar.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_arn.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_ast.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_ca.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_cs.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_cy.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_da.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_de.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_el.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_es.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_fr.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_gl.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_he.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_hu.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_id.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_it.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_ja.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_lt.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_nb_NO.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_nl.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_pl.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_pt.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_ru.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_sk_SK.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_tr.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_uk.qm
/usr/share/lxqt/translations/lxqt-policykit-agent/lxqt-policykit-agent_zh_CN.qm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxqt-policykit/7fab4cd4eb7f499d60fe183607f046484acd6e2d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lxqt-policykit-agent.1
