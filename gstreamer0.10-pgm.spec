Summary:	PGM plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka PGM dla GStreamera
Name:		gstreamer0.10-pgm
Version:	2.0.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://openpgm.googlecode.com/files/gstpgm-%{version}.tar.bz2
# Source0-md5:	4879b9e14234c0d55e3c0057592c9201
URL:		http://openpgm.googlecode.com/
BuildRequires:	gstreamer0.10-devel >= 0.10
BuildRequires:	libpgm-devel >= 5.2
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGM plugin for GStreamer.

%description -l pl.UTF-8
Wtyczka PGM dla GStreamera.

%prep
%setup -q -n gstpgm

%build
# scons file is outdated, doesn't support optflags etc. - build manually
libtool --mode=link --tag=CC %{__cc} %{rpmldflags} %{rpmcflags} %{rpmcppflags} gstpgm.c gstpgmsrc.c gstpgmsink.c -o libgstpgm.la -shared -module -avoid-version $(pkg-config --cflags --libs glib-2.0 gthread-2.0 gstreamer-base-0.10 openpgm-5.2) -rpath %{_libdir}/gstreamer-0.10

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10

libtool --mode=install install libgstpgm.la $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/libgst*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstpgm.so
