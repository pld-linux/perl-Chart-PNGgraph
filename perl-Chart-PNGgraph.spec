%include	/usr/lib/rpm/macros.perl
%define	pdir	Chart
%define	pnam	PNGgraph
Summary:	Chart::PNGgraph - Graph Plotting Module (deprecated)
#Summary(pl):	
Name:		perl-Chart-PNGgraph
Version:	1.21
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRequires:	ImageMagick-perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
*** THIS MODULE IS NOW DEPRECATED -- USE GD::Graph INSTEAD ***

This is PNGgraph 1.21, a package to generate PNG charts, using Lincoln
Stein's GD.pm.  It's a wrapper around GD::Graph, provided for backward
compatibility with existing Chart::PNGgraph scripts only.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc BUGS CHANGES README TODO
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
