%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Mail generator library for Ruby
Summary(pl):	Biblioteka do generowania listów w jêzyku Ruby
Name:		ruby-ActionMailer
%define tarname actionmailer
Version:	1.0.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/5117/%{tarname}-%{version}.tgz
# Source0-md5:	2f8fba468c27e0f980dd56c452aa9f64
Patch0:	%{name}-sanity.patch
URL:		http://actionpack.rubyonrails.org/
BuildRequires:	ruby
Requires:	ruby
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
%patch0 -p1

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
