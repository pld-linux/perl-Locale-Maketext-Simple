#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	Maketext-Simple
Summary:	Locale::Maketext::Simple - Simple interface to Locale::Maketext::Lexicon
Summary(pl):	Locale::Maketext::Simple - prosty interfejs do Locale::Maketext::Lexicon
Name:		perl-Locale-Maketext-Simple
Version:	0.12
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a65312da2ae8d59f898151f9c044383
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Regexp-Common
BuildRequires:	perl-Test-Simple
# to resolve dependency package name only:
BuildRequires:	perl-Locale-Maketext
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple interface to Locale::Maketext::Lexicon.

%description -l pl
Prosty interfejs do Locale::Maketext::Lexicon.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/%{pdir}/Maketext/*.pm
%{_mandir}/man?/*
