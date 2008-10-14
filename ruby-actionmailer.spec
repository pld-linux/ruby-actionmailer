%define pkgname actionmailer
Summary:	Mail generator library for Ruby
Summary(pl.UTF-8):	Biblioteka do generowania listów w języku Ruby
Name:		ruby-ActionMailer
Version:	1.1.5
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/7648/actionmailer-%{version}.tgz
# Source0-md5:	48c3b18413c52dcf731c459c395489a7
URL:		http://actionpack.rubyonrails.org/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-ActionPack >= 1.7.0
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarc only because of ruby packaging
%define		_enable_debug_packages	0

%description
Action Mailer uses the Action Pack library to generate template-driven
email.

%description -l pl.UTF-8
Action Mailer używa biblioteki Action Pack do generowania listów
elektronicznych na podstawie szablonów.

%package rdoc
Summary:	Documentation files for ActionMailer
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ActionMailer.

%prep
%setup -q -n actionmailer-%{version}
rm -rf lib/action_mailer/vendor

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
%{__rm} -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}/%{name}-%{version}-%{release}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/ri/ActionMailer
%{ruby_ridir}/ri/MailHelper

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}-%{release}
