Name:     xf86driproto
Summary:  X.Org X11 Protocol xf86driproto
Version:  2.1.1
Release:  1
Group:    Development/System
License:  MIT
URL:      http://www.x.org
Source0:  %{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: pkgconfig(xorg-macros)

# some file to be intalled can be ignored when rpm generates packages
%define _unpackaged_files_terminate_build 0

%description
%{summary}.

%prep
%setup -q

%build
%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?jobs:-j%jobs}

%install
%make_install

%remove_docs


%files
%defattr(-,root,root,-)
%{_includedir}/X11/dri/*.h
%{_datadir}/pkgconfig/*.pc
