%define pkgname actionmailer
Summary:	Mail generator library for Ruby
Summary(pl.UTF-8):	Biblioteka do generowania listów w języku Ruby
Name:		ruby-%{pkgname}
Version:	2.0.5
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/45362/%{pkgname}-%{version}.tgz
# Source0-md5:	ce75e1b795804a48d65707e610d9ce64
URL:		http://rubyforge.org/projects/actionmailer/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-actionpack >= 1.7.0
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Action Mailer uses the Action Pack library to generate template-driven
email.

%description -l pl.UTF-8
Action Mailer używa biblioteki Action Pack do generowania listów
elektronicznych na podstawie szablonów.

%package rdoc
Summary:	Documentation files for ActionMailer
Summary(pl.UTF-8):	Dokumentacja do biblioteki ActionMailer
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ActionMailer.

%description rdoc -l pl.UTF-8
Dokumentacja do biblioteki ActionMailer.

%prep
%setup -q -n actionmailer-%{version}
rm -rf lib/action_mailer/vendor

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
%{__rm} -f ri/created.rid
# external pkgs?
rm -rf ri/Test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_rubylibdir}/action_mailer
%{ruby_rubylibdir}/action_mailer.rb
%{ruby_rubylibdir}/actionmailer.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}
%{ruby_ridir}/ActionMailer
%{ruby_ridir}/MailHelper
