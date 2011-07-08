%define pkgname actionmailer
Summary:	Mail generator library for Ruby
Summary(pl.UTF-8):	Biblioteka do generowania listów w języku Ruby
Name:		ruby-%{pkgname}
Version:	2.3.11
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	4b76a14a67b2ac8220298c6d3b44792c
Patch0:		%{name}-vendor.patch
URL:		http://rubyforge.org/projects/actionmailer/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-actionpack >= 2.3.11
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
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}
%patch0 -p1

rm -r lib/action_mailer/vendor

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm -r ri/{Net,Test,Text}

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

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/ActionMailer
%{ruby_ridir}/MailHelper
