%define upstream_name    Archive-Tar-Wrapper
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    API wrapper around the 'tar' utility
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Archive/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cwd)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IPC::Run)
BuildRequires: perl(Log::Log4perl)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Archive::Tar::Wrapper is an API wrapper around the 'tar' command line
utility. It never stores anything in memory, but works on temporary
directory structures on disk instead. It provides a mapping between the
logical paths in the tarball and the 'real' files in the temporary
directory on disk.

It differs from Archive::Tar in two ways:

* *

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


