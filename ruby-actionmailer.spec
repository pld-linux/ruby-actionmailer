%define pkgname actionmailer
Summary:	Mail generator library for Ruby
Summary(pl.UTF-8):	Biblioteka do generowania listów w języku Ruby
Name:		ruby-%{pkgname}
Version:	3.2.19
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	88ae7f86d4b8585a2108581145de6819
URL:		http://rubyforge.org/projects/actionmailer/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-actionpack >= 3.2.19
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

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
#rm -r ri/{system,Net,Test,Text}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}

# install gemspec
install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc
%{ruby_rubylibdir}/action_mailer
%{ruby_rubylibdir}/action_mailer.rb
%{ruby_rubylibdir}/rails/generators/mailer
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/ActionMailer
