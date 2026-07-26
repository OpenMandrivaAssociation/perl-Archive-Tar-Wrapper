%define upstream_name    Archive-Tar-Wrapper
Name:		perl-%{upstream_name}
Version:0.42
Release:	2

Summary:	API wrapper around the 'tar' utility
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/haarg/Archive-Tar-Wrapper
Source0:	https://cpan.metacpan.org/authors/id/H/HA/HAARG/Archive-Tar-Wrapper-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Log::Log4perl)
BuildRequires:	perl(File::Which)
BuildArch:	noarch

%description
Archive::Tar::Wrapper is an API wrapper around the 'tar' command line
utility. It never stores anything in memory, but works on temporary
directory structures on disk instead. It provides a mapping between the
logical paths in the tarball and the 'real' files in the temporary
directory on disk.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.140.0-3mdv2011.0
+ Revision: 657384
- rebuild for updated spec-helper

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.140.0-2
+ Revision: 640762
- rebuild to obsolete old packages

* Fri Feb 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1
+ Revision: 638458
- update to new version 0.14

* Thu Feb 03 2011 Shlomi Fish <shlomif@mandriva.org> 0.130.0-1
+ Revision: 635724
- import perl-Archive-Tar-Wrapper



