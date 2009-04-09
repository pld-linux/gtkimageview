Summary:	A GTK+ widget providing zoomable and panable view of a GdkPixbuf
Name:		gtkimageview
Version:	1.6.4
Release:	1
License:	LGPL v2.1
Group:		X11/Libraries
#Source0:	http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/%{name}-%{version}.tar.gz?format=raw
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	501367b3f50e69a12208dc9c6ad00b18
URL:		http://trac.bjourne.webfactional.com/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

%package devel
Summary:	Header files for the GtkImageView widget
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.0

%description devel
Header files for the GtkImageView widget.

%package static
Summary:	Static library of the GtkImageView widget
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version libraries of the GtkImageView widget.

%package apidocs
Summary:	GTKImageView API documentation
Summary(pl.UTF-8):	Dokumentacja API GtkImageView
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GtkImageView API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GtkImageView.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libgtkimageview.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkimageview.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkimageview.so
%{_libdir}/libgtkimageview.la
%{_pkgconfigdir}/gtkimageview.pc
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkimageview.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtkimageview
