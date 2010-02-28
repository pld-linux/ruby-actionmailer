%define pkgname actionmailer
Summary:	Mail generator library for Ruby
Summary(pl.UTF-8):	Biblioteka do generowania listów w języku Ruby
Name:		ruby-%{pkgname}
Version:	2.3.5
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	623772ef110fe42f4fbefbf99d8c3524
URL:		http://rubyforge.org/projects/actionmailer/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-actionpack >= 1.7.0
Requires:	ruby-tmail
Requires:	ruby-text-format
Obsoletes:	ruby-ActionMailer
Provides:	ruby-ActionMailer
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
%setup -q -c

%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}

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
