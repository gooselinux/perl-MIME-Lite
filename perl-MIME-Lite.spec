Name:           perl-MIME-Lite
Version:        3.027
Release:        2%{?dist}
Summary:        MIME::Lite - low-calorie MIME generator

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/MIME-Lite/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/MIME-Lite-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::More)
BuildRequires:	perl(Email::Date::Format) perl(Mail::Address)
BuildRequires:	perl(MIME::Types) >= 1.28
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# not detected by automated find-requires:
Requires:	perl(Email::Date::Format)
Requires:	perl(MIME::Types) >= 1.28

%description
MIME::Lite is intended as a simple, standalone module for generating (not 
parsing!) MIME messages... specifically, it allows you to output a simple,
decent single- or multi-part message with text or binaryattachments.  It does
not require that you have the Mail:: or MIME:: modules installed.

%prep
%setup -q -n MIME-Lite-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -empty -exec rmdir ';'


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc changes.pod README examples contrib  
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 3.027-2
- rebuild against perl 5.10.1

* Mon Nov  2 2009 Stepan Kasal <skasal@redhat.com> - 3.027-1
- new upstream version

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 3.26-2
- no need to search for *.bs files in noarch rpm

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 3.26-1
- new upstream version
- fix buildrequires
- add requires not detected automatically

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep  2 2008 Paul Howarth <paul@city-fan.org> 3.01-7
- fix FTBFS (#449558)

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> 3.01-6
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.01-5.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sun Sep 10 2006 Mike McGrath <imlinux@gmail.com> 3.01-5
- Rebuild

* Thu Mar 30 2006 Mike McGrath <imlinux@gmail.com> 3.01-4
- New maintainer

* Thu Jun 23 2005 Ralf Corsepius <ralf@links2linux.de> 3.01-3
- Add %%{dist}.

* Wed Apr 06 2005 Hunter Matthews <thm@duke.edu> 3.01-2
- Review suggestions from José Pedro Oliveira

* Fri Mar 18 2005 Hunter Matthews <thm@duke.edu> 3.01-1
- Initial packageing.
