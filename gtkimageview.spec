Summary:	A GTK+ widget providing zoomable and panable view of a GdkPixbuf
Name:		gtkimageview
Version:	1.6.3
Release:	1
License:	LGPL v2.1
Group:		X11/Libraries
#Source0:	http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/%{name}-%{version}.tar.gz?format=raw
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	9c241ecf36faeb750d42c5cbc1301bcf
URL:		http://trac.bjourne.webfactional.com/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.6.0
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	 \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}{,/doc}/gtk-doc
rm $RPM_BUILD_ROOT%{_libdir}/lib*.so.?

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/*
