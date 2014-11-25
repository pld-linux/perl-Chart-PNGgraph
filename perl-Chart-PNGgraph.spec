%define		pdir	Chart
%define		pnam	PNGgraph
%include	/usr/lib/rpm/macros.perl
Summary:	Chart::PNGgraph - graph plotting module (deprecated)
Summary(pl.UTF-8):	Chart::PNGgraph - moduł rysujący wykresy (wycofywany)
Name:		perl-Chart-PNGgraph
Version:	1.21
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b235ddafeef8caf0a15e2e492d1e5964
URL:		http://search.cpan.org/dist/Chart-PNGgraph/
BuildRequires:	ImageMagick-perl
BuildRequires:	perl-GIFgraph
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
*** THIS MODULE IS NOW DEPRECATED -- USE GD::Graph INSTEAD ***

This is PNGgraph 1.21, a package to generate PNG charts, using Lincoln
Stein's GD.pm.  It's a wrapper around GD::Graph, provided for backward
compatibility with existing Chart::PNGgraph scripts only.

%description -l pl.UTF-8
*** TEN MODUŁ WYCHODZI Z UŻYTKU -- NALEŻY UŻYWAĆ GD::Graph ***

To jest PNGgraph - pakiet do generowania wykresów PNG przy użyciu
GD.pm Lincolna Steina. Jest to obudowa dla GD::Graph, udostępniona
tylko dla wstecznej kompatybilności z istniejącymi skryptami
Chart::PNGgraph.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README TODO
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
