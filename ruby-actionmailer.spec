Summary:	Mail generator library for Ruby
Summary(pl):	Biblioteka do generowania listów w jêzyku Ruby
Name:		ruby-ActionMailer
%define tarname actionmailer
Version:	1.1.1
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/6575/%{tarname}-%{version}.tgz
# Source0-md5:	3649c201096d5e4d0a45f34ddd253c60
URL:		http://actionpack.rubyonrails.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-ActionPack >= 1.7.0
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Action Mailer uses the Action Pack library to generate template-driven
email.

%description -l pl
Action Mailer u¿ywa biblioteki Action Pack do generowania listów
elektronicznych na podstawie szablonów.

%prep
%setup -q -n %{tarname}-%{version}

%build
rm -rf lib/action_mailer/vendor
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/ActionMailer
%{ruby_ridir}/MailHelper
